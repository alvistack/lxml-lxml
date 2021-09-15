%global debug_package %{nil}

Name: python-lxml
Epoch: 100
Version: 4.6.3
Release: 1%{?dist}
Summary: Pythonic binding for the C libraries libxml2 and libxslt
License: BSD-3-Clause
URL: https://github.com/lxml/lxml/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: zlib-devel

%description
lxml is the most feature-rich and easy-to-use library for processing XML
and HTML in the Python language. It's also very fast and memory
friendly, just so you know.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-lxml
Summary: Pythonic binding for the C libraries libxml2 and libxslt
Requires: python3
Provides: python%{python3_version_nodots}-lxml-devel = %{epoch}:%{version}-%{release}
Provides: python3-lxml = %{epoch}:%{version}-%{release}
Provides: python3dist(lxml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-lxml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(lxml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-lxml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(lxml) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-lxml
lxml is the most feature-rich and easy-to-use library for processing XML
and HTML in the Python language. It's also very fast and memory
friendly, just so you know.

%files -n python%{python3_version_nodots}-lxml
%license LICENSE.txt
%{python3_sitearch}/lxml*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-lxml
Summary: Pythonic binding for the C libraries libxml2 and libxslt
Requires: python3
Provides: python3-lxml-devel = %{epoch}:%{version}-%{release}
Provides: python3-lxml = %{epoch}:%{version}-%{release}
Provides: python3dist(lxml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-lxml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(lxml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-lxml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(lxml) = %{epoch}:%{version}-%{release}

%description -n python3-lxml
lxml is the most feature-rich and easy-to-use library for processing XML
and HTML in the Python language. It's also very fast and memory
friendly, just so you know.

%files -n python3-lxml
%license LICENSE.txt
%{python3_sitearch}/lxml*
%endif

%changelog
