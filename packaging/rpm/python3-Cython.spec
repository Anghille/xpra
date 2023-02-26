%define _disable_source_fetch 0

Name:		python3-Cython
Version:	3.0.0b1
Release:	1%{?dist}
Summary:	A language for writing Python extension modules
Group:		Development/Tools
License:	Python
URL:		http://www.cython.org
Source0:    https://github.com/cython/cython/archive/refs/tags/%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   python3

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	gcc

%description
This is a development version of Pyrex, a language
for writing Python extension modules.

%prep
sha256=`sha256sum %{SOURCE0} | awk '{print $1}'`
if [ "${sha256}" != "bca121dbe96c88de9f2369d9d9231dd6b481cca486514421ed8252b4390eab5b" ]; then
	echo "invalid checksum for %{SOURCE0}"
	exit 1
fi
%setup -q -n cython-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python3_sitelib}/setuptools/tests

%clean
rm -rf %{buildroot}

#these tests take way too long:
#%check
#%{__python3} runtests.py -x numpy

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
%{_bindir}/cygdb
%{_bindir}/cython
%{_bindir}/cythonize
%doc *.txt Demos Tools

%changelog
* Wed Feb 22 2023 Antoine Martin <antoine@xpra.org> 0.29.33-1
- new upstream release

* Wed May 18 2022 Antoine Martin <antoine@xpra.org> 0.29.30-1
- new upstream release

* Fri Jan 28 2022 Antoine Martin <antoine@xpra.org> 0.29.27-1
- new upstream release

* Mon Dec 06 2021 Antoine Martin <antoine@xpra.org> 0.29.25-1
- new upstream release

* Thu Nov 04 2021 Antoine Martin <antoine@xpra.org> 0.29.24-1
- CentOS Stream 9 (temporary?) replacement package
