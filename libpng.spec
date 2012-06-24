Summary:	PNG library
Summary(de):	PNG-Library
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG 
Summary(tr):	PNG kitapl���
Name:		libpng
Version:	1.0.14
Release:	1
Epoch:		2
License:	Distributable
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://swrinde.nde.swri.edu/pub/png/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-pngminus.patch
Patch2:		%{name}-badchunks.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libpng2

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l pl
Biblioteki PNG s� kolekcj� form u�ywanych do tworzenia i manipulowania
plikami w formatacie graficznym PNG. Format ten zosta� stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowo�ciami.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
f�r GIF entwickelt und enth�lt viele Verbesserungen und Erweiterungen.

%description -l fr
La librairie PNG est un ensemble de routines utilis�es pour cr�er et
manipuler des fichiers graphiques au format PNG. Le format PNG a �t�
�labor� pour remplacer le GIF, avec de nombreuses am�liorations et
extensions.

%description -l tr
PNG kitapl���, PNG format�ndaki resim dosyalar�n� i�lemeye y�nelik
yordamlar� i�erir. PNG, GIF format�n�n yerini almak �zere tasarlanm��
bir resim format�d�r.

%package devel
Summary:	headers 
Summary(de):	Headers und statische Libraries 
Summary(fr):	en-t�tes et biblioth�ques statiques
Summary(pl):	Pliki nag��wkowe
Summary(tr):	ba�l�k dosyalar� ve statik kitapl�klar
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	zlib-devel
Obsoletes:	libpng2-devel

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description -l pl devel
W pakiecie tym znajduj� si� pliki nag��wkowe, przeznaczone dla
programist�w u�ywaj�cych bibliotek PNG.

%description -l de devel
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library ben�tigt.

%description -l fr devel
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
d�veloppement avec la librairie PNG.

%description -l tr devel
PNG kitapl���n� kullanan programlar geli�tirmek i�in gereken
kitapl�klar ve ba�l�k dosyalar�.

%package static
Summary:	static libraries
Summary(pl):	Biblioteki statyczne
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%description -l pl static
Biblioteki statyczne.

%package progs
Summary:	libpng utility programs
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika

%description progs
This package contains utility programs to convert png files to and
from pnm files.

%description -l pl progs
Narz�dzia do konwersji plik�w png z lub do plik�w pnm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

ln -s scripts/makefile.linux ./Makefile

%build
%{__make} OPT_FLAGS="%{rpmcflags}"
cd contrib/pngminus
%{__make} -f makefile.std \
	OPT_FLAGS="%{rpmcflags} -I../../"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}}

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

install png.5 $RPM_BUILD_ROOT%{_mandir}/man5/
install {libpngpf,libpng}.3 $RPM_BUILD_ROOT%{_mandir}/man3/
install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf *.txt ANNOUNCE CHANGES KNOWNBUG README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
