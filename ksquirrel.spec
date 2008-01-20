# TODO:
# - recheck (was: doesn't work for me, runs but i cant view any image)
Summary:	Graphics file browser utility
Summary(pl.UTF-8):	Narzędzie do przeglądania plików graficznych
Name:		ksquirrel
Version:	0.7.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	61b8c4f653eb2a9f8b7572f6b14771df
Patch0:		%{name}-desktop.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.3
BuildRequires:	ksquirrel-libs-devel >= %{version}
BuildRequires:	libkexif-devel
BuildRequires:	libkipi-devel
BuildRequires:	pkgconfig
# libqui
BuildRequires:	qt-designer-libs
BuildRequires:	rpmbuild(macros) >= 1.197
Obsoletes:	ksquirrel-common
Obsoletes:	ksquirrel-small
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSquirrel is an image viewer for KDE with disk navigator, file tree,
thumbnails, extended thumbnails, dynamic format support and tools to
resize, convert, colorize and print images.

%description -l pl.UTF-8
KSquirrel to przeglądarka obrazków dla KDE z nawigacją po dyskach,
drzewku plików, miniaturkach, rozszerzonych miniaturkach i narzędziach
do zmiany wielkości, rozszerzenia, koloru i do drukowania obrazków.

%prep
%setup -q
%patch0 -p1

%build
install /usr/share/automake/config.* admin
%configure \
	--libdir=%{_libdir} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# move .desktop to proper place
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/ksquirrel
%{_datadir}/apps/konqueror/servicemenus/konqksquirrel-dir.desktop
%{_datadir}/apps/ksquirrel
%{_datadir}/config/magic/x-ras.magic
%{_datadir}/config/magic/x-sun.magic
%{_datadir}/config/magic/x-utah.magic
%{_datadir}/mimelnk/image/*.desktop
%{_desktopdir}/kde/ksquirrel.desktop
%{_iconsdir}/hicolor/*/apps/ksquirrel.png
%{_mandir}/man1/ksquirrel.1*
