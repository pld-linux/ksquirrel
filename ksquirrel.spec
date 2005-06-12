Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych
Name:		ksquirrel
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	06bdb4235c082b529f54e41376a7c957
Patch0:		%{name}.desktop.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 3.2
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	ksquirrel-libs
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
%patch0 -p1

%build
sed -i -e 's#/usr/lib/squirrel/#%{_libdir}/ksquirrel#g' \
	./ksquirrel/ksquirrel.cpp ./ksquirrel/ksquirrelrc ./ksquirrel/sq_options.ui.h
install %{_datadir}/automake/config.* admin
%configure \
%if "%{_lib}" == "lib64"
        --enable-libsuffix=64 \
%endif
        --with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/ksquirrel.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/ksquirrel
%{_desktopdir}/ksquirrel.desktop
%{_datadir}/apps
%{_iconsdir}/*/*/*/*
