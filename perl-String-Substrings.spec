#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Substrings
Summary:	String::Substrings - module to extract some/all substrings from a string
#Summary(pl):	
Name:		perl-String-Substrings
Version:	0.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-String-Random
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has only one method C<substrings>.  It is called as

  substrings STRING [,LENGTH]

Without a length specification, it returns all substrings with a length
of 1 or greater including the string itselfs. The substrings returned
are sorted for the length (starting with length 1) and for their index.
E.g. C<substrings "abc"> returns C<("a","b","c","ab","bc","abc")>.
This order is guaranteed to stay even in future versions.  That also
includes that the returned list of substrings needn't be unique.
E.g. C<substrings "aaa"> returns C<("a","a","a","aa","aa","aaa")>.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
