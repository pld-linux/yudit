Summary:	Unicode text editor
Summary(pl):	Edytor tekstu unicode
Name:		yudit
Version:	2.7.6
%define	bver	beta2
Release:	0.%{bver}.2
Epoch:		1
License:	GPL
Vendor:		Gaspar Sinai <gsinai@yudit.org>
Group:		Applications/Editors
Source0:	http://yudit.org/download/%{name}-%{version}.%{bver}.tar.gz
# Source0-md5:	e83b524172af7945b568d4c387672719
Source1:	%{name}.desktop
Patch0:		%{name}-use_locale_by_default.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	FAQ.TXT

%description
Yudit is a unicode text editor for the X Window System. It does not
need localized environment or unicode fonts. It supports simultanious
processing of many languages, input methods, conversions for local
character standards. This package includes X11 editor interface, shell
conversion utilities and it also has support for postscript printing.

%description -l pl
Yudit jest edytorem tekstu w standardzie unicode dla systemu X Window.
Nie wymaga zloakalizowanego ¶rodowiska, ani fontów unicode. Wspiera
jednoczesne przetwarzanie wielu jêzyków, sposobów wprowadzania tekstu,
konwersji z lokalnych standardów kodowania. Pakiet tan zawiera
interferjs edytora dla X11, narzêdzia do konwersji, a tak¿e wspiera
drukowanie PostScript.

%prep
%setup -q -n %{name}-%{version}.%{bver}
%patch -p1

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
ln -sf ../../doc $RPM_BUILD_ROOT%{_datadir}/yudit/doc

rm -rf doc/??/FAQ.TXT.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT FAQ.TXT README.TXT TODO.TXT BUGS.TXT
%doc doc/*.utf8 doc/problems doc/HOWTO-*.txt
%lang(bg) %doc doc/bg
%lang(cs) %doc doc/cs
%lang(de) %doc doc/de
%lang(es) %doc doc/es
%lang(fi) %doc doc/fi
%lang(hu) %doc doc/hu
%lang(ja) %doc doc/ja
%lang(ko) %doc doc/ko
%lang(ru) %doc doc/ru
%lang(sr) %doc doc/sr
%lang(vi) %doc doc/vi
%lang(yi) %doc doc/yi
%lang(zh_HK,zh_TW) %doc doc/zh

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

%dir %{_datadir}/yudit
%{_datadir}/yudit/data
%{_datadir}/yudit/doc
%{_datadir}/yudit/fonts
%{_datadir}/yudit/src
%{_applnkdir}/Editors/yudit.desktop
%{_pixmapsdir}/yudit.png
%dir %{_datadir}/yudit/locale
%{_datadir}/yudit/locale/en
%lang(am) %{_datadir}/yudit/locale/am
%lang(ar) %{_datadir}/yudit/locale/ar
%lang(az) %{_datadir}/yudit/locale/az
%lang(bg) %{_datadir}/yudit/locale/bg
%lang(bn) %{_datadir}/yudit/locale/bn
%lang(cs) %{_datadir}/yudit/locale/cs
%lang(de) %{_datadir}/yudit/locale/de
%lang(el) %{_datadir}/yudit/locale/el
%lang(es) %{_datadir}/yudit/locale/es
%lang(fi) %{_datadir}/yudit/locale/fi
%lang(fr) %{_datadir}/yudit/locale/fr
%lang(hi) %{_datadir}/yudit/locale/hi
%lang(hu) %{_datadir}/yudit/locale/hu
%lang(ko) %{_datadir}/yudit/locale/ko
%lang(ja) %{_datadir}/yudit/locale/ja
%lang(mn) %{_datadir}/yudit/locale/mn
%lang(pl) %{_datadir}/yudit/locale/pl
%lang(ru) %{_datadir}/yudit/locale/ru
%lang(sl) %{_datadir}/yudit/locale/sl
%lang(sr) %{_datadir}/yudit/locale/sr
%lang(ta) %{_datadir}/yudit/locale/ta
%lang(ur) %{_datadir}/yudit/locale/ur
%lang(uk) %{_datadir}/yudit/locale/uk
%lang(vi) %{_datadir}/yudit/locale/vi
%lang(yi) %{_datadir}/yudit/locale/yi
%lang(zh_HK,zh_TW) %{_datadir}/yudit/locale/zh
%dir %{_datadir}/yudit/config
%config %{_datadir}/yudit/config/*
