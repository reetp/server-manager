# $Id: smeserver-manager.spec,v 1.3 2018/02/04 18:11:07 jpp Exp $

Summary: smeserver manager 2 navigation module
%define name smeserver-manager
Name: %{name}
%define version 0.1.0
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.xz
Patch0: smeserver-manager-0.1.0-bz10506.patch
Patch1: smeserver-manager-add-basic-files.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildRequires: gettext
BuildRequires: gcc
Requires: e-smith-lib >= 1.18.0-26
Requires: e-smith-manager >= 2.4.0-22
Requires: perl-Mojolicious >= 6.44
Requires: pwauth
Requires: perl(Apache::AuthTkt
Requires: smeserver-manager-html
Provides: server-manager2
AutoReqProv: no

%changelog
* Tue Feb 06 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1.0-2.sme
- Start adding some template files

* Sun Feb 04 2018 Jean-Philipe Pialasse <tests@pialasse.com> 0.1.0-1.sme
- first smeserver-manager package [SME: 10506]
  this is a sandbox to dev the next server-manager based on mojolicious
  this package is based on part of the old e-smith-manager and needs it 
  to work until we moved the httpd-admin part.

* Sun Apr 16 2017 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-26.sme
- add a panel to ease reporting bugs [SME: 8783]
- Original work from Mats Schuh m.schuh@neckargeo.net

* Wed Apr 05 2017 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-20.sme
- fix warning uninitialized value in lc [SME: 10209]

* Mon Mar 27 2017 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-19.sme
- fix typo in  e-smith-manager-2.8.0-bz10167-emptyback.patch

* Sat Mar 25 2017 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-18.sme
- avoid internal server error if empty back parameter [SME: 10167]
- return user friendly message

* Sat Mar 25 2017 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-17.sme
- fix too short timeout in server-manager [SME: 9921]
- now 30 min as default instead of 5
- possibility to change this and adapt the default 0.66 of timeout remaining to reset it
- by default only a session cookie, can activate persistent cookie
- sha256 as encryption.

* Mon Jan 16 2017 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-15.sme
- fix bad redirection parameter that might reveal session information to remote site [SME: 9924]

* Tue Jul 19 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-13.sme
- added missing template-begin for tkt.css [SME: 9676]

* Tue Jul 19 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-12.sme
- Update server-manager to Koozali branding [SME: 9676]
- We thanks John Crisp for his wonderful work. 

* Wed Jun 15 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-11.sme
- change link for donation to koozali.org  [SME: 9599]

* Wed Jun 15 2016 Daniel Berteaud <daniel@firewall-services.com> 2.8.0-10.sme
- Fix syntax for removing Indexes options [SME: 9587]

* Wed Jun 15 2016 Daniel Berteaud <daniel@firewall-services.com> 2.8.0-9.sme
- Remove index option for manager's resources [SME: 9587]

* Mon Jun 13 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-8.sme
- fix 307 redirection to http when https is used [SME: 8825] [SME: 9583]
- update syntaxe for TKT Auth
- bump 8 for typo

* Wed Jun 1 2016 Daniel Berteaud <daniel@firewall-services.com> 2.8.0-6.sme
- Fix a syntax error in server-manager's logout script [SME: 9527]

* Wed May 11 2016 Daniel Berteaud <daniel@firewall-services.com> 2.8.0-5.sme
- Add a C wrapper to execute manager's cgi to replace perl-suid [SME: 9393]

* Wed Mar 23 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-4.sme
- fix syntax for httpd 2.4 [SME: 9365]

* Fri Mar 18 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.8.0-3.sme
- rebuild for Bug [SME: 9347]
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Wed Mar 14 2000 --> Wed Mar 08 2000 or Tue Mar 14 2000 or Wed Mar 15 2000 or ....
  Wed Apr 04 2002 --> Wed Apr 03 2002 or Thu Apr 04 2002 or Wed Apr 10 2002 or ....
  Tue May 15 2008 --> Tue May 13 2008 or Thu May 15 2008 or Tue May 20 2008 or ....

* Fri Mar 18 2016 Daniel Berteaud <daniel@firewall-services.com> 2.8.0-2.sme
- Don't require perl-suidperl anymore [SME: 9339]

* Fri Feb 05 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 2.8.0-1.sme
- Initial release to sme10

* Fri Feb 5 2016 Daniel Berteaud <daniel@firewall-services.com> 2.6.0-4.sme
- Really don't redirect to http when login in/out of the server-manager
  [SME: 9163]

* Sun Jan 31 2016 Daniel Berteaud <daniel@firewall-services.com> 2.6.0-3.sme
- Don't redirect to http when login in/out of the server-manager from
  localhost [SME: 9163]

* Tue Jan 6 2015 Daniel Berteaud <daniel@firewall-services.com> 2.6.0-2.sme
- Allow access to the server-manager without SSL from the loopback
  [SME: 9163]

* Sun Mar 23 2014 Ian Wells <esmith@wellsi.com> 2.6.0-1.sme
- Roll new stream to remove obsolete images [SME: 7962] 

* Sun Mar 23 2014 Ian Wells <esmith@wellsi.com> 2.4.0-9.sme
- Remove references to obsolete images, by Stephane de Labrusse [SME: 7962]

* Fri Oct 11 2013 Ian Wells <esmith@wellsi.com> 2.4.0-8.sme
- Renew donation text in server-manager, by John Crisp [SME: 7897]

* Thu Jun 6 2013 Daniel Berteaud <daniel@firewall-services.com> 2.4.0-7.sme
- Do not load mod_ssl [SME: 7602]

* Wed Mar 6 2013 Shad L. Lords <slords@mail.com> 2.4.0-6.sme
- Correct path to pwauth [SME: 7319]

* Sat Feb 23 2013 Ian Wells <esmith@wellsi.com> 2.4.0-5.sme
- Correct processing of server-manager URL [SME: 7254]

* Thu Jan 31 2013 Shad L. Lords <slords@mail.com> 2.4.0-4.sme
- Fix typo in perl(Apache::AuthTkt) requires [SME: 7236]

* Thu Jan 31 2013 Shad L. Lords <slords@mail.com> 2.4.0-3.sme
- Add perl-suidperl dependency [SME: 7235]

* Thu Jan 31 2013 Shad L. Lords <slords@mail.com> 2.4.0-2.sme
- Add perl(Apache::AuthTkt) dependency [SME: 7236]

* Thu Jan 31 2013 Shad L. Lords <slords@mail.com> 2.4.0-1.sme
- Roll new stream for sme9

* Sat Aug 7 2010 Ian Wells <esmith@wellsi.com> 2.2.0-6.sme
- Remove empty <p> tag from /etc/e-smith/web/common/foot.tmpl, by Daniel [SME: 5905]

* Sun Jan 31 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-5.sme
- Only display error messages intended for admin in server-manager [SME: 5700]

* Wed Dec  9 2009 Charlie Brady <charlieb@budge.apana.org.au> 2.2.0-4.sme
- Fix css validation errors. [SME: 5656]

* Fri Sep 18 2009 Stephen Noble <support@dungog.net> 2.2.0-4.sme 
- display reconfigure warning once if UnsavedChanges=yes [SME: 5475]

* Fri Sep 18 2009 Stephen Noble <support@dungog.net> 2.2.0-3.sme 
- display reconfigure warning if UnsavedChanges=yes [SME: 5475]

* Sun Apr 26 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-2.sme
- Fix misinterpretation of display string [SME: 5022]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sat Oct 4 2008 Shad L. Lords <slords@mail.com> 1.14.0-20
- Make navigation use new db class for navigation [SME: 4619]

* Thu Jul 31 2008 Shad L. Lords <slords@mail.com> 1.14.0-19
- Make binmode properties of db class [SME: 4317]
- Add new navigation db & utf8 classes [SME: 4317]

* Tue Jul 1 2008 Shad L. Lords <slords@mail.com> 1.14.0-18
- Fix open of database to create if necessary [SME: 4147]

* Thu May 15 2008 Shad L. Lords <slords@mail.com> 1.14.0-17
  Tue May 15 2008 --> Tue May 13 2008 or Thu May 15 2008 or Tue May 20 2008 or ....
- No longer remove navigation dbs. [SME: 4147]
- Deal a little more gracefully with non UTF-8 lexicons [SME: 4229]

* Mon Mar 31 2008 Shad L. Lords <slords@mail.com> 1.14.0-16
- Remove navigation dbs and create new [SME: 4147]

* Fri Mar 28 2008 Shad L. Lords <slords@mail.com> 1.14.0-15
- Remove last remnant of pleasewait [SME: 4130]

* Wed Mar 26 2008 Shad L. Lords <slords@mail.com> 1.14.0-14
- Include general lexicons in nav-config [SME: 4113]

* Tue Mar 25 2008 Shad L. Lords <slords@mail.com> 1.14.0-13
- Fix wide output to print in navigation and allow navigations db to
  be utf8 [SME: 4101]

* Sat Mar 22 2008 Shad L. Lords <slords@mail.com> 1.14.0-12
- Fix UTF-8 encoding in header and nav-conf [SME: 4072]

* Tue Jan 08 2008 Stephen Noble <support@dungog.net> 1.14.0-11
- Fix to remove spaces and newlines in panel headers [SME: 3346] 

* Tue Jan 08 2008 Stephen Noble <support@dungog.net> 1.14.0-10
- remove the FormMagick session files [SME: 3723]

* Tue Jan 08 2008 Stephen Noble <support@dungog.net> 1.14.0-9
- Remove spaces and newlines in panel headers [SME: 3346] 

* Sun Jul 01 2007 Shad L. Lords <slords@mail.com> 1.14.0-8
- Make login/logout no quite so verbose. [SME: 2660]

* Fri May 18 2007 Shad L. Lords <slords@mail.com> 1.14.0-7
- Use correct lib for modules

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Mon Apr 9 2007 Stephen Noble <support@dungog.net> 1.14.0-6
- Convert http to https [SME: 2577]

* Mon Mar 12 2007 Gavin Weight <gweight@gmail.com> 1.14.0-5
- Restyle the SME Server manager login form. [SME: 2666]

* Mon Mar 05 2007 Shad L. Lords <slords@mail.com> 1.14.0-4
- Don't pass domain in ticket cookie (logout) unless it contains a dot [SME: 2402]

* Mon Mar 05 2007 Shad L. Lords <slords@mail.com> 1.14.0-3
- Don't pass domain in ticket cookie (login) unless it contains a dot [SME: 2402]

* Tue Feb 13 2007 Charlie Brady <charlie_brady@mitel.com> 1.14.0-2
- Deal gracefully with renamed apache modules. [SME: 2471]

* Fri Jan 26 2007 Shad L. Lords <slords@mail.com> 1.14.0-1
- Roll stable stream. [SME: 2328]

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 1.13.1-13
- Create /etc/httpd/admin-conf directory

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 1.13.1-12
- Move apache logrotate to e-smith-apache.
- Put quotes around 'httpd-admin' in hashes.

* Thu Jan 18 2007 Shad L. Lords <slords@mail.com> 1.13.1-11
- Move last httpd fragments from e-smith-base.

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Mon Nov 27 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-09
- Randomize string used for encrypting auth tickets.

* Tue Nov 21 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-08
- Add ProxyPassReverse entries for server-manager passthroughs, so that
  redirects work correctly.

* Thu Nov 16 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-07
- Add basic L10N in navigation-conf.

* Wed Nov 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-06
- Avoid use of FormMagick in navigation-conf. TODO: fix I18N.

* Mon Nov 06 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-05
- Simplify the sorting code in navigation (so that I can understand
  it).

* Mon Nov 06 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-04
- Simplify javascript, and remove use of pleasewait script.

* Mon Nov 06 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-03
- Move swapClass javascript out of standard header and into just
  navigation.

* Fri Nov 03 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-02
- Use mod_auth_tkt authentication for server manager access.

* Thu Nov 02 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.1-01
- Add branch tag and roll new development version.

* Wed Nov 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.0-06
- Move httpd-admin and its configuration templates from e-smith-base RPM.
  [SME: 2023]

* Wed Nov 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.0-05
- Move more server-manager components from e-smith-base RPM. [SME: 2023]

* Wed Nov 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.13.0-04
- Add manager header/footer templates (moved from e-smith-base)
  [SME: 2023]

* Wed Aug 2 2006 Michael Soulier <msoulier@digitaltorque.ca>
- [1.13.0-03]
- Fixing broken db path in patch. [SME: 107]

* Wed Mar 29 2006 Michael Soulier <michael_soulier@mitel.com>
- [1.13.0-02]
- Forward porting arbitrary menu plugins. [SME: 107]

* Wed Mar 29 2006 Michael Soulier <michael_soulier@mitel.com>
- [1.13.0-01]
- Rolling to dev.
  [SME: 107]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Tue Jan 31 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-13
- Changed the static CSS files into directory templates, which are
  expanded in bootstrap-console-save [SME: 408]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-12
- Bump release number only

* Sun Oct 16 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-11]
- Removed "table-layout: fixed;" from sme_main.css [SF: 1299779]

