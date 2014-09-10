%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A picture viewer for the Xfce desktop environment
Name:		ristretto
Version:	0.6.3
Release:	4
License:	GPLv2+
Group:		Graphics
URL:		http://goodies.xfce.org/projects/applications/ristretto
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.11
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(exo-1)
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
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

