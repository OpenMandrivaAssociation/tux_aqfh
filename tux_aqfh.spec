%define name	tux_aqfh
%define version	1.0.14
%define release	%mkrel 11
%define	Summary	Tuxedo T. Penguin: A Quest For Herring

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://tuxaqfh.sourceforge.net/
Group:		Games/Arcade
Source0:	http://tuxaqfh.sourceforge.net/dist/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Summary:	%{Summary}
BuildRequires:	plib-devel
BuildRequires:  libmesaglu-devel
BuildRequires:	libmesaglut-devel
BuildRequires:  libx11-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tuxedo T. Penguin: A Quest For Herring

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir} --x-libraries="-L%{_libdir} -lplibjs"
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} bindir=$RPM_BUILD_ROOT%{_gamesbindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

#Move website to HTML so we can include it as a %doc instead of clutterng up %_datadir
mv $RPM_BUILD_ROOT%{_datadir}/%{name} HTML

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}   
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README HTML
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
