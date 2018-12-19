Name:           libjpeg8
Version:        8d1
Release:        4
Summary:        Independent JPEG Group's free JPEG software Version 8

License:        BSD
URL:            http://www.infai.org/jpeg/
Source0:        https://jpegclub.org/support/files/jpegsrc.v8d1.tar.gz

%description
JPEG library is a free library with functions for handling the JPEG
image data format.
This package doesn't conflict with other versions of libjpeg, since
it only provides the corresponding dynamic library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libjpeg-turbo-devel
Conflicts:      libjpeg7-devel
Conflicts:      libjpeg9-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
This package conflicts with other versions of libjpeg, along with
the libjpeg-turbo implementaion, since they provides different
versions of header files under the same time.

%package        utils
Summary:        Utility binaries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libjpeg7-utils
Conflicts:      libjpeg9-utils

%description    utils
The %{name}-utils package contains utility binaries which comes
alongside with %{name}.
This package conflicts with other versions of libjpeg, along with
the libjpeg-turbo implementaion, since they provides different
versions of binaries under the same name.

%prep
%setup -n jpeg-8d1 -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%check
LD_LIBRARY_PATH=${RPM_BUILD_ROOT}/%{_libdir} make check

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
* Wed Dec 19 2018 aflyhorse@hotmail.com
- Change the download link to https. No source change so no version bump.
* Sun Oct 9 2016 aflyhorse@hotmail.com
- Conflict fix.
* Sun Oct 9 2016 aflyhorse@hotmail.com
- Bump to v8d1.
* Sun Oct 9 2016 aflyhorse@hotmail.com
- Tweak version numbers.
- Configure libtools to make it more friendly to rpath.
* Fri Sep 30 2016 aflyhorse@hotmail.com
- Initial implementation for v8.
