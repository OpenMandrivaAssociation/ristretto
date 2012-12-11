%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A picture viewer for the Xfce desktop environment
Name:		ristretto
Version:	0.6.3
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		http://goodies.xfce.org/projects/applications/ristretto
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	cairo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libexif-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfconf-devel
BuildRequires:	exo-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
Requires:	xfconf

%description
Ristretto is a fast and lightweight picture-viewer for the 
Xfce desktop environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install \
	--add-only-show-in="XFCE" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg


%changelog
* Thu Aug 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.3-1
+ Revision: 814988
- update to new version 0.6.3

* Tue May 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1
+ Revision: 794662
- update to new version 0.6.0

* Wed Apr 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.2-1
+ Revision: 791664
- version update 0.5.2

* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-2
+ Revision: 789487
- rebuild

* Sun Apr 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-1
+ Revision: 788581
- update to new version 0.3.6

* Sun Jan 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.3-1
+ Revision: 769551
- version update 0.3.3

* Sat Jan 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.2-1
+ Revision: 760866
- version update 0.3.2

* Mon Nov 07 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1
+ Revision: 728127
- add buildrequires on exo-devel
- update to new version 0.3.0

* Fri Oct 28 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-1
+ Revision: 707754
- update to new version 0.2.2

* Thu Oct 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1
+ Revision: 707442
- update to new version 0.2.1

* Sat Oct 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1
+ Revision: 705650
- update to new version 0.2.0

* Mon Oct 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-1
+ Revision: 704013
- update to new version 0.1.1

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.93-1
+ Revision: 644010
- update to new version 0.0.93
- replace buildrequires from libxfcegui4-devel to libxfce4ui-devel

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.91-3
+ Revision: 633050
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.91-2mdv2011.0
+ Revision: 579682
- rebuild for new xfce 4.7.0
- adjust buildrequires

* Sat Jul 31 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.91-1mdv2011.0
+ Revision: 564037
- update to new version 0.0.91
- drop patch 0

* Thu Feb 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.22-2mdv2010.1
+ Revision: 511212
- Patch0: fix crash with gif images

* Sat May 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.22-1mdv2010.0
+ Revision: 376450
- update to new version 0.0.22

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.21-2mdv2009.1
+ Revision: 349167
- rebuild whole xfce

* Sat Nov 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.21-1mdv2009.1
+ Revision: 307792
- update to new version 0.0.21
- add support for xfconf
- drop patch 0 and 1, fixed upstream

* Sat Nov 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.20-5mdv2009.1
+ Revision: 301087
- Patch1: fix memleak

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.20-4mdv2009.1
+ Revision: 294926
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.20-3mdv2009.0
+ Revision: 270024
- Patch0: fix ristretto crash on adjusting image size

* Fri Jul 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.20-2mdv2009.0
+ Revision: 238069
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 25 2008 Funda Wang <fwang@mandriva.org> 0.0.20-1mdv2009.0
+ Revision: 211112
- New version 0.0.20

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.19-1mdv2009.0
+ Revision: 205572
- new version

* Fri Apr 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.18-2mdv2009.0
+ Revision: 192579
- drop ristretto-import.sh script as it doesn't work properly, use gthumb instead

* Wed Mar 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.18-1mdv2008.1
+ Revision: 190230
- new version

* Wed Mar 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.17-2mdv2008.1
+ Revision: 187108
- add wrapper script which searches removeable media for graphic files and displays them
 this script is going to be executed when a digital camera or similiar device is connected to the usb port

* Mon Feb 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.17-1mdv2008.1
+ Revision: 170061
- new version

* Mon Jan 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.16-1mdv2008.1
+ Revision: 159155
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.15-1mdv2008.1
+ Revision: 117017
- new version

* Sun Dec 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.14-1mdv2008.1
+ Revision: 114367
- new version

* Sun Nov 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.13-1mdv2008.1
+ Revision: 111931
- new version

* Sat Nov 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.12-1mdv2008.1
+ Revision: 109479
- new version

* Wed Nov 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.11-1mdv2008.1
+ Revision: 106759
- new version

* Sun Nov 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.10-1mdv2008.1
+ Revision: 105606
- fix buildrequires
- new version
- new license policy

* Tue Oct 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.9-1mdv2008.1
+ Revision: 98775
- new version

* Thu Oct 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.7-1mdv2008.0
+ Revision: 95350
- new version

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.6-1mdv2008.0
+ Revision: 94000
- add missing buildrequires on libexif-devel
- new version

* Fri Sep 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.5-1mdv2008.0
+ Revision: 85527
- new version
- new version

* Mon Sep 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.3-1mdv2008.0
+ Revision: 78567
- new version

* Thu Aug 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-1mdv2008.0
+ Revision: 75402
- new version
- add docs

* Tue Aug 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-1mdv2008.0
+ Revision: 72305
- make it work
- Import ristretto

