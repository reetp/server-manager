#!/usr/bin/perl -w 

# package esmith::FormMagick::Panel::wblNew;
package smeserver::Panel::wblNew;

use strict;
use warnings;
#use esmith::FormMagick;
#use esmith::cgi;
use esmith::ConfigDB;
use esmith::util;
use File::Basename;
use Exporter;
use Carp qw(verbose);

our @ISA = qw( Exporter);

our @EXPORT = qw(
get_dnsbl
get_rhsbl
get_uribl
get_sbllist
get_rbllist
get_ubllist
get_badhelo
get_badmailfrom
get_whitelisthosts
get_whitelisthelo
get_whitelistsenders
get_whitelistfrom
create_modify_black
create_modify_white
email_update
get_blacklistfrom
create_modify_rbl
);

our $VERSION = sprintf '%d.%03d', q$Revision: 1.1 $ =~ /: (\d+).(\d+)/;

our $db = esmith::ConfigDB->open() or die "Couldn't open ConfigDB\n";
our $wdb = esmith::ConfigDB->open('wbl') or die "Couldn't open wbl dbase\n";
our $sdb = esmith::ConfigDB->open('spamassassin') or die "Couldn't open spamassassin dbase\n";

sub get_dnsbl
{
    return ($db->get_prop('qpsmtpd', 'DNSBL') || 'disabled');
}

sub get_rhsbl
{
    return ($db->get_prop('qpsmtpd', 'RHSBL') || 'disabled');
}

sub get_uribl
{
    return ($db->get_prop('qpsmtpd', 'URIBL') || 'disabled');
}

sub get_sbllist
{
my $sbllistform = $db->get_prop('qpsmtpd', 'SBLList') || '';
$sbllistform =~ s/,/\n/g;
return $sbllistform;
}

sub get_rbllist
{
my $rbllistform = $db->get_prop('qpsmtpd', 'RBLList') || '';
$rbllistform =~ s/,/\n/g;
return $rbllistform;
}

sub get_ubllist
{
my $rbllistform = $db->get_prop('qpsmtpd', 'UBLList') || '';
$rbllistform =~ s/,/\n/g;
return $rbllistform;
}


sub get_badhelo
{
    my %list = $wdb->get('badhelo')->props;

    my @badhelo = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "Black") {
            push @badhelo, $parameter;
        }
    }

    return "" unless (scalar @badhelo);

#    return join "\n", sort(@badhelo);
    return sort(@badhelo);
}

sub get_badmailfrom
{
    my %list = $wdb->get('badmailfrom')->props;

    my @badmailfrom = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "Black") {
            push @badmailfrom, $parameter;
        }
    }

    return "" unless (scalar @badmailfrom);

#    return join "\n", sort(@badmailfrom);
    return sort(@badmailfrom);
}

sub get_whitelisthosts
{
    my %list = $wdb->get('whitelisthosts')->props;

    my @whitelisthosts = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "White") {
            push @whitelisthosts, $parameter;
        }
    }

    return "" unless (scalar @whitelisthosts);

#    return join "\n", sort(@whitelisthosts);
    return sort(@whitelisthosts);
    
}

sub get_whitelisthelo
{
    my %list = $wdb->get('whitelisthelo')->props;

    my @whitelisthelo = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "White") {
            push @whitelisthelo, $parameter;
        }
    }

    return "" unless (scalar @whitelisthelo);

#    return join "\n", sort(@whitelisthelo);
    return sort(@whitelisthelo);
}

sub get_whitelistsenders
{
    my %list = $wdb->get('whitelistsenders')->props;

    my @whitelistsenders = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "White") {
            push @whitelistsenders, $parameter;
        }
    }

    return "" unless (scalar @whitelistsenders);

    #return join "\n", sort(@whitelistsenders);
    return sort(@whitelistsenders);
}

sub get_whitelistfrom
{
    my %list = $sdb->get('wbl.global')->props;

    my @whitelistfrom = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "White") {
            push @whitelistfrom, $parameter;
        }
    }

    return "" unless (scalar @whitelistfrom);

#    return join "\n", sort(@whitelistfrom);
    return sort(@whitelistfrom);
}

