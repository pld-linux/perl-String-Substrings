#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	String
%define		pnam	Substrings
%include	/usr/lib/rpm/macros.perl
Summary:	String::Substrings - module to extract some/all substrings from a string
Summary(pl.UTF-8):	String::Substrings - moduł do wyciągania części/wszystkich podciągów z ciągu
Name:		perl-String-Substrings
Version:	0.02
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f733d88cd3f8349946832fb640984842
URL:		http://search.cpan.org/dist/String-Substrings/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-String-Random
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has only one method substrings. It is called as substrings
STRING [,LENGTH]. Without a length specification, it returns all
substrings with a length of 1 or greater including the string itselfs.
The substrings returned are sorted for the length (starting with
length 1) and for their index. E.g. substrings "abc" returns
("a","b","c","ab","bc","abc"). This order is guaranteed to stay even
in future versions. That also includes that the returned list of
substrings needn't be unique. E.g. substrings "aaa" returns
("a","a","a","aa","aa","aaa").

%description -l pl.UTF-8
Ten moduł ma tylko jedną metodę - substrings. Wywołuje się ją jako
substrings CIĄG [,DŁUGOŚĆ]. Bez podanej długości, zwraca wszystkie
podciągi o długości 1 lub większej, włącznie z całym ciągiem. Zwracane
podciągi są posortowane po długości (począwszy od 1) i po indeksie.
Np. substrings "abc" zwraca ("a","b","c","ab","bc","abc").
Gwarantowane jest zachowanie kolejności w przyszłych wersjach.
Zwracana lista podciągów nie musi być unikalna. Np. substrings "aaa"
zwraca ("a","a","a","aa","aa","aaa").

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
