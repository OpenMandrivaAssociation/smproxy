Name: smproxy
Version: 1.0.6
Release: 3
Summary: Session Manager Proxy
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Smproxy allows X applications that do not support X11R6 session management
to participate in an X11R6 session.

%prep
%setup -q -n %{name}-%{version}

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/smproxy
%{_mandir}/man1/smproxy.*
