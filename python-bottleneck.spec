%define tarname	Bottleneck
%define name	python-bottleneck
%define version 0.5.0
%define release %mkrel 1

Summary:	Fast NumPy array functions written in Cython
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/B/%{tarname}/%{tarname}-%{version}.tar.gz
Source1:	sphinxext.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/Bottleneck
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-numpy
BuildRequires:	python-numpy-devel, python-devel, python-sphinx

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd doc
rm -rf sphinxext
tar zxf %SOURCE1
export PYTHONPATH=`dir -d ../build/lib* | head -1`
make html
find . -name .buildinfo -exec rm -f {} \;
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc LICENSE README.rst RELEASE.rst doc/build/html
