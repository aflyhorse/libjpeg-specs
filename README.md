# libjpeg-specs

There are RPM spec files for Independent JPEG Group's libjpeg.

Source files are fetched from [IJG's repository](http://www.ijg.org/files/).

Binary packages (as well as SRPMS) will be released under [COPR](https://copr.fedorainfracloud.org/coprs/aflyhorse/libjpeg/).

JPEG library is a free library with functions for handling the JPEG image data format. The libjpeg coming with Fedora/CentOS project (libjpeg-turbo) only provides v6 implementation of JPEG (aka. libjpeg.so.62). This project is provided as dependencies for various projects which need libjpeg.so.7, libjpeg.so.8, etc.

The corresponding libjpeg package only provides library files, thus won't conflict with other versions, as well as the factory version. The -devel and -utils pacakge conflicts with each other, since they provide files under the same location.

Please only contact me on packaging problems.
