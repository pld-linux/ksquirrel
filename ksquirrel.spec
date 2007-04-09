%define		_pre	pre2
Summary:	Graphics file browser utility
Summary(pl.UTF-8):	Narzędzie do przeglądania plików graficznych
Name:		ksquirrel
Version:	0.7.0
Release:	0.%{_pre}.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}-%{_pre}.tar.bz2
# Source0-md5:	8798cffb9a3203af51104e49a1481246
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

%description -l pl.UTF-8
KSquirrel to przeglądarka obrazków dla KDE z nawigacją po dyskach,
drzewku plików, miniaturkach, rozszerzonych miniaturkach i narzędziach
do zmiany wielkości, rozszerzenia, koloru i do drukowania obrazków.

%package common
Summary:	Common files for KSquirrel
Summary(pl.UTF-8):	Pliki wspólne dla KSquirrel
Group:		X11/Applications/Graphics

%description common
Documentation and common files for ksquirrel and ksquirrel-small.

%description common -l pl.UTF-8
Dokumentacja oraz pliki wspólne dla ksquirrel i ksquirrel-small.

%package small
Summary:	Graphics file browser utility - small version
Summary(pl.UTF-8):	Narzędzie do przeglądania plików graficznych - mała wersja
Group:		X11/Applications/Graphics
Requires:	%{name}-common = %{version}-%{release}

%description small
KSquirrel is an image viewer for KDE with disk navigator, file tree,
thumbnails, extended thumbnails, dynamic format support and tools to
resize, convert, colorize and print images - small version.

%description small -l pl.UTF-8
KSquirrel to przeglądarka obrazków dla KDE z nawigacją po dyskach,
drzewku plików, miniaturkach, rozszerzonych miniaturkach i narzędziach
do zmiany wielkości, rozszerzenia, koloru i do drukowania obrazków -
mała wersja.

%prep
%setup -q -n %{name}-%{version}-%{_pre}
%patch0 -p1
%{__sed} -i 's@/usr/lib@%{_libdir}@g' ksquirrel/*.{cpp,ui*}

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