sub create_modify_black
{
    my $fm = shift;
    my $q = $fm->{'cgi'};

    # qmail badhelo
    my %list = $wdb->get('badhelo')->props;
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "Black") {
            $wdb->get_prop_and_delete('badhelo', "$parameter");
        }
    }

    my $BadHelo = $q->param("badhelo");
    $BadHelo =~ s/\r\n/,/g;
    my @BadHelo = sort(split /,/, $BadHelo);
    foreach $BadHelo (@BadHelo)
	{
	$wdb->set_prop('badhelo', "$BadHelo", 'Black');
	}

    # qmail badmailfrom
    my %list_badmailfrom = $wdb->get('badmailfrom')->props;
    my $parameter_badmailfrom = "";
    my $value_badmailfrom = "";
    while (($parameter_badmailfrom,$value_badmailfrom) = each(%list_badmailfrom)) {
        if ($parameter_badmailfrom eq "type") {next;}

        if ($value_badmailfrom eq "Black") {
            $wdb->get_prop_and_delete('badmailfrom', "$parameter_badmailfrom");
        }
    }

    my $BadMailFrom = $q->param("badmailfrom");
    $BadMailFrom =~ s/\r\n/,/g;
    my @BadMailFrom = sort(split /,/, $BadMailFrom);
    foreach $BadMailFrom (@BadMailFrom){
        $wdb->set_prop('badmailfrom', "$BadMailFrom", 'Black');
    }
    # spamassassin blacklist_from
    my %list_wblglobal = $sdb->get('wbl.global')->props;
    my $parameter_wblglobal = "";
    my $value_wblglobal = "";
    while (($parameter_wblglobal,$value_wblglobal) = each(%list_wblglobal)) {
        if ($parameter_wblglobal eq "type") {next;}

        if ($value_wblglobal eq "Black") {
            $sdb->get_prop_and_delete('wbl.global', "$parameter_wblglobal");
        }
    }

    my $BlacklistFrom = $q->param("blacklistfrom");
    $BlacklistFrom =~ s/\r\n/,/g;
    my @BlacklistFrom = sort(split /,/, $BlacklistFrom);
    foreach $BlacklistFrom (@BlacklistFrom){
        $sdb->set_prop('wbl.global', "$BlacklistFrom", 'Black');
    }

    ##Update email settings
    unless ( system ("/sbin/e-smith/signal-event", "smeserver-wbl-update") == 0 ){
        $fm->error('ERROR_UPDATING');
        return undef;
    }

    $fm->success('SUCCESS');
}

sub create_modify_white
{
    my $fm = shift;
    my $q = $fm->{'cgi'};

    # qpsmtpd whitelisthosts
    my %list = $wdb->get('whitelisthosts')->props;
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "White") {
            $wdb->get_prop_and_delete('whitelisthosts', "$parameter");
        }
    }

    my $WhitelistHosts = $q->param("whitelisthosts");
    $WhitelistHosts =~ s/\r\n/,/g;
    my @WhitelistHosts = sort(split /,/, $WhitelistHosts);
    foreach $WhitelistHosts (@WhitelistHosts)
	{
	$wdb->set_prop('whitelisthosts', "$WhitelistHosts", 'White');
	}

    # qpsmtpd whitelisthelo
    my %list_whitelisthelo = $wdb->get('whitelisthelo')->props;
    my $parameter_whitelisthelo = "";
    my $value_whitelisthelo = "";
    while (($parameter_whitelisthelo,$value_whitelisthelo) = each(%list_whitelisthelo)) {
        if ($parameter_whitelisthelo eq "type") {next;}

        if ($value_whitelisthelo eq "White") {
            $wdb->get_prop_and_delete('whitelisthelo', "$parameter_whitelisthelo");
        }
    }

    my $WhitelistHelo = $q->param("whitelisthelo");
    $WhitelistHelo =~ s/\r\n/,/g;
    my @WhitelistHelo = sort(split /,/, $WhitelistHelo);
    foreach $WhitelistHelo (@WhitelistHelo)
	{
	$wdb->set_prop('whitelisthelo', "$WhitelistHelo", 'White');
	}

    # qpsmtpd whitelistsenders
    my %list_whitelistsenders = $wdb->get('whitelistsenders')->props;
    my $parameter_whitelistsenders = "";
    my $value_whitelistsenders = "";
    while (($parameter_whitelistsenders,$value_whitelistsenders) = each(%list_whitelistsenders)) {
        if ($parameter_whitelistsenders eq "type") {next;}

        if ($value_whitelistsenders eq "White") {
            $wdb->get_prop_and_delete('whitelistsenders', "$parameter_whitelistsenders");
        }
    }

    my $WhitelistSenders = $q->param("whitelistsenders");
    $WhitelistSenders =~ s/\r\n/,/g;
    my @WhitelistSenders = sort(split /,/, $WhitelistSenders);
    foreach $WhitelistSenders (@WhitelistSenders)
	{
	$wdb->set_prop('whitelistsenders', "$WhitelistSenders", 'White');
	}

    # spamassassin whitelist_from
    my %list_wblglobal = $sdb->get('wbl.global')->props;
    my $parameter_wblglobal = "";
    my $value_wblglobal = "";
    while (($parameter_wblglobal,$value_wblglobal) = each(%list_wblglobal)) {
        if ($parameter_wblglobal eq "type") {next;}

        if ($value_wblglobal eq "White") {
            $sdb->get_prop_and_delete('wbl.global', "$parameter_wblglobal");
        }
    }

    my $WhitelistFrom = $q->param("whitelistfrom");
    $WhitelistFrom =~ s/\r\n/,/g;
    my @WhitelistFrom = sort(split /,/, $WhitelistFrom);
    foreach $WhitelistFrom (@WhitelistFrom){
        $sdb->set_prop('wbl.global', "$WhitelistFrom", 'White');
    }

    ##Update email settings
    unless ( system ("/sbin/e-smith/signal-event", "smeserver-wbl-update") == 0 ){
        $fm->error('ERROR_UPDATING');
        return undef;
    }

    $fm->success('SUCCESS');
}

