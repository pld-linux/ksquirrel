Summary:	Graphics file browser utility
Summary(pl):	Narz�dzie do przegl�dania plik�w graficznych
Name:		ksquirrel
Version:	0.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	86d7f2204344f718f07f14921834b3da
Patch0:		%{name}-desktop.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 3.2
BuildRequires:	ksquirrel-libs-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSquirrel is an image viewer for KDE with disk navigator, file tree,
thumbnails, extended thumbnails, dynamic format support and tools to
resize, convert, colorize and print images.

%description -l pl
KSquirrel to przegl�darka obrazk�w dla KDE z nawigacj� po dyskach,
drzewku plik�w, miniaturkach, rozszerzonych miniaturkach i narz�dziach
do zmiany wielko�ci, rozszerzenia, koloru i do drukowania obrazk�w.

%package common
Summary:	Common files for KSquirrel
Summary(pl):	Pliki wsp�lne dla KSquirrel
Group:		X11/Applications/Graphics

%description common
Documentation and common files for ksquirrel and ksquirrel-small.

%description common
Dokumentacja oraz pliki wsp�lne dla ksquirrel i ksquirrel-small.

%package small
Summary:	Graphics file browser utility - small version
Summary(pl):	Narz�dzie do przegl�dania plik�w graficznych - ma�a wersja
Group:		X11/Applications/Graphics
Requires:	%{name}-common = %{version}-%{release}

%description small
KSquirrel is an image viewer for KDE with disk navigator, file tree,
thumbnails, extended thumbnails, dynamic format support and tools to
resize, convert, colorize and print images - small version.

%description small -l pl
KSquirrel to przegl�darka obrazk�w dla KDE z nawigacj� po dyskach,
drzewku plik�w, miniaturkach, rozszerzonych miniaturkach i narz�dziach
do zmiany wielko�ci, rozszerzenia, koloru i do drukowania obrazk�w -
ma�a wersja.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@/usr/lib@%{_libdir}@g' ksquirrel{,/ksquirrel-small}/*.{cpp,ui*}

%build
install /usr/share/automake/config.* admin
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/ksquirrel{,-small}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksquirrel
%{_desktopdir}/ksquirrel.desktop
%{_mandir}/man1/ksquirrel.*

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%{_datadir}/apps/ksquirrel
%{_iconsdir}/hicolor/*/*/*

%files small
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksquirrel-small
%{_desktopdir}/ksquirrel-small.desktop
%{_mandir}/man1/ksquirrel-small.*
