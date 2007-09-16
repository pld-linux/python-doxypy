#
# TODO:
# - make the documentation more good sounding
#
%define         _module         doxypy

Summary:	Input filter of python code for Doxygen
Summary(pl.UTF-8):Filtr wejściowy kodu pythonowego dla Doxygena.
Name:		python-%{_module}
Version:	0.2.2
Release:	0.1
License:	GPLv2
Group:		Development/Languages/Python
Source0:	http://code.foosel.net/files/%{_module}-%{version}.py
# Source0-md5:	284833a9b38acafc94cb2efc491a873e
URL:		http://code.foosel.org/doxypy
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Suggests:	doxygen
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Doxypy is an input filter for Doxygen. It preprocesses python files so
that docstrings of classes and functions are reformatted into Doxygen
conform documentation blocks. This makes it possible to use the
Doxygen/Javadoc syntax inside of docstrings when writing code
documentation and automatically generate API documentation out of it,
instead of being forced to use the non-native documentation blocks
over the standard docstrings or to document everything twice.

%description -l pl.UTF-8
Doxypy jest filtrem wejściowym dla Doxygena. Wstępnie przetwarza
pliki pythonowe w taki sposób, że łańcuchy dokumentujące klasy i
funkcje są sformatowane w bloki dokumentacyjne dostosowane do
Doxygena. To umożliwia używanie składni Doxygena/Javadoca w
łańcuchach dokumentujących przy pisaniu dokumentacji kodu i
automatyczne generowanie z tego dokumentacji API zamiast być
zmuszanym do wykorzystanie nienatywnych bloków dokumentacyjnych nad
standardowymi stringami dokumentującymi lub do pisania wszystkiego
dwa razy.

%prep
%setup -c -T -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{_module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{_module}
