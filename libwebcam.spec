%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A library for user-space configuration of the uvcvideo driver
Name:		libwebcam
Version:	0.2.3
Release:	2
Group:		System/Kernel and hardware
License:	GPLv3+
Url:		http://sourceforge.net/p/libwebcam/wiki/Home/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
Patch0:		libwebcam-silence-uvcdynctrl.patch
Patch1:		libwebcam-src-0.2.3-v4l2-check.patch
BuildRequires:	cmake
BuildRequires:	gengetopt
BuildRequires:	pkgconfig(libxml-2.0)

%description
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A library for user-space configuration of the uvcvideo driver
Group:		System/Libraries

%description -n %{libname}
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

%files -n %{libname}
%doc libwebcam/README libwebcam/COPYING.LESSER
%{_libdir}/libwebcam.so.*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries and headers for libwebcam
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development libraries and headers for libwebcam.

%files -n %{devname}
%{_includedir}/webcam.h
%{_libdir}/libwebcam.so
%{_libdir}/pkgconfig/libwebcam.pc

#----------------------------------------------------------------------------

%package -n uvcdynctrl
Summary:	Command line interface to libwebcam
Group:		System/Kernel and hardware
Requires:	uvcdynctrl-data = %{EVRD}

%description -n uvcdynctrl
Uvcdynctrl is a command line interface for manipulating settings in
UVC-type webcams. It uses the libwebcam library for webcam access.

%files -n uvcdynctrl
%doc uvcdynctrl/README uvcdynctrl/COPYING
%{_bindir}/uvcdynctrl*
/lib/udev/uvcdynctrl
/lib/udev/rules.d/80-uvcdynctrl.rules
%{_mandir}/man1/uvcdynctrl*.1*

#----------------------------------------------------------------------------

%package -n uvcdynctrl-data
Summary:	XML control file for the uvcdynctrl package
Group:		System/Kernel and hardware
Requires:	uvcdynctrl = %{EVRD}
BuildArch:	noarch

%description -n uvcdynctrl-data
XML control file for the uvcdynctrl package.

%files -n uvcdynctrl-data
%{_datadir}/uvcdynctrl

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build
rm %{buildroot}%{_libdir}/libwebcam.a

