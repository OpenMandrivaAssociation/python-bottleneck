%define module bottleneck
%define oname Bottleneck
%bcond tests 1
%bcond docs 1

Name:		python-bottleneck
Summary:	Fast NumPy array functions written in Cython
Version:	1.6.0
Release:	1
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.python.org/pypi/Bottleneck
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix doc build with Sphinx 6+: https://github.com/pydata/bottleneck/pull/432/
Patch0:	https://github.com/pydata/bottleneck/pull/432/commits/00f39d74f8788ad5aa0dbfe34e7b66b38d0c63d1.patch

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(versioneer)
%if %{with docs}
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(numpydoc)
%endif
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%if %{with docs}
%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch

%description doc
Documentation files for %{name}.
%endif

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info
# Remove the contributors extensions which wont work as we don't have a repo.
sed -i /contributors/d doc/source/conf.py

%build -p
export CFLAGS="%{optflags} -fno-strict-aliasing"
export LDFLAGS="%{ldflags} -lpython%{pyver} -lm"

%install -a
# install the buildroot docdir
install -dpm 755 %{buildroot}%{_docdir}/%{name}
# Use sphinx-build to build html docs into buildroot docdir,
# Doc generation requires the module to be installed in order to run successfully.
export READTHEDOCS=1
PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}" \
    sphinx-build -b html doc/source %{buildroot}%{_docdir}/%{name}
# remove .buildinfo and .doctrees
rm -rf %{buildroot}%{_docdir}/%{name}/{.buildinfo,.doctrees,.nojekyll}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pushd build/lib.linux-*
pytest bottleneck
popd
%endif

%files
%doc README.rst RELEASE.rst
%license LICENSE
%py_platsitedir/%{module}
%py_platsitedir/%{module}-%{version}.dist-info

%if %{with docs}
%files doc
%{_docdir}/%{name}
%endif
