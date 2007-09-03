Summary:	A picture viewer for the Xfce desktop environment
Name:		ristretto
Version:	0.0.3
Release:	%mkrel 1
License:	GPL
Group:		Graphics
URL:		http://goodies.xfce.org/projects/applications/ristretto
Source0:	%{name}-%{version}.tar.bz2 
BuildRequires:	gtk+2-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libthunar-devel
BuildRequires:	desktop-file-utils
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

%post
%{update_menus}
%{update_desktop_database}
%{update_mime_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_mime_database}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
