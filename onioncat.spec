#%%define runuser onioncatuser
# TODO add a initscript

Name:		onioncat
Version:	0.1.13
Release:	%mkrel 2
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
