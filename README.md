# What is this project?

There are RPM spec files for [Independent JPEG Group](https://www.ijg.org/)'s libjpeg. JPEG library is a free library with functions for handling the JPEG image data format.

# Is it safe?

Source files are directly fetched from [IJG's repository](https://www.ijg.org/files/) or its sibling [support site](https://jpegclub.org/support/files/).

# How to utilize this project?

Binary packages (as well as SRPMS) are released at [COPR](https://copr.fedorainfracloud.org/coprs/aflyhorse/libjpeg/).

- libjpeg7 ![7status](https://copr.fedorainfracloud.org/coprs/aflyhorse/libjpeg/package/libjpeg7/status_image/last_build.png)
- libjpeg8 ![8status](https://copr.fedorainfracloud.org/coprs/aflyhorse/libjpeg/package/libjpeg8/status_image/last_build.png)
- libjpeg9 ![9status](https://copr.fedorainfracloud.org/coprs/aflyhorse/libjpeg/package/libjpeg9/status_image/last_build.png)

# Why do you create this project?

The libjpeg coming with Fedora/CentOS project (libjpeg-turbo) only provides v6 implementation of JPEG (aka. libjpeg.so.62). This project is provided as dependencies for various projects which need libjpeg.so.7, libjpeg.so.8 and libjpeg.so.9.

The corresponding libjpeg package only provides library files, thus won't conflict with other versions, as well as the factory version. The -devel and -utils pacakge conflicts with each other, since they provide files under the same location.

# How can I report problems?

I only build official released tarballs (or officially suggested ones).

Please only contact me on packaging problems. For the others, please report to the upstream.