* Sun Oct 16 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-10]
- dos2unix conversion on CSS files [SF: 1299779]

* Wed Aug 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-09]
- Remove bogus "Provides: perl(I18N::AcceptLanguage)" header. [SF: 1262438]

* Thu Jun  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-08]
- Add newly required manager/cgi-bin/{navigation,noframes} symlinks.
  [SF: 1217426]

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-07]
- Remove references to /etc/e-smith/web/panel/manager/common
  [SF: 1172203, 1210715]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-06]
- Updated perl dependencies. [msoulier MN00040240]

* Tue Jul 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-05]
- Added the sme_panel_menu.css file, for tabbed menu support. Added a link to
  it in the standard header.
  [msoulier MN00030141]

* Thu Feb 26 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-04]
- Backed-out previous change. It was better before. [msoulier dpar-22042]

* Thu Feb 26 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-03]
- Added vertical-align: text-top; to td.sme-noborders-label to ensure that
  text is aligned vertically at the top of the cell. [msoulier dpar-22042]

* Tue Jul  8 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Check that files are executable before listing in the
  manager navigation frame. [charlieb 9197]
- s/Copyright/License/.

* Tue Jul  8 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Changing version to development stream number - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-16]
- New class for error link within table cell [gordonr 8129]

* Tue Apr  8 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-15]
- Removed borders around "warning" cells so they don't look like
  they are bleeding on some browsers (e.g. Mozilla) [gordonr 8127]

