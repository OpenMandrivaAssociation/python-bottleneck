%define tarname	Bottleneck

Summary:	Fast NumPy array functions written in Cython
Name:		python-bottleneck
Version:	0.6.0
Release:	2
Source0:	http://pypi.python.org/packages/source/B/%{tarname}/%{tarname}-%{version}.tar.gz
Source1:	sphinxext.tar.gz
Patch0:		lm-0.5.0.patch
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/Bottleneck
Requires:	python-numpy
BuildRequires:	python-numpy-devel
BuildRequires:	python-devel
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(lapack)

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p0

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
pushd doc
rm -rf sphinxext
tar zxf %SOURCE1
export PYTHONPATH=`dir -d ../build/lib* | head -1`
make html
find . -name .buildinfo -exec rm -f {} \;
popd

%files
%doc LICENSE README.rst RELEASE.rst doc/build/html
%py_platsitedir/Bottleneck*
%py_platsitedir/bottleneck*



%changelog
* Mon Jun 25 2012 Lev Givon <lev@mandriva.org> 0.6.0-1
+ Revision: 806814
- Update to 0.6.0.

* Fri Aug 05 2011 Lev Givon <lev@mandriva.org> 0.5.0-2
+ Revision: 693371
- Need -lm when building extensions.
- import python-bottleneck


