#!/usr/bin/perl 
# no -d allowed when running suid from the cgi-bin dir :-(
#-wT
# vim: ft=xml:

#----------------------------------------------------------------------
# heading     : Configuration
# description : E-mail WBL
# navigation  : 6000 6710
#----------------------------------------------------------------------

use strict;
use warnings;
use Mojolicious::Lite;
use esmith::wblNew;

# We can use separate template in templates/somefile.html.ep
# plugin 'HTMLTemplateProRenderer';

# Load up our wbl subroutines
# my $f = esmith::wblNew->new();

# Initial setup when called
get '/' => sub {

    my ($mojo) = @_;

    # Setup our 3 buttons
    # $mojo->stash( RBL => 'RBL List', Black => 'Black List', White => 'White List' );

    # Or use a dropdown list
    my @wblList = ( 'RBL List', 'Black List', 'White List' );
    $mojo->stash( list => \@wblList );

    # This is the template fragment to be embedded in main
    $mojo->stash( contentVar => '_choice' );

    # And now we render main
    $mojo->render( template => 'main' );

};

#get 'test1' => sub {
#};

#get 'test2' => sub {
#};

# called via post
post '/' => sub {

    # push the returned array to the $mojo array
    my $mojo = shift;

    my $button = $mojo->param('button');

    # This is the name used in the select_files e.g. 'list'
    my $list = $mojo->param('list');

    # We should put the vars below into these SWITCH statements
    # We can then check the call in the $list var.
    # If it is a straightforward POST call we return a template
    # If it is like wbl.cgi?get_dnsbl or wbl.cgi?get_rblSettings or similar
    # we could return some JSON instead
    # Just needs some logic to figure the call style and output relevant data
    
    SWITCH: {
        if ( $list =~ /^RBL List/ ) {
            $mojo->stash( contentVar => '_rbl' );
            $mojo->stash( listR      => $list );
        }
        if ( $list =~ /^Black List/ ) {
            $mojo->stash( contentVar => '_black' );
            $mojo->stash( listR      => $list );
        }
        if ( $list =~ /^White List/ ) {
            $mojo->stash( contentVar => '_white' );
            $mojo->stash( listR      => $list );
        }

        # Fall through back to choice list
        # Not sure how do do an 'else' though !
#        my @wblList = ( 'RBL List', 'Black List', 'White List' );
#        $mojo->stash( list       => \@wblList );
#        $mojo->stash( contentVar => '_choice' );
    }

    # Hmm some of this comes back as a carriage return separated array
    # For now removed the \n and join in the wbl.pm file
    # eg joe@domain.com\nfred@domain.com
    #
    
    # The following should probably go in the above switch routines so they only get called as required
    # You can then do some logic to either call a template to output the data,
    # or alternatively answer a query with some JSON instead

    # For RBL List
    # dnsbl - returns 'enabled/disabled
    my $dnsbl = get_dnsbl();
    $mojo->stash( dnsbl => $dnsbl );
    
    # rhsbl - returns 'enabled/disabled
    my $rhsbl = get_rhsbl();
    $mojo->stash( rhsbl => $rhsbl );
    
    # uribl - returns 'enabled/disabled
    my $uribl = get_uribl();
    $mojo->stash( uribl => $uribl );
    
    # For SBLList List
    my @sbllist = get_sbllist();
    $mojo->stash( sbllist => \@sbllist );

    # For RBLList List
    my @rbllist = get_rbllist();
    $mojo->stash( rbllist => \@rbllist );
    
    # For URLList List
    my @ubllist = get_ubllist();
    $mojo->stash( ubllist => \@ubllist );
    

    # For Black List
    my @badhelo = get_badhelo();
    $mojo->stash( badhelo => \@badhelo );
    
    my @badmailfrom = get_badmailfrom();
    $mojo->stash( badmailfrom => \@badmailfrom );


    # For WBL List
    my @whitelistsenders = get_whitelistsenders();
    $mojo->stash( whitesenders => \@whitelistsenders );

    my @whitelisthelo = get_whitelisthelo();
    $mojo->stash( whitehelo => \@whitelisthelo );

    my @whitelisthosts = get_whitelisthosts();
    $mojo->stash( whitehosts => \@whitelisthosts );

    my @whitelistfrom = get_whitelistfrom();
    $mojo->stash( whitefrom => \@whitelistfrom );

    # Ignore this = was thinking choice buttons instead of a dropdown.
    # Decide what to do depending on the button

    $mojo->render( template => 'main' );
};

app->start;

__DATA__

@@ _choice.html.ep

<div>
      <section class="content">
      
%#Some Form Buttons
%#= button_to Test => 'http://home.reetspetit.net/'
%#= button_to Remove => './wbl.cgi'

<form name="choice" action="" method="POST">

Test dropbown list
<div>
<%= select_field 'list' => [ @{ stash('list') }], id=> 'dropdown' %>
</div>
<br />

<input type="submit" value="Submit">
</form>
      </section><!-- /.content -->
</div>

@@ _black.html.ep