* Thu Apr  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-14]
- Make <h2> and <p> within div.{success,error} => {red,green} [gordonr 7919]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-13]
- Moved manager SSL fragments back to e-smith-base [gordonr 7900]

* Tue Apr  1 2003 Tony Clayton <apc@e-smith.com>
- [1.9.5-12]
- add td.sme-radiobutton css class for date/time panel [tonyc 1588]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-11]
- Make the question make bold [gordonr 7946]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-10]
- Fix SSL listen template for serveronly mode [gordonr 7900]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-09]
- Bind manager on port 981 to localhost only [gordonr 7900]

* Mon Mar 31 2003 Mike Dickson <miked@e-smith.com>
- [1.9.5-08]
- changed class for sme-noborders-label to width=33% rather than
  a fixed 250px wide, due to limitations in IE6 [miked 7676]
- added class "sectionbar" for use [miked]
- modified "td.noborders-label" colour [miked]


* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-07]
- Changed Copyright font from 8px to 10px [gordonr 7676]

* Thu Mar 27 2003 Mark Knox <markk@e-smith.com>
- [1.9.5-06]
- Changed Help -> ? and changed formatting of current user and host [markk
  7707]

* Thu Mar 20 2003 Tony Clayton <apc@e-smith.com>
- [1.9.5-05]
- Add css style for a.error class [tonyc 4718]

