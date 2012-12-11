%define module_name hachoir-regex

Summary:	Regex manipulation Python library	
Name:		python-%{module_name}
Version:	1.0.5
Release:	%mkrel 1
Source0:	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://hachoir.org/wiki/hachoir-metadata
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
BuildRequires:	python-setuptools

%description
Regex manipulation Python library.

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%{py_puresitedir}/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 598270
- rebuild for py2.7

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 1.0.5-1mdv2010.1
+ Revision: 500604
- update to new version 1.0.5

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2010.0
+ Revision: 442166
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.3-1mdv2009.1
+ Revision: 320033
- rebuild with python 2.6
- clean spec
- new release 1.0.3

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 259623
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 247428
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.2-1mdv2008.1
+ Revision: 136450
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 52871
- Import python-hachoir-regex

