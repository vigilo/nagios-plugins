%define module  nagios-plugins
%define name    vigilo-%{module}
%define version 1.6
%define release %mkrel 9%{?svn}
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
Requires:   srvadmin-omacore
Requires:   perl
Requires:   vigilo-nagios-plugins-bgp
Requires:   vigilo-nagios-plugins-cpu
Requires:   vigilo-nagios-plugins-dell_openmanage
Requires:   vigilo-nagios-plugins-hp
Requires:   vigilo-nagios-plugins-https_via_proxy
Requires:   vigilo-nagios-plugins-ipmi
Requires:   vigilo-nagios-plugins-megaraid
Requires:   vigilo-nagios-plugins-ospf
Requires:   vigilo-nagios-plugins-ospf2
Requires:   vigilo-nagios-plugins-postgres
Requires:   vigilo-nagios-plugins-raid
Requires:   vigilo-nagios-plugins-sysuptime
Requires:   vigilo-nagios-plugins-tape
Requires:   vigilo-nagios-plugins-udp_simple
Requires:   vigilo-nagios-plugins-vigiloservers
Requires:   vigilo-nagios-plugins-win_procs

# Rename from nagios-plugins-vigilo
Obsoletes:  nagios-plugins-vigilo < 1.6-2
Provides:   nagios-plugins-vigilo = %{version}-%{release}


%description
Additional Nagios plugins
Additionnal plugins for the Nagios supervision system
This application is part of the Vigilo Project <http://vigilo-project.org>


%package    -n vigilo-nagios-config
Summary:    Nagios configuration for Vigilo
Group:      System/Servers
Requires:   nagios

%description -n vigilo-nagios-config
This contains the Vigilo configuration for Nagios.
This package is part of the Vigilo Project <http://vigilo-project.org>

%package    -n vigilo-nrpe-config
Summary:    NRPE configuration for the Vigilo plugins
Group:      System/Servers
Requires:   nrpe

%description -n vigilo-nrpe-config
This contains the Vigilo configuration for the Nagios Remote Plugin Executor.
This package is part of the Vigilo Project <http://vigilo-project.org>

%package    hp
Summary:    Additionnal plugins for Nagios: HP hardware
#Requires:   hpasm
Requires:   net-snmp-utils
Group:      System/Servers
# Rename from nagios-plugins-vigilo-hp
Obsoletes:  nagios-plugins-vigilo-hp < 1.6-2
Provides:   nagios-plugins-vigilo-hp = %{version}-%{release}

%description hp
Additionnal Nagios plugins for HP hardware.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    bgp
Summary:    Additionnal plugins for Nagios: BGP routing
Group:      System/Servers

%description bgp
Additionnal Nagios plugin for BGP routing.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    cpu
Summary:    Additionnal plugins for Nagios: CPU check
Group:      System/Servers

%description cpu
Additionnal Nagios plugin for CPU checking.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    https_via_proxy
Summary:    Additionnal plugins for Nagios: HTTPS/Proxy
Group:      System/Servers
Requires:   curl

%description https_via_proxy
Additionnal Nagios plugin for HTTPS over proxy checking.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ipmi
Summary:    Additionnal plugins for Nagios: IPMI-enabled hardware
Group:      System/Servers
Requires:   ipmitool

%description ipmi
Additionnal Nagios plugin for IPMI-enabled hardware.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    megaraid
Summary:    Additionnal plugins for Nagios: LSI MegaRAID hardware
Group:      System/Servers
Requires:   megacli

%description megaraid
Additionnal Nagios plugin for LSI MegaRAID hardware.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ospf2
Summary:    Additionnal plugins for Nagios: OSPF2 routing
Group:      System/Servers

%description ospf2
Additionnal Nagios plugin for OSPF2 routing.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ospf
Summary:    Additionnal plugins for Nagios: OSPF routing
Group:      System/Servers

%description ospf
Additionnal Nagios plugin for OSPF2 routing.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    raid
Summary:    Additionnal plugins for Nagios: software RAID on Linux
Group:      System/Servers
Requires:   sudo

%description raid
Additionnal Nagios plugin for software RAID on Linux.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    sysuptime
Summary:    Additionnal plugins for Nagios: system uptime
Group:      System/Servers

%description sysuptime
Additionnal Nagios plugin for system uptime.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    udp_simple
Summary:    Additionnal plugins for Nagios: UDP-based servers
Group:      System/Servers
Requires:   sudo
Requires:   nmap

%description udp_simple
Additionnal Nagios plugins for UDP-based server.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    win_procs
Summary:    Additionnal plugins for Nagios: MS Windows processes
Group:      System/Servers

%description win_procs
Additionnal Nagios Plugins
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    tape
Summary:    Additionnal plugins for Nagios: tape backups
Group:      System/Servers
Requires:   smartmontools
Requires:   mtx
Requires:   sudo

%description tape
Additionnal Nagios plugin for tape backups.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    dell_openmanage
Summary:    Additionnal plugins for Nagios: Dell hardware
Group:      System/Servers
Requires:   srvadmin-omacore
Requires:   perl
Requires:   sudo

%description dell_openmanage
Additionnal Nagios plugin for Dell hardware.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    toip
Summary:    Additionnal plugins for Nagios: ToIP
Group:      System/Servers
Requires:   python

%description toip
Additionnal Nagios plugins for IPBX and other ToIP appliances.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    nagios
Summary:    Additionnal plugins for Nagios: Nagios itself
Group:      System/Servers
Requires:   python

