Name:           renesas_rcar-libgbm
Version:        1.0.0
Release:	0
License:	MIT
Summary:	libgbm library
Source:       %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
ExclusiveArch:	armv7l
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libkms)
BuildRequires:  pkgconfig(libdrm) >= 2.4.24
BuildRequires:  pkgconfig(libudev) > 150
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-kms)
BuildRequires:  pkgconfig(wayland-egl)

%description
libgbm - Reimplementation of gbm for use with kms backend

%package devel
Summary:    libgbm library (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libgbm development files

%prep
%setup

%build
autoreconf -vif
%configure
make

%install
%make_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libgbm.so.*
%{_libdir}/gbm/libgbm_kms.so.*

%files devel
%{_libdir}/libgbm.so
%{_libdir}/gbm/libgbm_kms.so
%exclude %{_libdir}/pkgconfig/gbm.pc
%{_includedir}/gbm.h
%exclude %{_includedir}/gbmint.h
%exclude %{_includedir}/common_drm.h
%exclude %{_includedir}/gbm_kmsint.h
