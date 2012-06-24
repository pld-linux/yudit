Summary:	Unicode Text Editor
Summary(pl):	Edytor tekstu Unicode
Name:		yudit
Version:	2.4.8
Release:	1
Epoch:		1
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplica��es/Editores
License:	GPL
Source0:	http://yudit.org/download/%{name}-%{version}.tar.gz
Vendor:		Gaspar Sinai <gsinai@yudit.org>
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Yudit is a unicode text editor for the X Window System. It does not
need localized environment or unicode fonts. It supports simultanious
processing of many languages, input methods, conversions for local
character standards. This package includes X11 editor interface, shell
conversion utilities and it also has support for postscript printing.

%description -l pl
Yudit jest edytorem tekstu w standardzie unicde dla systemu X Window.
Nie wymaga zloakalizowanego �rodowiska, ani font�w unicde. Wspiera
jednoczesne przetwarzanie wielu j�zyk�w, sposob�w wprowadzania tekstu,
konwersji z lokalnych standard�w kodowania. Pakiet tan zawiera
interferjs edytora dla X11, narz�dzia do konwersji, a tak�e wspiera
drukowanie PostScript.

%prep
%setup -q

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT%{_prefix}
%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Editors
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install gnome-yudit.png $RPM_BUILD_ROOT%{_pixmapsdir}/yudit.png

cat >$RPM_BUILD_ROOT%{_applnkdir}/Editors/yudit.desktop <<EOF
[Desktop Entry]
Name=Yudit (Unicode editor)
Type=Application
Description=The Yudit Unicode editor
Exec=yudit
Icon=yudit.png
EOF

gzip -9nf CHANGELOG.TXT COPYING FAQ.TXT README.TXT TODO.TXT doc/*.utf8 doc/problems/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/problems/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%dir %{_datadir}/yudit
%{_datadir}/yudit/data
%{_datadir}/yudit/fonts
%{_datadir}/yudit/src 
%{_datadir}/yudit/doc 
%{_applnkdir}/Editors/yudit.desktop
%{_pixmapsdir}/yudit.png
%dir %{_datadir}/yudit/locale
%lang(az) %{_datadir}/yudit/locale/az
%lang(bg) %{_datadir}/yudit/locale/bg
%lang(de) %{_datadir}/yudit/locale/de
%lang(en) %{_datadir}/yudit/locale/en
%lang(es) %{_datadir}/yudit/locale/es
%lang(fi) %{_datadir}/yudit/locale/fi
%lang(fr) %{_datadir}/yudit/locale/fr
%lang(hu) %{_datadir}/yudit/locale/hu
%lang(ja) %{_datadir}/yudit/locale/ja
%lang(sl) %{_datadir}/yudit/locale/sl
%lang(sr) %{_datadir}/yudit/locale/sr
%lang(yi) %{_datadir}/yudit/locale/yi
%dir %{_datadir}/yudit/config
%config %{_datadir}/yudit/config/*
