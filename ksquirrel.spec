# TODO:
# - add libkexif support, with it i get:
#   /usr/bin/ld: ksquirrel: hidden symbol `__dso_handle' in
#   /usr/lib64/gcc/x86_64-pld-linux/4.2.1/crtbegin.o is referenced by DSO
#   /usr/bin/ld: final link failed: Nonrepresentable section on output
# - check if BR: qt-designer-libs is really needed, without it i get:
#   /usr/bin/ld: cannot find -lqui
# - doesn't work for me, runs but i cant view any image
Summary:	Graphics file browser utility
Summary(pl.UTF-8):	Narzędzie do przeglądania plików graficznych
Name:		ksquirrel
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	73f15672456e85c05c4f49baa396cbd7
Patch0:		%{name}-desktop.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 3.2
BuildRequires:	ksquirrel-libs-devel >= %{version}
#BuildRequires:	libkexif-devel
BuildRequires:	libkipi-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-designer-libs
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
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
	--disable-kexif \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# move .desktop to proper place
mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Graphics/%{name}.desktop,%{_desktopdir}}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ksquirrel
%{_datadir}/apps/konqueror/servicemenus/konqksquirrel-dir.desktop
%{_datadir}/apps/ksquirrel
%{_datadir}/config/magic/*.magic
%{_datadir}/mimelnk/image/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/ksquirrel.desktop
%{_mandir}/man1/ksquirrel.*
