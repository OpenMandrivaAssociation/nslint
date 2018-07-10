Summary:	A DNS lint checker
Name:		nslint
Version:	2.1a6
Release:	18
License:	BSD
Group:		Networking/Other
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.bz2
Patch0:		%{name}-owner.patch

%description
Perform consistency checks on DNS files.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man8
%makeinstall_std install-man
chmod 0755 %{buildroot}%{_bindir}/%{name}

%files
%doc README CHANGES
%{_bindir}/%{name}
%{_mandir}/*/*

