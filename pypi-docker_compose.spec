#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docker_compose
Version  : 1.29.2
Release  : 48
URL      : https://files.pythonhosted.org/packages/1f/6a/f4703077123ad0c90026985cb9780c0703922c2a5451ab93fb63511d915a/docker-compose-1.29.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/6a/f4703077123ad0c90026985cb9780c0703922c2a5451ab93fb63511d915a/docker-compose-1.29.2.tar.gz
Summary  : Multi-container orchestration for Docker
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-docker_compose-bin = %{version}-%{release}
Requires: pypi-docker_compose-license = %{version}-%{release}
Requires: pypi-docker_compose-python = %{version}-%{release}
Requires: pypi-docker_compose-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cached_property)
BuildRequires : pypi(certifi)
BuildRequires : pypi(chardet)
BuildRequires : pypi(colorama)
BuildRequires : pypi(distro)
BuildRequires : pypi(docker)
BuildRequires : pypi(docker_pycreds)
BuildRequires : pypi(dockerpty)
BuildRequires : pypi(docopt)
BuildRequires : pypi(idna)
BuildRequires : pypi(ipaddress)
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pysocks)
BuildRequires : pypi(python_dotenv)
BuildRequires : pypi(pywin32)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(texttable)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(websocket_client)
Patch1: 0001-Remove-upper-bound-pin-on-websocket-client.patch

%description
==============

%package bin
Summary: bin components for the pypi-docker_compose package.
Group: Binaries
Requires: pypi-docker_compose-license = %{version}-%{release}

%description bin
bin components for the pypi-docker_compose package.


%package license
Summary: license components for the pypi-docker_compose package.
Group: Default

%description license
license components for the pypi-docker_compose package.


%package python
Summary: python components for the pypi-docker_compose package.
Group: Default
Requires: pypi-docker_compose-python3 = %{version}-%{release}

%description python
python components for the pypi-docker_compose package.


%package python3
Summary: python3 components for the pypi-docker_compose package.
Group: Default
Requires: python3-core
Provides: pypi(docker_compose)
Requires: pypi(distro)
Requires: pypi(docker)
Requires: pypi(dockerpty)
Requires: pypi(docopt)
Requires: pypi(jsonschema)
Requires: pypi(python_dotenv)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(texttable)
Requires: pypi(websocket_client)

%description python3
python3 components for the pypi-docker_compose package.


%prep
%setup -q -n docker-compose-1.29.2
cd %{_builddir}/docker-compose-1.29.2
%patch1 -p1
pushd ..
cp -a docker-compose-1.29.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655408880
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . PyYAML
pypi-dep-fix.py . jsonschema
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . PyYAML
pypi-dep-fix.py . jsonschema
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docker_compose
cp %{_builddir}/docker-compose-1.29.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-docker_compose/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} PyYAML
pypi-dep-fix.py %{buildroot} jsonschema
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docker-compose

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-docker_compose/8ff574408142cd6bbb2a1b83302de24cb7b35e8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
