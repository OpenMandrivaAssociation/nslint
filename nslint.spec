Summary:	A DNS lint checker
Name:		nslint
Version:	2.1a6
Release:	10
License:	BSD
Group:		Networking/Other
Source:		ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.bz2
Patch:		%{name}-owner.patch

%description
Perform consistency checks on DNS files.

%prep
%setup -q
%patch -p1

%build
%configure
%make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man8
%makeinstall_std install-man
chmod 0755 %{buildroot}%{_bindir}/%{name}

%files
%doc README CHANGES
%{_bindir}/%{name}
%{_mandir}/*/*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1a6-8mdv2011.0
+ Revision: 666624
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1a6-7mdv2011.0
+ Revision: 606826
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1a6-6mdv2010.1
+ Revision: 523443
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1a6-5mdv2010.0
+ Revision: 426255
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1a6-4mdv2009.0
+ Revision: 223348
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.1a6-3mdv2008.1
+ Revision: 153288
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Feb 24 2007 Giuseppe GhibÃ² <ghibo@mandriva.com> 2.1a6-1mdv2007.0
+ Revision: 125416
- Release: 2.1a8.
- Import nslint

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.1a3-6mdk
- Rebuild

* Sat Aug 06 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.1a3-5mdk
- Rebuilt.

