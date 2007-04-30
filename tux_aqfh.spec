%define name	tux_aqfh
%define version	1.0.14
%define release	7mdk
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
BuildRequires:	plib-devel MesaGLU-devel XFree86-devel Mesa-common-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tuxedo T. Penguin: A Quest For Herring

%prep
%setup -q

%build
%configure	--bindir=%{_gamesbindir} \
		--x-libraries="%{_prefix}/X11R6/%{_lib} -lplibjs"
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} bindir=$RPM_BUILD_ROOT%{_gamesbindir}

install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  icon=%{name}.png \
		  needs="x11" \
		  section="More Applications/Games/Arcade" \
		  title="Tuxedo Quest"\
		  longtitle="%{Summary}"
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

#Move website to HTML so we can include it as a %doc instead of clutterng up %_datadir
mv $RPM_BUILD_ROOT%{_datadir}/%{name} HTML

%post
%{update_menus}
 
%postun
%{clean_menus}   

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
%{_menudir}/%{name}
