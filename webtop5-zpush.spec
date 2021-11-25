%define wtrelease 5.14.2

Summary: WebTop z-push
Name: webtop5-zpush
Version: 1.2.2
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: https://github.com/sonicle-webtop/webtop-eas-server/archive/wt-%{wtrelease}.tar.gz
Source1: webtop5-zpush.conf
Source2: config.json
Source3: webtop-zpush
BuildArch: noarch

Requires: webtop5-core
Requires: rh-php72-php-fpm, rh-php72-php-mbstring, rh-php72-php-imap, rh-php72-php-pdo
Conflicts: webtop4-zpush

%description
NethServer z-push for WebTop 5

%build
mkdir -p root/var/log/z-push/state
mkdir -p root/usr/share/webtop/z-push/
mkdir -p root/etc/httpd/conf.d/
mkdir -p root/etc/logrotate.d/
tar xvzf %{SOURCE0} --exclude='.gitignore' -C root/usr/share/webtop/z-push --strip-components=2 webtop-eas-server-wt-%{wtrelease}/src
cp %{SOURCE1} root/etc/httpd/conf.d/
cp %{SOURCE2} root/usr/share/webtop/z-push/
cp %{SOURCE3} root/etc/logrotate.d/
echo %{wtrelease} > VERSION

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
%attr(755, apache, apache) /var/log/z-push
%attr(755, apache, apache) /var/log/z-push/state
%attr(755, root, root) /usr/share/webtop/z-push/z-push-admin.php
%config /etc/httpd/conf.d/webtop5-zpush.conf
%config /usr/share/webtop/z-push/config.json
/usr/share/webtop/z-push/*
/usr/share/webtop/z-push/.htaccess
/usr/share/webtop/z-push/.user.ini
/etc/logrotate.d/webtop-zpush
%doc VERSION


%changelog
* Thu Nov 25 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- WebTop 5.14.2 - NethServer/dev#6604

* Wed Mar 04 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.1-1
- WebTop 5.8.1 - NethServer/dev#6060

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- WebTop: new ActiveSync implementation - NethServer/dev#5732

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
