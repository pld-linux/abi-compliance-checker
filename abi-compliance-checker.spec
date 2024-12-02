Summary:	Tool for checking backward API/ABI compatibility
Name:		abi-compliance-checker
Version:	2.3
Release:	1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	https://github.com/lvc/abi-compliance-checker/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7234921acc9dabee1d1cb6a5ac43c4be
URL:		https://github.com/lvc/abi-compliance-checker
BuildRequires:	perl-base >= 5
Requires:	abi-dumper >= 1.1
Requires:	binutils
Requires:	perl-base >= 5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tool analyzes changes in API/ABI (ABI=API+compiler ABI) that may
break binary compatibility and/or source compatibility: changes in
calling stack, v-table changes, removed symbols, renamed fields, etc.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}

%{__perl} Makefile.pl \
	-install \
	--prefix="%{_prefix}" \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/abi-compliance-checker
%{_datadir}/abi-compliance-checker
