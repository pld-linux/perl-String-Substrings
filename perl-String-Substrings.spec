#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Substrings
Summary:	String::Substrings - module to extract some/all substrings from a string
Summary(pl):	String::Substrings - modu³ do wyci±gania czê¶ci/wszystkich podci±gów z ci±gu
Name:		perl-String-Substrings
Version:	0.02
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f733d88cd3f8349946832fb640984842
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-String-Random
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has only one method substrings. It is called as
substrings STRING [,LENGTH]. Without a length specification, it
returns all substrings with a length of 1 or greater including the
string itselfs. The substrings returned are sorted for the length
(starting with length 1) and for their index. E.g. substrings "abc"
returns ("a","b","c","ab","bc","abc"). This order is guaranteed to
stay even in future versions. That also includes that the returned
list of substrings needn't be unique. E.g. substrings "aaa" returns
("a","a","a","aa","aa","aaa").

%description -l pl
Ten modu³ ma tylko jedn± metodê - substrings. Wywo³uje siê j± jako
substrings CI¡G [,D£UGO¦Æ]. Bez podanej d³ugo¶ci, zwraca wszystkie
podci±gi o d³ugo¶ci 1 lub wiêkszej, w³±cznie z ca³ym ci±giem. Zwracane
podci±gi s± posortowane po d³ugo¶ci (pocz±wszy od 1) i po indeksie.
Np. substrings "abc" zwraca ("a","b","c","ab","bc","abc").
Gwarantowane jest zachowanie kolejno¶ci w przysz³ych wersjach.
Zwracana lista podci±gów nie musi byæ unikalna. Np. substrings "aaa"
zwraca ("a","a","a","aa","aa","aaa").

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
