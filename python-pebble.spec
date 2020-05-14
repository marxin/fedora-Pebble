%global modname pebble

Name:           python-%{modname}
Version:        4.5.1
Release:        0
Summary:        Threading and multiprocessing eye-candy for Python
License:        LGPLv3
URL:            https://github.com/noxdafox/pebble
Source:         %{pypi_source Pebble}
BuildArch:      noarch

%global _description %{expand:
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description %_description

%prep
%autosetup -n %{modname}-%{version} -Sgit

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/pebble/
%{python3_sitelib}/Pebble-*.egg-info/

%changelog
* Wed May 13 2020 Martin Liška <mliska@suse.cz> - 4.5.1
- Initial Fedora package
