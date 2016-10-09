Name:           libjpeg8
Version:        d
Release:        1%{?dist}
Summary:        Independent JPEG Group's free JPEG software

License:        BSD
URL:            http://www.infai.org/jpeg/
Source0:        http://www.ijg.org/files/jpegsrc.v8d.tar.gz

#BuildRequires:  
#Requires:       

%description
JPEG library is a free library with functions for handling the JPEG
image data format.
This package doesn't conflict with other versions of libjpeg, since
it only provides the corresponding dynamic library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libjpeg-turbo
Conflicts:      libjpeg7
Conflicts:      libjpeg9

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
This package conflicts with other versions of libjpeg, along with
the libjpeg-turbo implementaion, since they provides different
versions of header files under the same time.

%package        utils
Summary:        Utility binaries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libjpeg-turbo
Conflicts:      libjpeg7
Conflicts:      libjpeg9

%description    utils
The %{name}-utils package contains utility binaries which comes
alongside with %{name}.
This package conflicts with other versions of libjpeg, along with
the libjpeg-turbo implementaion, since they provides different
versions of binaries under the same name.

%prep
%setup -n jpeg-8d -q

%build
%configure --disable-static
%make_build

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc change.log
%doc README
%{_libdir}/*.so.*

%files devel
%doc structure.txt
%doc usage.txt
%doc wizard.txt
%doc example.c
%{_includedir}/*
%{_libdir}/*.so

%files utils
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Sep 30 2016 aflyhorse@hotmail.com
- Initial implementation for v8.
