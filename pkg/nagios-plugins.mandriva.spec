%define module  nagios-plugins
%define name    vigilo-%{module}
%define version 1.6
%define release %mkrel 7%{?svn}
%define nagios_plugins_cfg plugins.d/


Name:       %{name}
Summary:    Additional Nagios plugins
Version:    %{version}
Release:    %{release}
Source0:    %{module}.tar.bz2
URL:        http://www.projet-vigilo.org
Group:      System/Servers
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-build
License:    GPLv2
Buildarch:  noarch
###############################
#Requires:   net-snmp-utils
Requires:   sudo
Requires:   nmap
Requires:   ipmitool
Requires:   curl
Requires:   smartmontools
Requires:   mtx

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

%package    bgp
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description bgp
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    cpu
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description cpu
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    https_via_proxy
Summary:    Additionnal plugins for nagios
Group:      System/Servers
Requires:   curl

%description https_via_proxy
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ipmi
Summary:    Additionnal plugins for nagios
Group:      System/Servers
Requires:   ipmitool

%description ipmi
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    megaraid
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description megaraid
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ospf2
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description ospf2
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ospf
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description ospf
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    raid
Summary:    Additionnal plugins for nagios
Group:      System/Servers
Requires:   sudo

%description raid
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    rrd
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description rrd
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    sysuptime
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description sysuptime
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    udp_simple
Summary:    Additionnal plugins for nagios
Group:      System/Servers
Requires:   sudo
Requires:   nmap

%description udp_simple
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    win_procs
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description win_procs
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    tape
Summary:    Additionnal plugins for nagios
Group:      System/Servers
Requires:   smartmontools
Requires:   mtx

%description tape
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    dell_openmanage
Summary:    Additionnal plugins for nagios
Group:      System/Servers

%description dell_openmanage
Additionnal Nagios Plugins
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
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/*
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

%files bgp
%defattr(-,root,root)
%_libdir/nagios/plugins/check_bgp

%files cpu
%defattr(-,root,root)
%_libdir/nagios/plugins/check_cpu
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_cpu.cfg

%files https_via_proxy
%defattr(-,root,root)
%_libdir/nagios/plugins/check_https_via_proxy
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_proxy_ssl.cfg

%files ipmi
%defattr(-,root,root)
%_libdir/nagios/plugins/check_ipmi
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_ipmi.cfg

%files megaraid
%defattr(-,root,root)
%_libdir/nagios/plugins/check_megaraid
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_megaraid.cfg

%files ospf2
%defattr(-,root,root)
%_libdir/nagios/plugins/check_ospf2

%files ospf
%defattr(-,root,root)
%_libdir/nagios/plugins/check_ospf

%files raid
%defattr(-,root,root)
%_libdir/nagios/plugins/check_raid

%files rrd
%defattr(-,root,root)
%_libdir/nagios/plugins/check_rrd
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_rrd.cfg

%files sysuptime
%defattr(-,root,root)
%_libdir/nagios/plugins/check_sysuptime

%files udp_simple
%defattr(-,root,root)
%_libdir/nagios/plugins/check_udp_simple
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_udp_simple.cfg

%files win_procs
%defattr(-,root,root)
%_libdir/nagios/plugins/check_win_procs

%files tape
%defattr(-,root,root)
%_libdir/nagios/plugins/check_tape

%files dell_openmanage
%defattr(-,root,root)
%_libdir/nagios/plugins/check_dell_openmanage*


%changelog
* Thu Aug 26 2010  BURGUIERE Thomas <thomas.burguiere@c-s.fr>
- add new plugins (openmanage for Dell, and for generic tape and tape changer)

* Tue Aug 24 2010  BURGUIERE Thomas <thomas.burguiere@c-s.fr>
- modification to have specific mandriva spec file

* Fri Aug 06 2010  Thomas Burguiere <thomas.burguiere@c-s.fr>
- modification to have one rpm per check

* Wed Jan 13 2010  Thomas Burguiere <thomas.burguiere@c-s.fr>
- modification for relocalisation

* Tue Dec 22 2009 Thomas Burguiere <thomas.burguiere@c-s.fr>
- adaptation Redhat 5.2

* Thu Jul 30 2009 Aurelien Bompard <aurelien.bompard@c-s.fr>
- rename

* Fri Feb 27 2009  Thomas Burguiere <thomas.burguiere@c-s.fr>
- first creation of the RPM from debian archive