%description nagios
Additionnal Nagios plugin to check the health of a Nagios server.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    rrdcached
Summary:    Additionnal plugins for Nagios: RRDcached
Group:      System/Servers
Requires:   python

%description rrdcached
Additionnal Nagios plugin to check the RRDtool caching daemon.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    postgres
Summary:    Additionnal plugins for Nagios: PostgreSQL
Group:      System/Servers
Requires:   python

%description postgres
Additionnal Nagios plugin to check a PostgreSQL database.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    vigiloservers
Summary:    Additionnal plugins for Nagios: Vigilo servers
Group:      System/Servers
Requires:   python

%description vigiloservers
Additionnal Nagios plugin to check whether a manual VigiConf redeployment is needed or not.
This application is part of the Vigilo Project <http://vigilo-project.org>


%prep
%setup -q -n %{module}

%build

%install
rm -rf $RPM_BUILD_ROOT
make install \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    DESTDIR=$RPM_BUILD_ROOT \
    LIBDIR=%{_libdir} \
    BINDIR=%{_bindir} \
    PYTHON=%{_bindir}/python
# pas nécessaire sur cea
#rm -f $RPM_BUILD_ROOT%_libdir/nagios/plugins/check_tacacs


%clean
rm -rf $RPM_BUILD_ROOT


%post -n vigilo-nrpe-config
#%%_post_service nrpe
/sbin/service nrpe condrestart > /dev/null 2>&1 || :

%post tape
if ! grep -qs "^# NRPE Tape" /etc/sudoers; then
    echo "" >> /etc/sudoers
    echo "# NRPE Tape" >> /etc/sudoers
    echo "Cmnd_Alias CHECK_TAPE = \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_tape" >> /etc/sudoers
    echo "nagios ALL=(ALL) NOPASSWD: CHECK_TAPE" >> /etc/sudoers
fi


%post dell_openmanage
if ! grep -qs "^# NRPE Dell openmanage" /etc/sudoers; then
    echo "" >> /etc/sudoers
    echo "# NRPE Dell openmanage" >> /etc/sudoers
    echo "Cmnd_Alias CHECK_DELL_HARDWARE = \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_dell_openmanage_raid.pl, \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_dell_openmanage_chassis.pl, \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_dell_openmanage_fans.pl, \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_dell_openmanage_general.pl, \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_dell_openmanage_powersupplies.pl, \ " >> /etc/sudoers
    echo "    /usr/lib64/nagios/plugins/check_dell_openmanage_temperature.pl" >> /etc/sudoers
    echo "nagios ALL=(ALL) NOPASSWD: CHECK_DELL_HARDWARE" >> /etc/sudoers
fi

#%files
#%defattr(644,root,root,755)
#%doc COPYING

%files -n vigilo-nagios-config
%defattr(644,root,root,755)
%doc COPYING
%config(noreplace) %{_sysconfdir}/nagios/vigilo.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/vigilo-commands.cfg

%files -n vigilo-nrpe-config
%defattr(644,root,root,755)
%doc COPYING
%config(noreplace) %{_sysconfdir}/nrpe.d/*.cfg

%files hp
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %_libdir/nagios/plugins/check_hp_fan
%attr(755,root,root) %_libdir/nagios/plugins/check_hp_power_supplies
%attr(755,root,root) %_libdir/nagios/plugins/check_hp_raid
%attr(755,root,root) %_libdir/nagios/plugins/check_hp_temp
%attr(755,root,root) %_libdir/nagios/plugins/check_snmp_hp_power_supplies
%attr(755,root,root) %_libdir/nagios/plugins/check_snmp_hp_raid
%attr(755,root,root) %_libdir/nagios/plugins/check_snmp_hp_temp
%attr(755,root,root) %_libdir/nagios/plugins/check_snmp_hp_fan

%files bgp
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_bgp

%files cpu
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_cpu
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_cpu.cfg

%files https_via_proxy
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_https_via_proxy
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_proxy_ssl.cfg

%files ipmi
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_ipmi
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_ipmi.cfg

%files megaraid
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_megaraid
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_megaraid.cfg

%files ospf2
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_ospf2

%files ospf
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_ospf

%files raid
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_raid

%files sysuptime
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_sysuptime

%files udp_simple
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_udp_simple
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_udp_simple.cfg

%files win_procs
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_win_procs

%files tape
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_tape

%files dell_openmanage
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_dell_openmanage*

%files toip
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_mevo_capacity.py*
%attr(755,root,root) %_libdir/nagios/plugins/check_ip_phones_or_ccda.py*
%attr(755,root,root) %_libdir/nagios/plugins/check_free_position_ua_card.py*
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_mevo_capacity.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_free_position_ua_card.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_ip_phones_or_ccda.cfg

%files nagios
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_nagiostats_vigilo

%files rrdcached
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_rrdcached
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_rrdcached.cfg

%files postgres
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_postgres

%files vigiloservers
%defattr(644,root,root,755)
%attr(755,root,root) %_libdir/nagios/plugins/check_vigiloservers


%changelog
* Mon Feb 21 2011 Vincent QUEMENER <vincent.quemener@c-s.fr>
- added a plugin to check PostgreSQL databases ;
- added a plugin to check whether a manual VigiConf redeployment is necessary or not.

* Mon Nov 08 2010  BURGUIERE Thomas <thomas.burguiere@c-s.fr>
- make vigilo-nagios-plugins a meta package

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
