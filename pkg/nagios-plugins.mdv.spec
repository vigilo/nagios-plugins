%define module  nagios-plugins
%define name    vigilo-%{module}
%define version 1.6
%define release 4

Name:       %{name}
Summary:    Additional Nagios plugins
Version:    %{version}
Release:    %{release}
Source0:    %{module}.tar.bz2
URL:        http://www.projet-vigilo.org
Group:      System/Servers
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-build
License:    GPLv2
#Buildarch:  noarch
Requires:   net-snmp-utils
Requires:   sudo
Requires:   nmap
#Requires:   openipmi
#Requires:   ipmitool
Requires:   nagios-check_tcp
Requires:   nagios-check_ntp

# Rename from nagios-plugins-vigilo
Obsoletes:  nagios-plugins-vigilo < 1.6-2
Provides:   nagios-plugins-vigilo = %{version}-%{release}


%description
Additional Nagios plugins
Additionnal plugins for the Nagios supervision system
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    hp    
Summary:    Additionnal plugins for HP servers
#Requires:   hpasm
Requires:   net-snmp-utils
Group:      System/Servers
# Rename from nagios-plugins-vigilo-hp
Obsoletes:  nagios-plugins-vigilo-hp < 1.6-2
Provides:   nagios-plugins-vigilo-hp = %{version}-%{release}

%description hp
Additionnal Nagios Plugins
Additionnal plugins for HP servers
This application is part of the Vigilo Project <http://vigilo-project.org>

%prep
%setup -q -n %{module}

%build

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir} BINDIR=%{_bindir}
# pas nécessaire sur cea
#rm -f $RPM_BUILD_ROOT%_libdir/nagios/plugins/check_tacacs


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc COPYING nrpe_local.cfg
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/*
%{_libdir}/nagios/plugins/check_bgp
%{_libdir}/nagios/plugins/check_cpu
%{_libdir}/nagios/plugins/check_https_via_proxy
%{_libdir}/nagios/plugins/check_ipmi
%{_libdir}/nagios/plugins/check_megaraid
%{_libdir}/nagios/plugins/check_ospf
%{_libdir}/nagios/plugins/check_ospf2
%{_libdir}/nagios/plugins/check_raid
%{_libdir}/nagios/plugins/check_rrd
#%{_libdir}/nagios/plugins/check_tacacs
%{_libdir}/nagios/plugins/check_udp_simple
%{_libdir}/nagios/plugins/check_win_procs
%{_libdir}/nagios/plugins/check_sysuptime

%files hp
%defattr(-,root,root)
%doc COPYING
%_libdir/nagios/plugins/check_hp_fan
%_libdir/nagios/plugins/check_hp_power_supplies
%_libdir/nagios/plugins/check_hp_raid
%_libdir/nagios/plugins/check_hp_temp
%_libdir/nagios/plugins/check_snmp_hp_power_supplies
%_libdir/nagios/plugins/check_snmp_hp_raid
%_libdir/nagios/plugins/check_snmp_hp_temp
%_libdir/nagios/plugins/check_snmp_hp_fan


%changelog
* Wed Jan 13 2010  Thomas Burguiere <thomas.burguiere@c-s.fr>
- modification for relocalisation

* Tue Dec 22 2009 Thomas Burguiere <thomas.burguiere@c-s.fr>
- adaptation Redhat 5.2

* Thu Jul 30 2009 Aurelien Bompard <aurelien.bompard@c-s.fr>
- rename

* Fri Feb 27 2009  Thomas Burguiere <thomas.burguiere@c-s.fr>
- first creation of the RPM from debian archive

