Name: ficl
Version: 4.2.0rc1
Release: alt1

Summary: FORTH-Inspired Command Language
License: %bsd
Group: Development/Other

Url: https://github.com/NIR-Ginko/ficl
Source: %{name}-%{version}.tar.gz
Packager: Igor Chudov <nir@sarfsc.ru>

BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-make
BuildPreReq: rpm-macros-cmake
BuildPreReq: rpm-macros-generic-compat

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: rpm-build-licenses
BuildRequires: rpm-macros-make
BuildRequires: rpm-macros-cmake
BuildRequires: rpm-macros-generic-compat

%description
Fork of abandoned FORTH-Inspired Command Language

This is a FORTH language interpreter which is interesting with its
OOP system and ability to be embedded as a DSL interpreter.

%prep
%setup

%build
%cmake_insource . -DCMAKE_INSTALL_PREFIX=%prefix
%make_build

%install
%makeinstall_std

%files
%{_bindir}/ficl

%changelog
* Mon Jan 14 2019 Igor Chudov <nir@sarfsc.ru> 4.2.0rc1-alt1
- Initial build for Sisyphus.

