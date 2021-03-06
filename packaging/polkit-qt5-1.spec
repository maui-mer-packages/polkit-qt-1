# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       polkit-qt5-1

# >> macros
# << macros

Summary:    Qt bindings for PolicyKit
Version:    0.112.0
Release:    1
Group:      System/Libraries
License:    GPLv2+
URL:        https://projects.kde.org/projects/kdesupport/%{name}
Source0:    %{name}-%{version}.tar.xz
Source100:  polkit-qt5-1.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  cmake
BuildRequires:  cmake

%description
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations (like calling the HAL Mount() method)
for unprivileged (desktop) applications.

libpolkit-qt-1 provides convenience classes and methods for Qt/KDE
applications that want to use PolicyKit.

This package contains the files necessary for running applications that use
the libpolkit-qt-1 library.


%package devel
Summary:    PolicyKit Qt development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes.

It is a framework for centralizing the decision making process with respect to
granting access to privileged operations (like calling the HAL Mount() method)
for unprivileged (desktop) applications.

libpolkit-qt-1 provides convenience classes and methods for Qt/KDE
applications that want to use PolicyKit-1.

This package contains the development libraries and headers.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DUSE_QT5:bool=ON

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libpolkit-qt5-agent-1.so.1*
%{_libdir}/libpolkit-qt5-core-1.so.1*
%{_libdir}/libpolkit-qt5-gui-1.so.1*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/polkit-qt5-1/*
%{_libdir}/cmake/PolkitQt5-1/*
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
# >> files devel
# << files devel
