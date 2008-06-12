Summary:	A picture viewer for the Xfce desktop environment
Name:		ristretto
Version:	0.0.20
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphics
URL:		http://goodies.xfce.org/projects/applications/ristretto
Source0:	http://goodies.xfce.org/releases/ristretto/%{name}-%{version}.tar.gz
BuildRequires:	gtk+2-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libthunar-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libexif-devel
BuildRequires:	libxfcegui4-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Ristretto is a fast and lightweight picture-viewer for the 
Xfce desktop environment.

%prep
%setup -q

%build
%configure2_5x
		
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install \
	--add-only-show-in="XFCE" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%clean 
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%{update_mime_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_mime_database}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
