#!/usr/bin/perl
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
    $mojo->stash( RBL => 'RBL List', Black => 'Black List', White => 'White List' );

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
    $mojo->stash( listR => $list );

    $mojo->stash( passR => 'Test Test');
    # OK, lets do one bit and see what occurs
    
    my @dnsbl = get_dnsbl();
    $mojo->stash( dnsbl => \@dnsbl );
    
    # Decide what to do depending on the button
    $mojo->stash( contentVar => '_result' );
    $mojo->render( template => 'main' );
};

app->start;

__DATA__

@@ _choice.html.ep

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


@@ _result.html.ep

<div>
      <section class="content">
         <p>Returned Values</p>
         First line is from dummy list: 
         <%= $listR %>
         <br />
         Second Line is the password field: 
         <%= $passR %>
         <br />


      </section><!-- /.content -->
</div>

Some results here
<br />
Should be the form for the selected page RBL Black or White

<table>
% for (@$dnsbl) {
%   my @columns = split;
%=  tag tr => begin
%   for (@columns) {
%=    tag td => $_
%   }
%   end
% }
</table>




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
          <li class="active"><a href="template.cgi"><span>Home</span></a></li>

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
