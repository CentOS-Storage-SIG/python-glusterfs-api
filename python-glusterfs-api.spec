# What's in a name ? :‑O
#
# * The source repo is named libgfapi-python
# * The python package is named gfapi
# * The RPM package is named python-glusterfs-api to be analogous to
#   glusterfs-api RPM which provides the libgfapi C library

%global python_package_name gfapi

%{!?python2_sitelib: %global python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:             python-glusterfs-api
Summary:          Python bindings for GlusterFS libgfapi
Version:          1.1
Release:          2%{?dist}
License:          GPLv2 or LGPLv3+
Group:            System Environment/Libraries
URL:              https://github.com/gluster/libgfapi-python
Source0:          https://files.pythonhosted.org/packages/source/g/gfapi/%{python_package_name}-%{version}.tar.gz

BuildArch:        noarch

%global _description \
libgfapi is a library that allows applications to natively access\
GlusterFS volumes. This package contains python bindings to libgfapi.\
\
See http://libgfapi-python.rtfd.io/ for more details.

%description %{_description}

%package -n python2-glusterfs-api
Summary:          Python2 bindings for GlusterFS libgfapi
%{?python_provide:%python_provide python2-glusterfs-api}
%if ( 0%{?rhel} )
BuildRequires:    python-devel
BuildRequires:    python-setuptools
%if ( 0%{?rhel} < 7 )
%{!?__python2: %global __python2 /usr/bin/python2}
%endif
%else
BuildRequires:    python2-devel
BuildRequires:    python2-setuptools
%endif
# Requires libgfapi.so
Requires:         glusterfs-api >= 3.7.0
# Requires gluster/__init__.py
Requires:         python-gluster >= 3.7.0

%description -n python2-glusterfs-api %{_description}

%prep
%setup -q -n %{python_package_name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-glusterfs-api
%{!?_licensedir:%global license %%doc}
%doc README.rst
%license COPYING-GPLV2 COPYING-LGPLV3
%{python2_sitelib}/*
# As weird as it may seem, excluding __init__.py[co] is intentional as
# it is provided by python-gluster package which is a dependency.
%exclude %{python2_sitelib}/gluster/__init__*

%changelog
* Thu Jan 19 2017 Kaleb S. KEITHLEY <kkeithle[at]redhat.com>
- %__python2, %python2_sitelib, and %license globals for EL6

* Thu Jan 19 2017 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 1.1-2
- Initial import plus RHEL feature test for python-devel

* Tue Aug 9 2016 Prashanth Pai <ppai@redhat.com> - 1.1-1
- Update spec file

* Wed May 20 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-1
- Change Package name to python-glusterfs-api instead of python-gluster-gfapi.

* Mon May 18 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0beta3
- Added license macro.

* Wed Apr 15 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0beta2
- Added detailed description for this package.

* Tue Apr 14 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0beta1
- Renamed glusterfs module to gluster

* Wed Feb 11 2015 Humble Chirammal <hchiramm@redhat.com> - 1.0.0-0
- Introducing spec file.
