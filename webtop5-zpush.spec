%define wtrelease 5.3.0.1

Summary: WebTop z-push
Name: webtop5-zpush
Version: 1.1.6
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: https://github.com/sonicle-webtop/z-push-webtop/archive/wt-%{wtrelease}.tar.gz
BuildArch: noarch

Requires: webtop5-core
Requires: php-process, php-pgsql, php-imap, php-ldap, php-mcrypt, php-mbstring
Conflicts: webtop4-zpush

BuildRequires: php-cli

%description
NethServer z-push for WebTop 5

%prep
#%setup

%build
mkdir -p root/var/log/z-push/state
mkdir -p root/usr/share/webtop/z-push/
tar xvzf %{SOURCE0} --exclude='.gitignore' -C root/usr/share/webtop/z-push --strip-components=2 z-push-webtop-wt-%{wtrelease}/src
rm -rf  root/usr/share/webtop/z-push/backend/{caldav,carddav,kopano,ldap,maildir,searchldap,sqlstatemachine,vcarddir}
php -r "include('root/usr/share/webtop/z-push/backend/webtop/config.php'); file_put_contents('root/usr/share/webtop/z-push/VERSION',ZPUSH_VERSION);"

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
%attr(755, apache, apache) /var/log/z-push
%attr(755, apache, apache) /var/log/z-push/state
%attr(755, root, root) /usr/share/webtop/z-push/z-push-admin.php
/usr/share/webtop/z-push/*

%changelog
* Tue Jun 25 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.1.6-1
- WebTop 5.7.1 - NethServer/dev#5770
  - Update wtrelease to 5.3.0.1

* Thu Dec 13 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.1.5-1
-  WebTop 5.5.0 - NethServer/dev#5666
  - rpm spec: Add explicit php requirements

* Wed Aug 29 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.4-1
- webtop5-zpush: Incorrect creation of calendar events and contacts. - Bug NethServer/dev#5570

* Wed Feb 21 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.1.3-1
- WebTop 5.1.7 - NethServer/dev#5423

* Wed Nov 29 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Update to wt-5.1.4 - NethServer/de#5376

* Mon Sep 04 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- Release WebTop 5.0.13 - NethServer/dev#5338

* Wed May 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- WebTop 5: enable folder sorting - NethServer/dev#5275
- Build RPM from source

* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First WebTop5 release - NethServer/dev#5225
