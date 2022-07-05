#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupytext
Version  : 1.14.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/f5/0f/85dc71282666bcb6e5cdb004d799efb161c489d6bdc573a43ac0a16dff91/jupytext-1.14.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/0f/85dc71282666bcb6e5cdb004d799efb161c489d6bdc573a43ac0a16dff91/jupytext-1.14.0.tar.gz
Summary  : Jupyter notebooks as Markdown documents, Julia, Python or R scripts
Group    : Development/Tools
License  : MIT
Requires: pypi-jupytext-bin = %{version}-%{release}
Requires: pypi-jupytext-data = %{version}-%{release}
Requires: pypi-jupytext-license = %{version}-%{release}
Requires: pypi-jupytext-python = %{version}-%{release}
Requires: pypi-jupytext-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-qmake
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(jupyterlab)
BuildRequires : pypi(markdown_it_py)
BuildRequires : pypi(mdit_py_plugins)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(toml)
BuildRequires : pypi(wheel)

%description
![](https://raw.githubusercontent.com/mwouts/jupytext/main/docs/logo_large.png)
![CI](https://github.com/mwouts/jupytext/workflows/CI/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/jupytext/badge/?version=latest)](https://jupytext.readthedocs.io/en/latest/?badge=latest)
[![codecov.io](https://codecov.io/github/mwouts/jupytext/coverage.svg?branch=main)](https://codecov.io/gh/mwouts/jupytext/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/mwouts/jupytext.svg)](https://lgtm.com/projects/g/mwouts/jupytext/context:python)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub language count](https://img.shields.io/github/languages/count/mwouts/jupytext)](docs/languages.md)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/jupytext.svg)](https://anaconda.org/conda-forge/jupytext)
[![Pypi](https://img.shields.io/pypi/v/jupytext.svg)](https://pypi.python.org/pypi/jupytext)
[![pyversions](https://img.shields.io/pypi/pyversions/jupytext.svg)](https://pypi.python.org/pypi/jupytext)
[![Binder:notebook](https://img.shields.io/badge/binder-notebook-0172B2.svg)](https://mybinder.org/v2/gh/mwouts/jupytext/main?filepath=demo)
[![Binder:lab](https://img.shields.io/badge/binder-jupyterlab-0172B2.svg)](https://mybinder.org/v2/gh/mwouts/jupytext/main?urlpath=lab/tree/demo/get_started.ipynb)
[![launch - renku](https://renkulab.io/renku-badge.svg)](https://renkulab.io/projects/best-practices/jupytext/sessions/new?autostart=1)
[![](https://img.shields.io/badge/YouTube-JupyterCon%202020-red.svg)](https://www.youtube.com/watch?v=SDYdeVfMh48)

%package bin
Summary: bin components for the pypi-jupytext package.
Group: Binaries
Requires: pypi-jupytext-data = %{version}-%{release}
Requires: pypi-jupytext-license = %{version}-%{release}

%description bin
bin components for the pypi-jupytext package.


%package data
Summary: data components for the pypi-jupytext package.
Group: Data

%description data
data components for the pypi-jupytext package.


%package license
Summary: license components for the pypi-jupytext package.
Group: Default

%description license
license components for the pypi-jupytext package.


%package python
Summary: python components for the pypi-jupytext package.
Group: Default
Requires: pypi-jupytext-python3 = %{version}-%{release}

%description python
python components for the pypi-jupytext package.


%package python3
Summary: python3 components for the pypi-jupytext package.
Group: Default
Requires: python3-core
Provides: pypi(jupytext)
Requires: pypi(markdown_it_py)
Requires: pypi(mdit_py_plugins)
Requires: pypi(nbformat)
Requires: pypi(pyyaml)
Requires: pypi(toml)

%description python3
python3 components for the pypi-jupytext package.


%prep
%setup -q -n jupytext-1.14.0
cd %{_builddir}/jupytext-1.14.0
pushd ..
cp -a jupytext-1.14.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657035810
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupytext
cp %{_builddir}/jupytext-1.14.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupytext/663d0f732d7e77407322ad0fc528b2c9e9c6bbc5
cp %{_builddir}/jupytext-1.14.0/packages/labextension/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupytext/6070800810da89afd1bfd1d32e40f9cb79531c0e
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_notebook_config.d/jupytext.json
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_server_config.d/jupytext.json
rm -f %{buildroot}*/usr/etc/jupyter/nbconfig/notebook.d/jupytext.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupytext

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbextensions/jupytext/README.md
/usr/share/jupyter/nbextensions/jupytext/index.js
/usr/share/jupyter/nbextensions/jupytext/jupytext.yml
/usr/share/jupyter/nbextensions/jupytext/jupytext_menu.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupytext/6070800810da89afd1bfd1d32e40f9cb79531c0e
/usr/share/package-licenses/pypi-jupytext/663d0f732d7e77407322ad0fc528b2c9e9c6bbc5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
