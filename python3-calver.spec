%define		module	calver
Summary:	Setuptools extension for CalVer package versions
Summary(pl.UTF-8):	Rozszerzenie setuptools do wersji pakietów CalVer
Name:		python3-%{module}
Version:	2022.6.26
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	https://pypi.debian.net/calver/%{module}-%{version}.tar.gz
# Source0-md5:	e1fd924b9bf953c0b28c49bdfe117d7a
URL:		https://pypi.org/project/calver/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
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

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
