#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmypaint
Version  : 1.6.1
Release  : 13
URL      : https://github.com/mypaint/libmypaint/releases/download/v1.6.1/libmypaint-1.6.1.tar.xz
Source0  : https://github.com/mypaint/libmypaint/releases/download/v1.6.1/libmypaint-1.6.1.tar.xz
Summary  : MyPaint's brushstroke rendering library (@LIBMYPAINT_VERSION_FULL@)
Group    : Development/Tools
License  : HPND
Requires: libmypaint-data = %{version}-%{release}
Requires: libmypaint-lib = %{version}-%{release}
Requires: libmypaint-license = %{version}-%{release}
Requires: libmypaint-locales = %{version}-%{release}
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gegl-0.4)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libprofiler)

%description
# libmypaint - MyPaint brush engine library
[![Translation status](https://hosted.weblate.org/widgets/mypaint/-/libmypaint/svg-badge.svg)](https://hosted.weblate.org/engage/mypaint/?utm_source=widget)
[![Travis Build Status](https://travis-ci.org/mypaint/libmypaint.svg?branch=master)](https://travis-ci.org/mypaint/libmypaint)
[![Appveyor Build Status](https://ci.appveyor.com/api/projects/status/github/mypaint/libmypaint?branch=master&svg=true)](https://ci.appveyor.com/project/jonnor/libmypaint)

%package data
Summary: data components for the libmypaint package.
Group: Data

%description data
data components for the libmypaint package.


%package dev
Summary: dev components for the libmypaint package.
Group: Development
Requires: libmypaint-lib = %{version}-%{release}
Requires: libmypaint-data = %{version}-%{release}
Provides: libmypaint-devel = %{version}-%{release}
Requires: libmypaint = %{version}-%{release}

%description dev
dev components for the libmypaint package.


%package lib
Summary: lib components for the libmypaint package.
Group: Libraries
Requires: libmypaint-data = %{version}-%{release}
Requires: libmypaint-license = %{version}-%{release}

%description lib
lib components for the libmypaint package.


%package license
Summary: license components for the libmypaint package.
Group: Default

%description license
license components for the libmypaint package.


%package locales
Summary: locales components for the libmypaint package.
Group: Default

%description locales
locales components for the libmypaint package.


%prep
%setup -q -n libmypaint-1.6.1
cd %{_builddir}/libmypaint-1.6.1
pushd ..
cp -a libmypaint-1.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656131325
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656131325
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmypaint
cp %{_builddir}/libmypaint-1.6.1/COPYING %{buildroot}/usr/share/package-licenses/libmypaint/36b0708d2704b69ce4150e59f8b5173186cc38c7
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang libmypaint
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/MyPaint-1.6.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libmypaint/fastapprox/cast.h
/usr/include/libmypaint/fastapprox/fastexp.h
/usr/include/libmypaint/fastapprox/fastlog.h
/usr/include/libmypaint/fastapprox/fastpow.h
/usr/include/libmypaint/fastapprox/sse.h
/usr/include/libmypaint/glib/mypaint-brush.h
/usr/include/libmypaint/mypaint-brush-settings-gen.h
/usr/include/libmypaint/mypaint-brush-settings.h
/usr/include/libmypaint/mypaint-brush.h
/usr/include/libmypaint/mypaint-config.h
/usr/include/libmypaint/mypaint-fixed-tiled-surface.h
/usr/include/libmypaint/mypaint-glib-compat.h
/usr/include/libmypaint/mypaint-mapping.h
/usr/include/libmypaint/mypaint-matrix.h
/usr/include/libmypaint/mypaint-rectangle.h
/usr/include/libmypaint/mypaint-surface.h
/usr/include/libmypaint/mypaint-symmetry.h
/usr/include/libmypaint/mypaint-tiled-surface.h
/usr/lib64/libmypaint.so
/usr/lib64/pkgconfig/libmypaint.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libmypaint.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libmypaint.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libmypaint.so.0.0.0
/usr/lib64/libmypaint.so.0
/usr/lib64/libmypaint.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmypaint/36b0708d2704b69ce4150e59f8b5173186cc38c7

%files locales -f libmypaint.lang
%defattr(-,root,root,-)