* Wed Mar 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.5-04]
- Move navigation dbs to /home/e-smith/db/navigation. We shouldn't generate
  them in /etc/e-smith/locale and we should name them by language, in case
  we share lexicons (e.g. fr/fr-ca) [gordonr 7733]

* Sun Mar 16 2003 Mike Dickson <miked@e-smith.com>
- [1.9.5-03]
- stylesheet fixes: darkend the copyrigt text, adjuste the UL and LI tags [miked 7676]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [1.9.5-02]
- Removed 40LogoRow from header.htm templates [markk 4722]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [1.9.5-01]
- Removed product_logo.gif [markk 4722]

* Tue Mar 11 2003 Mike Dickson <miked@e-smith.com>
- [1.9.4-09]
- changed Adming to admin in header.htm templates [miked 7595]

* Thu Feb  6 2003 Mike Dickson <miked@e-smith.com>
- [1.9.4-08]
- updated the CSS to add a new "success" class [miked 7032]

* Tue Feb  4 2003 Mark Knox <markk@e-smith.com>
- [1.9.4-07]
- Refer to new SSL cert name of $SystemName.$DomainName [markk 4874]

* Mon Feb  3 2003 Mark Knox <markk@e-smith.com>
- [1.9.4-06]
- Include ValidFrom hosts in SSL allow statements [markk 6428]

