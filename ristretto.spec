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
