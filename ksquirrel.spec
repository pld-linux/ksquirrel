# TODO
# - categories fix
# - libs package
# - check BR/B

Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych
Name:		ksquirrel
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}-pre4.tar.bz2
# Source0-md5:	3a1894e8bef2131adb8b1a8ca7c824b1
Source1:	http://dl.sourceforge.net/ksquirrel/%{name}-libs-%{version}-pre3.tar.bz2
# Source1-md5:  7e0311f34664261f116feec6c015791f
#Patch0:		%{name}-etc_dir.patch
URL:		http://ksquirrel.sourceforge.net/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:  kdebase-devel >= 3.2
BuildRequires:  OpenGL-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSquirrel is an image viewer for KDE with disk navigator, file tree,
thumbnails, extended thumbnails, dynamic format support and tools to
resize, convert, colorize and print images.

%description -l pl
KSquirrel to przegl±darka obrazków dla KDE z nawigacj± po dyskach,
drzewku plików, miniaturkach, rozszerzonych miniaturkach i narzêdziach
do zmiany wielko¶ci, rozszerzenia, koloru i do drukowania obrazków.

%package libs
Summary:        KSquirrel libraries
Summary(pl):    Biblioteki przegl±darki graficznej KSquirrel
Group:          X11/Applications/Graphics

%description libs
ksquirrel libraries.

%description libs -l pl
Biblioteki przegl±darki graficznej KSquirrel.

%prep
%setup -q

%build
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
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
%{_iconsdir}
