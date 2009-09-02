%define name nslint
%define version 2.1a6

Summary: A DNS lint checker
Name: %{name}
Version: %{version}
Release: %mkrel 5
Source: ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.bz2
Patch: %{name}-owner.patch
License: BSD
Group: Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Perform consistency checks on DNS files.

%prep
%setup -q
%patch -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_mandir}/man8
%makeinstall_std install-man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*


