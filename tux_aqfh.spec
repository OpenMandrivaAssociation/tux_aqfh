%define name	tux_aqfh
%define version	1.0.14
%define release	14
%define	Summary	Tuxedo T. Penguin: A Quest For Herring

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		https://tuxaqfh.sourceforge.net/
Group:		Games/Arcade
Source0:	http://tuxaqfh.sourceforge.net/dist/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Summary:	%{Summary}
BuildRequires:	plib-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:	glut-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)

%description
Tuxedo T. Penguin: A Quest For Herring

%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir} --x-libraries="-L%{_libdir} -lplibjs"
%make

%install
%{makeinstall} bindir=%{buildroot}%{_gamesbindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

#Move website to HTML so we can include it as a %doc instead of clutterng up %_datadir
mv %{buildroot}%{_datadir}/%{name} HTML

%files
%doc README HTML
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
