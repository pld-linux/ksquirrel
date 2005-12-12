Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych
Name:		ksquirrel
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	ab0fedf3536b9c4d49dd01c775165476
Source1:	%{name}.desktop
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
Requires:	ksquirrel-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSquirrel is an image viewer for KDE with disk navigator, file tree,
thumbnails, extended thumbnails, dynamic format support and tools to
resize, convert, colorize and print images.

%description -l pl
KSquirrel to przegl±darka obrazków dla KDE z nawigacj± po dyskach,
drzewku plików, miniaturkach, rozszerzonych miniaturkach i narzêdziach
do zmiany wielko¶ci, rozszerzenia, koloru i do drukowania obrazków.

%prep
%setup -q
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

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/ksquirrel.desktop
%{_datadir}/apps/ksquirrel
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/ksquirrel*
