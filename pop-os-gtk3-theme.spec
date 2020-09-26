Name:           pop-os-gtk3-theme
Version:        5.2.0~1599689740~20.10~11b9d22
Release:        1%{?dist}
Summary:        A GTK+ theme for Pop!_OS

License:        LGPLv3
URL:            https://github.com/pop-os/gtk-theme
Source:         https://launchpad.net/~system76/+archive/ubuntu/pop/+sourcefiles/pop-gtk-theme/%{version}/pop-gtk-theme_%{version}.tar.xz
BuildArch: noarch



BuildRequires:  meson sassc glib2-devel

%description
A GTK+ theme for Pop!_OS

%changelog
* Wed Sep 23 2020 Justin Haygood <jhaygood86@gmail.com> - 5.2.0~1599689740~20.10~11b9d22
- Initial version of the package

%global _vpath_srcdir 11b9d2254a7e2506e14f42f77dc9d54095066175_groovy

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_datadir}/gnome-shell/theme/*.css
%{_datadir}/gnome-shell/theme/Pop/*
%{_datadir}/gnome-shell/theme/Pop-dark/*
%{_datadir}/sounds/Pop/index.theme
%{_datadir}/sounds/Pop/stereo/action/*.oga
%{_datadir}/sounds/Pop/stereo/alert/*.oga
%{_datadir}/sounds/Pop/stereo/notification/*.oga
%{_datadir}/themes/Pop/index.theme
%{_datadir}/themes/Pop/gnome-shell
%{_datadir}/themes/Pop/gtk-2.0/*rc
%{_datadir}/themes/Pop/gtk-2.0/assets/*.png
%{_datadir}/themes/Pop/gtk-3.0/*.css
%{_datadir}/themes/Pop/gtk-3.0/*.gresource
%{_datadir}/themes/Pop/gtk-3.20/*.css
%{_datadir}/themes/Pop/gtk-3.20/*.gresource
%{_datadir}/themes/Pop-dark/index.theme
%{_datadir}/themes/Pop-dark/gtk-2.0/*rc
%{_datadir}/themes/Pop-dark/gtk-2.0/assets/*.png
%{_datadir}/themes/Pop-dark/gtk-3.0/*.css
%{_datadir}/themes/Pop-dark/gtk-3.0/*.gresource
%{_datadir}/themes/Pop-dark/gtk-3.20/*.css
%{_datadir}/themes/Pop-dark/gtk-3.20/*.gresource