* Mon Feb  3 2003 Mark Knox <markk@e-smith.com>
- [1.9.4-05]
- Also Listen on the right ports [markk 6428]

* Mon Feb  3 2003 Mark Knox <markk@e-smith.com>
- [1.9.4-04]
- Bind SSL to port 443 if no primary web server available [markk 6428]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [1.9.4-03]
- darkened colour of copyright text [miked 6696]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [1.9.4-02]
- removed demo class "warn" from nav script [miked 6706]

* Mon Jan 13 2003 Mike Dickson <miked@e-smith.com>
- [1.9.4-01]
- updated CSS file to show correct colour in menu, added "warn.gif" [miked 6398]

* Fri Jan  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-13]
- Made use of esmith::I18N in navigation-conf. Renamed locale->lang
  to make it more obvious that we are dealing with a langtag [gordonr 5212]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-12]
- Hide online-manual from navigation bar - now in header Help [gordonr 6394]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-11]
- Updated navigation script to use esmith::I18N [gordonr 5212]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-10]
- Spell bootstrap-console-save correctly [gordonr 5493]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-09]
- Work out the correct navigation.info based on browser language [gordonr 5493]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-08]
- Generate navigation.info files (config db format) for each supported 
  language in /etc/e-smith/locale/{language}/etc/e-smith/web/functions
- Read the navigation.info file for the preferred language when 
  displaying the navigation bar 
- TODO: Actually select the correct navigation.info file [gordonr 5493]

* Tue Dec 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.3-07]
- Skip non-executable files when generating nav bar [gordonr 5802]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.9.3-06]
- updates and comments in the CSS files [miked 3185]
- commented out the two links in the header that are not ready yet
  (log out and update available) [miked 5967 and 492]

* Mon Dec 16 2002 Mike Dickson <miked@e-smith.com>
- [1.9.3-05]
- UI Update, part of the tweaking for the new UI [miked 5494]

* Tue Dec 10 2002 Mike Dickson <miked@e-smith.com>
- [1.9.3-04]
- forgot to update header.htm fragments [miked 5494]

* Mon Dec  9 2002 Mike Dickson <miked@e-smith.com>
- [1.9.3-03]
- ui update [miked 5494]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [1.9.3-02]
- ui update  [miked 5494]

* Wed Nov 27 2002 Mike Dickson <miked@e-smith.com>
- [1.9.3-01]
- and again to make it stick

* Wed Nov 27 2002 Mike Dickson <miked@e-smith.com>
- [1.9.2-01]
- updated the header images [miked 5529]
- updated other UI stuff [miked 5494]

* Fri Nov 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.1-02]
- templated header.htm [miked 5826]
- modified header.htm template to link to online-manual and blades 
  [gordonr 5826]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.9.1-01]
- update to new UI system [miked 5494]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-01]
- Changing to development stream; version upped to 1.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Wed Jun 19 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-01]
- Move SSL mutex and cache out of /var/log [markk 3830]

* Tue Jun 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Move admin apache SSL mutex and SSL session cache to files named admin_xxx
  to avoid name clash with main server. [charlieb 3830]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to maintained stream number to 1.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.11-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May 16 2002 Tony Clayton <apc@e-smith.com>
- [1.5.10-01]
- Pass noframes=1 as cgi param for browsers without frames [tonyc 3475]

* Thu May 16 2002 Tony Clayton <apc@e-smith.com>
- [1.5.9-01]
- use Dan McGarry's manager.css/navigation fixes for 3377 [tonyc]

