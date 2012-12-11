#%%define runuser onioncatuser
# TODO add a initscript

Name:		onioncat
Version:	0.1.13
Release:	%mkrel 3
Summary:	Anonymizing VPN over Tor
URL:		http://www.cypherpunk.at/onioncat/
Group:		Networking/Other
License:	GPLv3
Source0:	http://www.cypherpunk.at/ocat/download/Source/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OnionCat creates a transparent IP layer on top of Tor's hidden services.
It transmits any kind of IP-based data transparently through the Tor network 
on a location hidden basis. You can think of it as a point-to-multipoint VPN 
between hidden services.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}

%makeinstall
rm -Rf $RPM_BUILD_ROOT/usr/include/
rm -Rf $RPM_BUILD_ROOT/usr/share/doc/*

%clean
rm -rf ${RPM_BUILD_ROOT}

#%pre
#%_pre_useradd %{runuser} / /bin/false
#
#%postun
#%_postun_userdel %{runuser}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.1.13-3mdv2011.0
+ Revision: 664794
- rebuild old package

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sat Jun 13 2009 Michael Scherer <misc@mandriva.org> 0.1.13-1mdv2010.0
+ Revision: 385708
- new version
- new version

* Fri Feb 06 2009 Michael Scherer <misc@mandriva.org> 0.1.10-1mdv2009.1
+ Revision: 337999
- new version

* Mon Dec 29 2008 Michael Scherer <misc@mandriva.org> 0.1.8-1mdv2009.1
+ Revision: 321265
- import onioncat


