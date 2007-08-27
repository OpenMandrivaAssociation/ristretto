%define oname Ristretto

Summary:	A picture viewer for the Xfce desktop environment
Name:		ristretto
Version:	0.0.1
Release:	%mkrel 1
License:	GPL
Group:		Desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/ristretto
Source0:	%{name}-%{version}.tar.bz2 
BuildRequires:	gtk+2-devel
BuildRequires:	desktop-file-utils
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Ristretto is a fast and lightweight picture-viewer for the 
Xfce desktop environment.

%prep
%setup -qn %{name}-%{version}-

%build
%configure2_5x
		
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

%clean 
rm -rf %{buildroot}

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