* Thu May 16 2002 Tony Clayton <apc@e-smith.com>
- [1.5.8-01]
- Remove unnecessary <p> tags in navigation html [tonyc 3377]
- Fix navigation panel to not import symbols from fm subclasses 
  [tonyc 3109]

* Mon May 13 2002 Tony Clayton <apc@e-smith.com>
- [1.5.7-01]
- Fix navigation panel to play nice with FM subclasses [tonyc 3109]

* Fri May 10 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.6-01]
- Tell CGI.pm to not produce xhtml [gordonr 3377]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.5-01]
- Missing use esmith::util [gordonr 3372]

* Wed Apr 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.4-01]
- Ignore cgi-bin/internal-.* in navigation [gordonr 3202]

* Mon Apr 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.3-01]
- Back out gettext() calls - esmith::FormMagic was Croaking on
  bad lexicons for old panels. Now properly localises the navigation
  bar if the localisations exist [gordonr 3155]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.2-01]
- Added explicit gettext() call to localize navigation bar while
  figuring out esmith::FormMagick won't do it for me [gordonr 3155]

* Wed Apr 10 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.1-01]
- navigation is now polymorphic and does noframes as well [gordonr #3155]

* Thu Apr 04 2002 Gordon Rowell <gordonr@e-smith.com>
  Wed Apr 04 2002 --> Wed Apr 03 2002 or Thu Apr 04 2002 or Wed Apr 10 2002 or ....
- [1.5.0-01]
- Rolled to development stream [gordonr]

* Wed Apr 03 2002 Kirrily Robert <skud@e-smith.com>
- [1.4.4-01]
- Added red error messages to CSS [skud 3027]

* Thu Mar 14 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.4.3-01]
- Fixed regexp for ignoring pleasewait(-.*?). Two each in 
  pleasewait/noframes. Reduced to one in each [gordonr]

* Fri Mar 1 2002 Tony Clayton <tonyc@e-smith.com>
- [1.4.2-01]
- rollRPM: Rolled version number to 1.4.2-01. Includes patches up to 1.4.1-02.
- mkdir panels/manager/common in spec file for CVS migration

* Fri Jan 25 2002 Tony Clayton <tonyc@e-smith.com>
- [1.4.1-02]
- added missing ')' in navigation script pleasewait munging

* Fri Jan 25 2002 Tony Clayton <tonyc@e-smith.com>
- [1.4.1-01]
- rollRPM: Rolled version number to 1.4.1-01. Includes patches up to 1.4.0-02.
- navigation now ignores pleasewait-* files

* Thu Jan 10 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-02]
- Use dated log file for ssl_engine_log. Name the file ssl_engine_log.xxxxx
  to keep it distinct from the main web server's log file.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.4.0-01]
- rollRPM: Rolled version number to 1.4.0-01. Includes patches up to 1.3.0-07.

* Sat Dec 08 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-07]
- Move genNavigationHeader() down below the script grokking code in
  "navigation", to help Netscape's faulty rendering.

* Wed Nov 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-06]
- Remove troublesome "Requires: e-smith-base". 
- Remove obsolete "Requires: e-smith".

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-05]
- Indent description within navigation headings sections

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-04]
- Backed out patch from 1.3.0-02 - restored image to navigation frame

* Wed Oct 31 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-03]
- Add Mitel branding changes.

* Fri Aug 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-02]
- Removed image from top of navigation - now in separate frame
- Added Provides: server-manager

* Fri Aug 31 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-02.

* Fri Aug 17 2001 gordonr
- [1.2.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-04.

* Tue Jul 31 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-04]
- moving manager.css file from manager/html to common/css

* Tue Jul 31 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-03]
- Adding SSL enabling templates for port 981.
- Adding 01localAccessString fragment for use in SSL 
  enabling templates.

* Fri Jul 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-02]
- Prepend "/server-manager" to hrefs, to allow consistent path interpretation
  between admin and standard web server.

* Fri Jul 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-01]
- Rolled version number to 1.1.0-01. Includes patches upto 0.1.1-06.

* Tue Jul 24 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-06]
- Incorporating font size changes to manager.css

* Mon Jul 9 2001 Peter Samuel <peters@e-smith.com>
- [0.1.1-05]
- Updated packager information

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [0.1.1-04]
- Changed license to GPL

