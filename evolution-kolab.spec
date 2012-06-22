%define	evolution_base_version	3.4
%define	major	0
%define	libname	%mklibname ekolabconv %{major}
%define	devname	%mklibname ekolabconv -d

Summary:	Kolab groupware Connector for Evolution
Name:		evolution-kolab
Version:	3.4.3
Release:	1
License:	GPLv2+
Group:		Networking/Mail
Url:		http://evolution-kolab.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	gperf
BuildRequires:	intltool
BuildRequires:	pkgconfig(evolution-data-server-1.2)
BuildRequires:	pkgconfig(evolution-plugin-3.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmime-2.4)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libedata-book-1.2)
BuildRequires:	pkgconfig(libedata-cal-1.2)
BuildRequires:	pkgconfig(libedataserverui-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libical)

%description
A project to provide connectivity to Kolab groupware servers for
Evolution

%package  -n %{libname}
Summary:	Client library for Accessing Kolab groupware Servers
Group:		System/Libraries

%description -n %{libname}
This package contains the libraries for %{name}.

%package -n %{devname}
Summary:	Development Files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
This package contains  the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-lm'

%install
%makeinstall_std

find %{buildroot}%{_libdir} -name '*.la' -delete -print
rm -fr %{buildroot}%{_prefix}/doc

%find_lang evolution_kolab

%files -f evolution_kolab.lang
%doc COPYING
%{_bindir}/camel-kolab-imapx-provider
%{_bindir}/evolution_kolab
%{_bindir}/tdriver
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendkolab.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendkolab.so
%{_libdir}/evolution-data-server/camel-providers/libcamelkolab.so
%{_libdir}/evolution-data-server/camel-providers/libcamelkolab.urls
%{_libdir}/evolution/%{evolution_base_version}/plugins/liborg-gnome-kolab.so
%{_libdir}/evolution/%{evolution_base_version}/plugins/org-gnome-kolab.eplug

%files -n %{libname}
%{_libdir}/libekolabconv.so.%{major}*
#these are odd, should the have a versioned soname or are the modules
%{_libdir}/libekolab.so
%{_libdir}/libekolabbackend.so
%{_libdir}/libekolabutil.so

%files -n %{devname}
%{_bindir}/test-kolab-*
%{_bindir}/unittest-libekolabconv
%{_libdir}/libekolabconv.so
%{_datadir}/gtk-doc/*
%{_datadir}/%{name}
