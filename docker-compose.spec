#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-compose
Version  : 1.23.2
Release  : 15
URL      : https://github.com/docker/compose/archive/1.23.2.tar.gz
Source0  : https://github.com/docker/compose/archive/1.23.2.tar.gz
Summary  : Fast, isolated development environments using Docker
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-compose-bin = %{version}-%{release}
Requires: docker-compose-license = %{version}-%{release}
Requires: docker-compose-python = %{version}-%{release}
Requires: docker-compose-python3 = %{version}-%{release}
Requires: PySocks
Requires: PyYAML
Requires: backports.ssl_match_hostname
Requires: cached-property
Requires: certifi
Requires: chardet
Requires: docker
Requires: docker-py
Requires: docker-pycreds
Requires: dockerpty
Requires: docopt
Requires: enum34
Requires: functools32
Requires: idna
Requires: ipaddress
Requires: jsonschema
Requires: requests
Requires: six
Requires: texttable
Requires: urllib3
Requires: websocket_client
BuildRequires : PySocks
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cached-property
BuildRequires : certifi
BuildRequires : chardet
BuildRequires : docker
BuildRequires : docker-py
BuildRequires : docker-pycreds
BuildRequires : dockerpty
BuildRequires : docopt
BuildRequires : enum34
BuildRequires : functools32
BuildRequires : idna
BuildRequires : ipaddress
BuildRequires : jsonschema
BuildRequires : requests
BuildRequires : six
BuildRequires : texttable
BuildRequires : urllib3
BuildRequires : websocket_client
Patch1: 0001-Allow-requests-2.21.patch

%description
Docker Compose
==============
Compose is a tool for defining and running multi-container Docker applications.
With Compose, you use a Compose file to configure your application's services.
Then, using a single command, you create and start all the services
from your configuration. To learn more about all the features of Compose
see [the list of features](https://github.com/docker/docker.github.io/blob/master/compose/overview.md#features).

%package bin
Summary: bin components for the docker-compose package.
Group: Binaries
Requires: docker-compose-license = %{version}-%{release}

%description bin
bin components for the docker-compose package.


%package license
Summary: license components for the docker-compose package.
Group: Default

%description license
license components for the docker-compose package.


%package python
Summary: python components for the docker-compose package.
Group: Default
Requires: docker-compose-python3 = %{version}-%{release}

%description python
python components for the docker-compose package.


%package python3
Summary: python3 components for the docker-compose package.
Group: Default
Requires: python3-core

%description python3
python3 components for the docker-compose package.


%prep
%setup -q -n compose-1.23.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559918777
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/docker-compose
cp LICENSE %{buildroot}/usr/share/package-licenses/docker-compose/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docker-compose

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/docker-compose/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
