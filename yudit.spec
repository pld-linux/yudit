Summary:	Unicode Text Editor
Summary(pl):	Edytor tekstu Unicode
Name:		yudit
Version:	2.6
Release:	3
Epoch:		1
License:	GPL
Vendor:		Gaspar Sinai <gsinai@yudit.org>
Group:		Applications/Editors
Source0:	http://yudit.org/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
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
Nie wymaga zloakalizowanego ¶rodowiska, ani fontów unicde. Wspiera
jednoczesne przetwarzanie wielu jêzyków, sposobów wprowadzania tekstu,
konwersji z lokalnych standardów kodowania. Pakiet tan zawiera
interferjs edytora dla X11, narzêdzia do konwersji, a tak¿e wspiera
drukowanie PostScript.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Editors,%{_pixmapsdir}}

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

install gnome-yudit.png $RPM_BUILD_ROOT%{_pixmapsdir}/yudit.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors

rm -rf doc/cz doc/??/FAQ.TXT.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT FAQ.TXT README.TXT TODO.TXT BUGS.TXT
%doc doc/*.utf8 doc/problems 
%lang(bg) %doc doc/bg
#%lang(cs) %doc doc/cz
%lang(de) %doc doc/de
%lang(es) %doc doc/es
%lang(fi) %doc doc/fi
%lang(hu) %doc doc/hu
%lang(ja) %doc doc/ja
%lang(yi) %doc doc/yi
%lang(zh) %doc doc/zh

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%dir %{_datadir}/yudit
%{_datadir}/yudit/data
%{_datadir}/yudit/fonts
%{_datadir}/yudit/src
%{_applnkdir}/Editors/yudit.desktop
%{_pixmapsdir}/yudit.png
%dir %{_datadir}/yudit/locale
%{_datadir}/yudit/locale/en
%lang(az) %{_datadir}/yudit/locale/ar
%lang(ar) %{_datadir}/yudit/locale/az
%lang(bg) %{_datadir}/yudit/locale/bg
%lang(de) %{_datadir}/yudit/locale/de
%lang(es) %{_datadir}/yudit/locale/es
%lang(fi) %{_datadir}/yudit/locale/fi
%lang(fr) %{_datadir}/yudit/locale/fr
%lang(hi) %{_datadir}/yudit/locale/hi
%lang(hu) %{_datadir}/yudit/locale/hu
%lang(ja) %{_datadir}/yudit/locale/ja
%lang(sl) %{_datadir}/yudit/locale/sl
%lang(sr) %{_datadir}/yudit/locale/sr
%lang(ta) %{_datadir}/yudit/locale/ta
%lang(yi) %{_datadir}/yudit/locale/yi
%lang(zh) %{_datadir}/yudit/locale/zh
%dir %{_datadir}/yudit/config
%config %{_datadir}/yudit/config/*
