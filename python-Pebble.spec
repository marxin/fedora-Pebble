#
# spec file for package python
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global modname Pebble

Name:           python3-%{modname}
Version:        4.5.1
Release:        0
Summary:        Threading and multiprocessing eye-candy for Python
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/noxdafox/pebble
Source:         https://files.pythonhosted.org/packages/source/P/Pebble/Pebble-%{version}.tar.gz
BuildArch:      noarch

%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.

%prep
%autosetup -n %{modname}-%{version} -Sgit

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
