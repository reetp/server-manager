#!/usr/bin/perl

use strict;
use warnings;
use utf8;

use Mojolicious::Lite;
use esmith::DB;
use esmith::ConfigDB;

# Mojolicious::Lite
# plugin 'TagHelpers';

# Some sample code to test opening esmith DBs
my $configDB   = esmith::ConfigDB->open_ro          or die("can't open Config DB");
my $networksDB = esmith::ConfigDB->open('networks') or die("Error - cant connect to networks database");

my $key = 'sshd';

my $myKeyStatus = $configDB->get_prop( $key, 'status' ) || 'disabled';

# Used this as test text
my $data = "";
$data .= "A new line<br>";
$data .= "Some Text<br/>";
$data .= "some more Text<br/>";

# Open a 'controller'

get '/' => sub {

    my ($mojo) = @_;

    # Various old test $vars
    # my $mojo = shift;
    # my $test = $mojo->param('Key Value:');
    # my $text        = "Key $key is";

    # Some test code to grab a few bits

    my @connections = $networksDB->keys;

    foreach my $network (@connections) {

        my $netmask = $networksDB->get_prop( $network, 'Mask' ) || "";

        # This will ONLY stash the last value and not an array.
        $mojo->stash( network => $network, netmask => $netmask );

        # This produces an array something like this:
        # ('fish', 'carrot', 'egg', 'spoon', 'banana')
        my @stuff = qw ( fish carrot egg spoon banana );

        # Still not sure how to do this
        # To select a default value we have to get an array more like this (just demo stuff)
        # [[Germany => 'de', selected => 'selected'], [English => 'en'], 'us']
        # This should give us something like
        # <option selected="selected" value="de">Germany</option>
        # Either need to setup the array differently, or modify the select_field template line
        # Probably the latter

        # This bit works for the above array
        $mojo->stash( stuff => \@stuff );

    }

    #$c->render(text => "$text $myKeyStatus</br>New Line<br />$data");
    #$c->render(template=>'hello');
    # $mojo->render( template => 'hello', foo => 'test', bar => 23 );
    $mojo->stash( contentVar => '_content' );
    $mojo->render( template => 'main' );
};

# Sample - this answers http 'GET' requests
get '/update' => sub {
    print 'hello';
};

# This answers http 'POST'

# Access request information
# This will output the browser data - the form user /result to get here
# no idea yet how to get the posted form data

post '/' => sub {

    my $mojo = shift;

    # my ($mojo) = @_;

    my $host = $mojo->req->url->to_abs->host;
    my $ua   = $mojo->req->headers->user_agent;

    my $list = $mojo->param('list');
    $mojo->stash( listR => $list );

    my $pass = $mojo->param('pass');
    $mojo->stash( passR => $pass );

    my $country = $mojo->param('country');
    $mojo->stash( countryR => $country );

    #    $c->render( text => "Request by $ua reached $host. <br />Form data is $data <br /> Country is $radio <br />Pass is $pass");
    $mojo->stash( contentVar => '_result' );

    # here is where we are stuck - it shoudl render main with _result embedded. But it doesn't
    # I think there may be somethign buffered or otherwise held in memory
    $mojo->render( template => 'main' );

};

app->start;

__DATA__

@@ _content.html.ep

<!-- Main content -->

<form name="list" action="" method="POST">



<div>
% param country => 'germany' unless param 'country';
<br />
<%= radio_button 'country' => 'germany' %> Germany
<%= radio_button 'country' => 'france'  %> France
<%= radio_button 'country' => 'uk'      %> UK
</div>

<br />

<div>
<%= select_field 'list' => [ @{ stash('stuff') }], id=> 'dropdown' %>
</div>

<br />
<div>
Password
<%= password_field 'pass', id => 'foo' %>
</div>

<br />
<div>
<input type="submit" value="Submit">
</div>
</form>

      <section class="content">
        <h2>Welcome to the server manager</h2>

        <p>Welcome to SME Server, the leading Linux distribution for small and medium enterprises. SME Server is brought to you by Koozali Foundation, Inc., a non-profit corporation that exists to provide marketing and legal support for SME Server.</p>

        <p>SME Server is freely available under the GNU General Public License and is only possible through the efforts of the SME Server community. However, the availability and quality of SME Server is dependent on meeting our expenses, such as hosting costs, server hardware, etc.</p>

        <p>As such, we ask for a donation to offset costs and fund further development.</p>

        <p>a) If you are a school, a church, a non-profit organisation or an individual using SME for private purposes, we would appreciate it if you could contribute within your means toward the costs associated with hosting, maintenance and development.<br>
        b) If you are a company or an integrator and you are deploying SME in the course of your work to generate revenue, we expect you to make a donation commensurate with the level of revenue you generate and the number of servers your have in the field. Please, help the project</p>

        <p><a href="http://wiki.contribs.org/Donate/"><img src="../server-manager/img/btn_donateCC_LG.gif" alt="DONATE"></a></p>

        <p>This software comes with ABSOLUTELY NO WARRANTY. Please click here to view detailed support, warranty and licensing information.</p>

        <p>To perform a system administration function, click one of the links in the menu on the left of your screen.</p>
      </section><!-- /.content -->


@@ _result.html.ep

<div>
      <section class="content">
         <p>Returned Values</p>
         First line is
         <%= $listR %>
         <br />
         Second Line is 
         <%= $passR %>
         <br />
         Third line is 
         <%= $countryR %>
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
