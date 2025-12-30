%define tarname	Bottleneck

Summary:	Fast NumPy array functions written in Cython
Name:		python-bottleneck
Version:	1.3.8
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/B/%{tarname}/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/Bottleneck
Requires:	python-numpy
BuildRequires:	python-numpy-devel
BuildRequires:	python-devel
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(lapack)

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%prep
%autosetup -p1 -n %{tarname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc LICENSE README.rst RELEASE.rst
%py_platsitedir/Bottleneck*
%py_platsitedir/bottleneck*
