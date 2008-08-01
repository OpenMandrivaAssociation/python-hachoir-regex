%define module_name hachoir-regex

Summary:    	Regex manipulation Python library	
Name: 		python-%{module_name}
Version: 	1.0.2
Release: 	%mkrel 4
Source0: 	%{module_name}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://hachoir.org/wiki/hachoir-metadata
BuildArch:  noarch
Requires:   python-hachoir-core
Requires:   python-hachoir-parser
BuildRequires: python-devel
%description
Regex manipulation Python library.

%prep
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %py_puresitedir/hachoir_regex