<div>
      <section class="content">
         <p>Returned Values</p>
         First line is from returned from list: 
         <%= $listR %>
         <br />
      </section><!-- /.content -->
</div>
<br />

<div>
      <section class="content">
      
      Form starts here
      <br />

<table>
<tbody>
<tr>

<form name="list" action="" method="POST">


<b>Blacklist  helo</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('badhelo') }) {
%= $_
% }
%end
<br />

<b>Blacklist  helo</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('badmailfrom') }) {
%= $_
% }
%end
<br />
<input type="submit" value="Submit">
</form>

</tr>
</tbody>
</table>

<br />
<br />

      </section><!-- /.content -->
</div>


@@ _rbl.html.ep

<div>
      <section class="content">
         <p>Returned Values</p>
         First line is from returned from list: 
         <%= $listR %>
         <br />
      </section><!-- /.content -->
</div>
<br />
<div>
      <section class="content">
      Form starts here
      <br />
      <br />
      
<b>DNSBL</b>
<br />
% param dnsbl => 'disabled' unless $dnsbl eq 'enabled';
<%= radio_button 'dnsbl' => 'enabled' %> Enabled
<%= radio_button 'dnsbl' => 'disabled'  %> Disabled

<br />
<br />

<b>RHSBL</b>
<br />
<%= radio_button 'rhsbl' => 'enabled' %> Enabled
<%= radio_button 'rhsbl' => 'disabled'  %> Disabled

<br />
<br />

<b>URI BL</b>
<br />
<%= radio_button 'uribl' => 'enabled' %> Enabled
<%= radio_button 'uribl' => 'disabled'  %> Disabled

<br />
<br />

<form name="list" action="" method="POST">

<table>
<tbody>
<tr>
<b>RBL List</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('rbllist') }) {
%= $_
% }
%end
<br />
<tr />

<tr>
<b>SBL List</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('sbllist') }) {
%= $_
% }
%end
<br />

<b>URL List</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('ubllist') }) {
%= $_
% }
%end
<br />

</tr>
</tbody>
</table>

<input type="submit" value="Submit">
</form>

<br />
<br />

      </section><!-- /.content -->
</div>


@@ _white.html.ep

<div>
      <section class="content">
         <p>Returned Values</p>
         First line is from returned from list: 
         <%= $listR %>
         <br />
      </section><!-- /.content -->
</div>
<br />
<div>
      <section class="content">
      
      Form starts here
<br />


<form name="list" action="" method="POST">
<table>
<tbody>
<tr>

<b>Whitelist  hosts</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('whitehosts') }) {
%= $_
% }
%end
<br />
<br />

<b>Whitelist  helo</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('whitehelo') }) {
%= $_
% }
%end
<br />
<br />

<b>Whitelist senders</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('whitesenders') }) {
%= $_
% }
%end
<br />
<br />

<b>Spamassasin from</b>
<br />
%= text_area story => (cols => 40) => begin
% for (@{ stash('whitefrom') }) {
%= $_
% }
%end
<br />
<br />

<input type="submit" value="Submit">
</form>

</tr>
</tbody>
</table>

<br />
<br />
Sample text areas
<br />

%= text_area 'story'
<br />
%= text_area 'story', cols => 40
<br />
%= text_area story => 'Default\nDove', cols => 40
<br />
%= text_area story => (cols => 40) => begin
  Default
  Swan
% end
<br />
<br />

      </section><!-- /.content -->
</div>


@@ main.html.ep
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">

  <title>Koozali | Dashboard</title>
  <meta content='width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no' name='viewport'>
  <link href="../server-manager/img/favicon.ico" rel="shortcut icon" type="image/x-icon">
  <link href="../server-manager/css/bootstrap.min.css" rel="stylesheet" type="text/css">
  <link href="../server-manager/css/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css"><!-- Theme style -->
  <link href="../server-manager/css/AdminLTE.css" rel="stylesheet" type="text/css">
</head>