* Wed Jun 06 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1.1-03]
- Change font setting in navigation - use css class instead.
- Add newlines after each link in navigation frame - so that HTML
  source is readable.
- Add manager.css, which came from e-smith-base. Let's have all look&feel
  in the one RPM.
- Check whether "files" in cgi-bin directory are actually directories. Skip
  any directories.

* Mon Apr  9 2001 Adrian Chung <adrianc@e-smith.com>
- [0.1.1-02]
- changing CELLPADDING in navigation from 4 to 2.

* Tue Mar 14 2000 Charlie Brady <charlieb@e-smith.com>
  Wed Mar 14 2000 --> Wed Mar 08 2000 or Tue Mar 14 2000 or Wed Mar 15 2000 or ....
- initial release

%description
This RPM contributes the navigation bars for the smeserver-manager.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
perl createlinks
#gcc -o root/etc/e-smith/web/functions/wrapper manager.c
#mkdir -p root/home/e-smith/db/navigation
#mkdir -p root/etc/e-smith/web/common/css

#mkdir -p root/usr/share/locale/en_US/LC_MESSAGES/
#xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/foot.tmpl.po root/etc/e-smith/templates/etc/e-smith/web/common/foot.tmpl/25Copyright
## make header/footer symlinks
#ln -s head.tmpl root/etc/e-smith/web/common/userpassword_head.tmpl
#ln -s head.tmpl root/etc/e-smith/web/common/noframes_head.tmpl
#ln -s foot.tmpl root/etc/e-smith/web/common/noframes_foot.tmpl

#mkdir -p  root/etc/e-smith/web/panels/manager/html
#for file in index initial
#do
#    ln -s ../../../functions/wrapper root/etc/e-smith/web/panels/manager/html/${file}.cgi
#done

# Force creation of potentially empty directories
#mkdir -p root/etc/e-smith/web/{common,functions}
#mkdir -p root/etc/e-smith/web/panels/manager/{cgi-bin,html}
#mkdir -p root/etc/e-smith/web/panels/password/{cgi-bin,html}
#mkdir -p root/etc/httpd/admin-conf
mkdir -p root/etc/e-smith/web/panels/manager2/{cgi-bin,html}

#mkdir -p root/service
#mkdir -p root/etc/rc.d/init.d/supervise
#for service in httpd-admin
#do
#  ln -s /var/service/$service root/service/$service
#  mkdir -p root/var/service/$service/supervise
#  touch root/var/service/$service/down
#  if [ -d root/var/service/$service/log ]
#  then
#    mkdir -p root/var/service/$service/log/supervise
#    mkdir -p root/var/log/$service
#  fi
#  ln -s ../daemontools root/etc/rc.d/init.d/supervise/$service
#done

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
--file /etc/e-smith/web/panels/manager2/cgi-bin/wbl 'attr(4750,root,admin)' \
--dir /etc/e-smith/web/panels/manager2 'attr(0755,root,root)' \
> %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist


# Samples only
#    --file /etc/e-smith/web/common/cgi-bin/login 'attr(0755,root,root)' \
#    --file /etc/e-smith/web/common/cgi-bin/logout 'attr(0755,root,root)' \
#    --file /etc/e-smith/web/functions/wrapper 'attr(4750,root,admin)' \
#    --dir /var/service/httpd-admin 'attr(01755,root,root)' \
#    --file /var/service/httpd-admin/down 'attr(0644,root,root)' \
#    --file /var/service/httpd-admin/run 'attr(0755,root,root)' \
#    --dir /var/service/httpd-admin/log 'attr(0755,root,root)' \
#    --dir /var/service/httpd-admin/log/supervise 'attr(0700,root,root)' \
#    --dir /var/service/httpd-admin/supervise 'attr(0700,root,root)' \
#    --file /var/service/httpd-admin/log/run 'attr(0755,root,root)' \
#    --dir /var/log/httpd-admin 'attr(0750,smelog,smelog)' \
#    > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
#find /etc/e-smith/web/panels/manager/cgi-bin/ -type f | \
#    sed -n '/\/[0-9a-z]\{32\}$/p' | \
#    xargs grep -l Persisten | \
#    xargs rm -f

%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
