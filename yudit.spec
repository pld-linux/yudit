Summary:	Unicode text editor
Summary(pl):	Edytor tekstu unicode
Name:		yudit
Version:	2.7.8
Release:	1
Epoch:		1
License:	GPL v2
Vendor:		Gaspar Sinai <gsinai@yudit.org>
Group:		X11/Applications/Editors
Source0:	http://yudit.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	48c1dc0c02c832a86abe9f6ec4cabdd6
Source1:	%{name}.desktop
Patch0:		%{name}-use_locale_by_default.patch
URL:		http://yudit.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.10
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
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

install gnome-yudit.png $RPM_BUILD_ROOT%{_pixmapsdir}/yudit.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
ln -sf ../../doc $RPM_BUILD_ROOT%{_datadir}/yudit/doc

rm -rf doc/??/FAQ.TXT.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.TXT FAQ.TXT NEWS.TXT README.TXT TODO.TXT *BUGS.TXT
%doc doc/*.utf8 doc/problems doc/HOWTO-*.txt
%lang(bg) %doc doc/bg
%lang(cs) %doc doc/cs
%lang(de) %doc doc/de
%lang(es) %doc doc/es
%lang(fi) %doc doc/fi
%lang(hu) %doc doc/hu
%lang(it) %doc doc/it
%lang(ja) %doc doc/ja
%lang(ko) %doc doc/ko
%lang(ru) %doc doc/ru
%lang(sr) %doc doc/sr
%lang(te) %doc doc/te
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
%{_desktopdir}/yudit.desktop
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
%lang(ga) %{_datadir}/yudit/locale/ga
%lang(gu) %{_datadir}/yudit/locale/gu
%lang(hi) %{_datadir}/yudit/locale/hi
%lang(hu) %{_datadir}/yudit/locale/hu
%lang(ja) %{_datadir}/yudit/locale/ja
%lang(ko) %{_datadir}/yudit/locale/ko
%lang(mn) %{_datadir}/yudit/locale/mn
%lang(mr) %{_datadir}/yudit/locale/mr
%lang(pa) %{_datadir}/yudit/locale/pa
%lang(pl) %{_datadir}/yudit/locale/pl
%lang(ru) %{_datadir}/yudit/locale/ru
%lang(sl) %{_datadir}/yudit/locale/sl
%lang(sr) %{_datadir}/yudit/locale/sr
%lang(ta) %{_datadir}/yudit/locale/ta
%lang(uk) %{_datadir}/yudit/locale/uk
%lang(ur) %{_datadir}/yudit/locale/ur
%lang(vi) %{_datadir}/yudit/locale/vi
%lang(yi) %{_datadir}/yudit/locale/yi
%lang(zh_HK,zh_TW) %{_datadir}/yudit/locale/zh
%dir %{_datadir}/yudit/config
%config %{_datadir}/yudit/config/*
