Summary:	GNOME mud client
Summary(pl.UTF-8):	Klient muda dla GNOME
Name:		gnome-mud
Version:	0.10.7
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	1198ab9466435a5cd30f1e47bbf6f8fe
URL:		http://amcl.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	intltool >= 0.23
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 1.99.13
BuildRequires:	rpm-pythonprov
BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.10.26
BuildRequires:	zlib-devel
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME mud client.

%description -l pl.UTF-8
Klient muda dla GNOME.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install \
	--enable-mccp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS PLUGIN.API README ROADMAP
%attr(755,root,root) %{_prefix}/games/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man6/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
