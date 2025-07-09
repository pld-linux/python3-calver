#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	calver
Summary:	Setuptools extension for CalVer package versions
Summary(pl.UTF-8):	Rozszerzenie setuptools do wersji pakietów CalVer
Name:		python3-%{module}
Version:	2025.4.17
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/calver/
Source0:	https://files.pythonhosted.org/packages/source/c/calver/%{module}-%{version}.tar.gz
# Source0-md5:	b02f51c61083eb5bd1b84218ec2fffd3
URL:		https://pypi.org/project/calver/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:77.0.1
%if %{with tests}
BuildRequires:	python3-pretend
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The calver package is a setuptools extension for automatically
defining your Python package version as a calendar version.

%description -l pl.UTF-8
Pakiet calver to rozszerzenie setuptools do automatycznego
definiowania wersji pakietów Pythona jako wersji kalendarzowych.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
