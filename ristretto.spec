%define url_ver %(echo %{version} | cut -d. -f 1-2)
%define _disable_rebuild_configure 1

Summary:	A picture viewer for the Xfce desktop environment
Name:		ristretto
Version:	0.13.1
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		http://goodies.xfce.org/projects/applications/ristretto
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(exo-2)
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
Requires:	xfconf
Requires:	hicolor-icon-theme
Requires:	xfconf
Requires:	tumbler

%description
Ristretto is a fast and lightweight picture-viewer for the 
Xfce desktop environment.

%prep
%autosetup -p1

%build
#NOCONFIGURE=1 ./autogen.sh
%configure

%make_build

%install
%make_install

desktop-file-install \
	--add-only-show-in="XFCE" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README* ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.xfce.ristretto.appdata.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg

