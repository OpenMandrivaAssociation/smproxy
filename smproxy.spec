Summary:	Session Manager Proxy
Name:		smproxy
Version:	1.0.7
Release:	1
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xorg-macros)

%description
Smproxy allows X applications that do not support X11R6 session management
to participate in an X11R6 session.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/smproxy
%doc %{_mandir}/man1/smproxy.*
