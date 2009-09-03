Name: smproxy
Version: 1.0.2
Release: %mkrel 6
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
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/smproxy
%{_mandir}/man1/smproxy.*


