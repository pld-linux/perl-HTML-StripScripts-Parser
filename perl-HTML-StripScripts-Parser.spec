#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	StripScripts-Parser
Summary:	HTML::StripScripts::Parser - XSS filter using HTML::Parser
Summary(pl.UTF-8):	HTML::StripScripts::Parser - filtr XSS używający HTML::Parser
Name:		perl-HTML-StripScripts-Parser
Version:	1.03
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4c169034be56590a53f8835529627ba
URL:		http://search.cpan.org/dist/HTML-StripScripts-Parser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.56
BuildRequires:	perl-HTML-StripScripts >= 1.04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an easy interface to HTML::StripScripts, using
HTML::Parser to parse the HTML.

See HTML::Parser for details of how to customise how the raw HTML is parsed
into tags, and HTML::StripScripts for details of how to customise the way
those tags are filtered.

%description -l pl.UTF-8
Klasa ta dostarcza prosty interfejs do HTML::StripScripts przy użyciu HTML::Parser aby przetwarzać HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/HTML/StripScripts
%{perl_vendorlib}/HTML/StripScripts/*.pm
%{_mandir}/man3/*