<body class="skin-koozali-green">
  <!-- header logo: style can be found in header.less -->

  <header class="header">
    <a href="http://koozali.org" class="logo"><img src="../server-manager/img/koozali.png" alt="Koozali Foundation"></a>
      <!--  <a href="index.html" class="logo icon"> =-->
      <!-- Add the class icon to your logo image or logo icon to add the margining -->
      <!---  Koozali Server  </a> =-->
      <!-- Header Navbar: style can be found in header.less -->

    <nav class="navbar navbar-static-top" role="navigation">
      <!-- Sidebar toggle button-->
       <a href="#" class="navbar-btn sidebar-toggle" data-toggle="offcanvas" role="button"><span class="sr-only">Toggle navigation</span></a>

      <div class="navbar-right">
        <ul class="nav navbar-nav">
          <!-- User Account: style can be found in dropdown.less -->

          <li class="dropdown user user-menu">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span>Admin </span></a>

            <ul class="dropdown-menu">
              <li class="user-footer">
                <div class="pull-right">
                  <a href="#" class="btn btn-default btn-flat">Sign out</a>
                </div>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
  </header>

  <div class="wrapper row-offcanvas row-offcanvas-left">
    <!-- Left side column. contains the logo and sidebar -->

    <aside class="left-side sidebar-offcanvas">
      <!-- sidebar: style can be found in sidebar.less -->

      <section class="sidebar">
        <!-- sidebar menu: : style can be found in sidebar.less -->

        <ul class="sidebar-menu">
          <li class="active"><a href="wbl.cgi"><span>Home</span></a></li>

          <li class="treeview">
            <a href="#"><span>Collaboration</span></a>

            <ul class="treeview-menu">
              <li><a href="/server-manager/cgi-bin/useraccounts">Users</a></li>

              <li><a href="/server-manager/cgi-bin/groups">Groups</a></li>

              <li><a href="/server-manager/cgi-bin/quota">Quotas</a></li>

              <li><a href="/server-manager/cgi-bin/pseudonyms">Pseudonyms</a></li>

              <li><a href="/server-manager/cgi-bin/ibays">Information Bays</a></li>
            </ul>
          </li>

          <li class="treeview">
            <a href="#"><span>Administration</span></a>

            <ul class="treeview-menu">
              <li><a href="/server-manager/cgi-bin/backup">Backup or Restore</a></li>

              <li><a href="/server-manager/cgi-bin/viewlogfiles">View Log Files</a></li>

              <li><a href="/server-manager/cgi-bin/qmailanalog">Mail Log Files</a></li>

              <li><a href="/server-manager/cgi-bin/reboot">Reboot or Shutdown</a></li>
            </ul>
          </li>

          <li class="treeview">
            <a href="#"><span>Security</span></a>

            <ul class="treeview-menu">
              <li><a href="/server-manager/cgi-bin/remoteaccess">Remote Access</a></li>

              <li><a href="/server-manager/cgi-bin/localnetworks">Local Networks</a></li>

              <li><a href="/server-manager/cgi-bin/portforwarding">Port Forwarding</a></li>

              <li><a href="/server-manager/cgi-bin/proxy">Proxy Settings</a></li>
            </ul>
          </li>

          <li class="treeview">
            <a href="#"><span>DB Settings</span></a>

            <ul class="treeview-menu">
              <li><a href="#">DB Settings 1</a></li>

              <li><a href="#">DB Settings 2</a></li>

              <li><a href="#">DB Settings 3</a></li>

              <li><a href="#">DB Settings 4</a></li>
            </ul>
          </li>

          <li class="treeview">
            <a href="#"><span>Configuration</span></a>

            <ul class="treeview-menu">
              <li><a href="/server-manager/cgi-bin/yum">Software Installer</a></li>

              <li><a href="/server-manager/cgi-bin/datetime">Date and Time</a></li>

              <li><a href="/server-manager/cgi-bin/workgroup">Workgroup</a></li>

              <li><a href="/server-manager/cgi-bin/directory">Directory</a></li>

              <li><a href="/server-manager/cgi-bin/printers">Printers</a></li>

              <li><a href="/server-manager/cgi-bin/hostentries">Hostnames and Addresses</a></li>

              <li><a href="/server-manager/cgi-bin/domains">Domains</a></li>

              <li><a href="/server-manager/cgi-bin/emailsettings">E-mail</a></li>

              <li><a href="/server-manager/cgi-bin/clamav">Antivirus (ClamAV)</a></li>

              <li><a href="/server-manager/cgi-bin/review">Review Configuration</a></li>
            </ul>
          </li>

          <li class="treeview">
            <a href="#"><span>Miscellaneous</span></a>

            <ul class="treeview-menu">
              <li><a href="/server-manager/cgi-bin/support">Support and Licensing</a></li>

              <li><a href="/server-manager/cgi-bin/starterwebsite">Create Starter Web Site</a></li>
            </ul>
          </li>
        </ul>
      </section><!-- /.sidebar -->
    </aside>

    <!-- Right side column. Contains the navbar and content of the page -->

    <aside class="right-side">
      <!-- Content Header (Page header) -->

      <section class="content-header">
        <h1>Server-Manager <small>Control panel</small></h1>

        <ol class="breadcrumb">
          <li><a href="#">Home</a></li>

          <li class="active">Server-Manager</li>
        </ol>
      </section>

<%= include $contentVar %>


    </aside><!-- /.right-side -->
  </div><!-- ./wrapper -->


<script src="../server-manager/js/jquery/jquery-2.1.1.min.js" type="text/javascript"></script>
<script src="../server-manager/js/bootstrap/bootstrap.min.js" type="text/javascript"></script>
<script src="../server-manager/js/jquery/jquery-ui-1.10.4.min.js" type="text/javascript"></script>

<!-- AdminLTE App -->
  <script src="../server-manager/js/AdminLTE/app.js" type="text/javascript"></script>

<!-- AdminLTE dashboard demo (This is only for demo purposes) -->
  <script src="../server-manager/js/AdminLTE/dashboard.js" type="text/javascript"></script>

<!-- AdminLTE for demo purposes -->
  <script src="../server-manager/js/AdminLTE/demo.js" type="text/javascript">
</script>

</body>
</html>