sub email_update
{
    my $fm = shift;
    my $q = $fm->{'cgi'};

    unless ( system ("/sbin/e-smith/signal-event", "smeserver-wbl-update") == 0 )
    {
        $fm->error('ERROR_UPDATING');
        return undef;
    }

    $fm->success('SUCCESS');

}

sub get_blacklistfrom
{
    my %list = $sdb->get('wbl.global')->props;

    my @blacklistfrom = ();
    my $parameter = "";
    my $value = "";
    while (($parameter,$value) = each(%list)) {
        if ($parameter eq "type") {next;}

        if ($value eq "Black") {
            push @blacklistfrom, $parameter;
        }
    }

    return "" unless (scalar @blacklistfrom);

    return join "\n", sort(@blacklistfrom);
}
sub create_modify_rbl
{
    my $fm = shift;
    my $q = $fm->{'cgi'};

    my $dnsbl = $q->param('dnsbl');
    $db->set_prop('qpsmtpd', 'DNSBL', "$dnsbl");

    my $rhsbl = $q->param('rhsbl');
    $db->set_prop('qpsmtpd', 'RHSBL', "$rhsbl");


    my $sbllistcgi = $q->param('sbllist');
    my @sbllistcgi = split /\s{2,}/, $sbllistcgi;
    my $sbllistdb = '';
    foreach (@sbllistcgi) { $sbllistdb = $sbllistdb . ',' . $_; }
    $sbllistdb =~ s/^,//;

    $db->set_prop('qpsmtpd', 'SBLList', "$sbllistdb");
    

    my $rbllistcgi = $q->param('rbllist');
    my @rbllistcgi = split /\s{2,}/, $rbllistcgi;
    my $rbllistdb = '';
    foreach (@rbllistcgi) { $rbllistdb = $rbllistdb . ',' . $_; }
    $rbllistdb =~ s/^,//;

    $db->set_prop('qpsmtpd', 'RBLList', "$rbllistdb");

    ##Update email settings

    unless ( system ("/sbin/e-smith/signal-event", "smeserver-wbl-update") == 0 ){
        $fm->error('ERROR_UPDATING');
        return undef;
    }

    $fm->success('SUCCESS');
}

#Subroutine to display buttons
#sub print_custom_button{
#    my ($fm,$desc,$url) = @_;
#    my $q = $fm->{cgi};
#    $url="wbl?page=0&page_stack=&Next=Next&wherenext=".$url;
#    print "  <tr>\n    <td colspan='2'>\n";
#    print $q->p($q->a({href => $url, -class => "button-like"},$fm->localise($desc)));
#    print qq(</tr>\n);
#    return undef;
#}
#;
