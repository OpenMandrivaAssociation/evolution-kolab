%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		evolution-kolab
Summary:	Kolab support for Evolution
Version:	3.6.2
Release:	%mkrel 1
License:	LGPLv2+
Group:		Networking/Mail
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
URL:		https://live.gnome.org/Evolution/Kolab
BuildRequires:	pkgconfig(camel-1.2)
BuildRequires:	pkgconfig(evolution-plugin-3.0)
BuildRequires:	pkgconfig(gconf-2.0) >= 2.0.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.1
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.99.2
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libebackend-1.2)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libedata-book-1.2)
BuildRequires:	pkgconfig(libedata-cal-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedataserverui-3.0)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	gtk-doc
BuildRequires:	evolution-devel
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	intltool >= 0.35.5
BuildRequires:	gettext-devel
BuildRequires:	gperf
BuildRequires:	gnome-common
Requires:	evolution

%description
Provide connectivity to Kolab groupware servers for Evolution.

%files -f evolution_kolab.lang
%doc NEWS
%{_bindir}/*
%{_libdir}/evolution-data-server/*/*
%{_libdir}/evolution/*/plugins/*
%{_libdir}/evolution/*/modules/*.so

#----------------------------------------------------------------------

%define major	0
%define libname %mklibname ekolabconv %{major}

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library for %{name}

%description -n %{libname}
Library for %{name}.

%files -n %{libname}
%{_libdir}/libekolabconv.so.%{major}
%{_libdir}/libekolabconv.so.%{major}.*

#----------------------------------------------------------------------

%package devel
Group:		Development/C
Summary:	Headers for writing %{name} plugins
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}

%description devel
Install this if you want to build plugins that use %{name}'s API.

%files devel
%{_libdir}/libekolabconv.so
%{_datadir}/gtk-doc/html/*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
make

%install
%makeinstall_std

find %{buildroot} -name *.la | xargs rm

rm -fr %{buildroot}%{_prefix}/doc

%find_lang evolution_kolab
