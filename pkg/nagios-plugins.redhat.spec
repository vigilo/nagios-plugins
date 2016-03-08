%define module  nagios-plugins
%define nagios_plugins_cfg plugins.d

Name:       vigilo-%{module}
Summary:    Additional Nagios plugins
Version:    @VERSION@
Release:    @RELEASE@%{?dist}
Source0:    %{name}-%{version}.tar.gz
URL:        http://www.projet-vigilo.org
Group:      Applications/System
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-build
License:    GPLv2
#Buildarch:  noarch  # On installe dans _libdir

Requires:   vigilo-nagios-plugins-cpu
Requires:   vigilo-nagios-plugins-https_via_proxy
Requires:   vigilo-nagios-plugins-ipmi
Requires:   vigilo-nagios-plugins-megaraid
Requires:   vigilo-nagios-plugins-raid
Requires:   vigilo-nagios-plugins-sysuptime
Requires:   vigilo-nagios-plugins-udp_simple
# sudo est requis par la tâche cron de redémarrage de Nagios
Requires:   sudo


%description
Additional Nagios plugins
Additionnal plugins for the Nagios supervision system
This application is part of the Vigilo Project <http://vigilo-project.org>


%package    -n vigilo-nagios-config
Summary:    Nagios configuration for Vigilo
Group:      Applications/System
Requires:   nagios >= 3
Requires:   nagios-plugins-icmp

%description -n vigilo-nagios-config
This contains the Vigilo configuration for Nagios.
This package is part of the Vigilo Project <http://vigilo-project.org>

%package    -n vigilo-nrpe-config
Summary:    NRPE configuration for the Vigilo plugins
Group:      Applications/System
Requires:   nrpe

%description -n vigilo-nrpe-config
This contains the Vigilo configuration for the Nagios Remote Plugin Executor.
This package is part of the Vigilo Project <http://vigilo-project.org>

%package    cpu
Summary:    Additionnal plugins for Nagios: CPU check
Group:      Applications/System

%description cpu
Additionnal Nagios plugin for CPU checking.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    https_via_proxy
Summary:    Additionnal plugins for Nagios: HTTPS/Proxy
Group:      Applications/System
Requires:   curl

%description https_via_proxy
Additionnal Nagios plugin for HTTPS over proxy checking.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    ipmi
Summary:    Additionnal plugins for Nagios: IPMI-enabled hardware
Group:      Applications/System
Requires:   ipmitool

%description ipmi
Additionnal Nagios plugin for IPMI-enabled hardware.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    megaraid
Summary:    Additionnal plugins for Nagios: LSI MegaRAID hardware
Group:      Applications/System
Requires:   megacli

%description megaraid
Additionnal Nagios plugin for LSI MegaRAID hardware.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    raid
Summary:    Additionnal plugins for Nagios: software RAID on Linux
Group:      Applications/System
Requires:   sudo

%description raid
Additionnal Nagios plugin for software RAID on Linux.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    sysuptime
Summary:    Additionnal plugins for Nagios: system uptime
Group:      Applications/System

%description sysuptime
Additionnal Nagios plugin for system uptime.
This application is part of the Vigilo Project <http://vigilo-project.org>

%package    udp_simple
Summary:    Additionnal plugins for Nagios: UDP-based servers
Group:      Applications/System
Requires:   sudo
Requires:   nmap

%description udp_simple
Additionnal Nagios plugins for UDP-based server.
This application is part of the Vigilo Project <http://vigilo-project.org>


%prep
%setup -q

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


%clean
rm -rf $RPM_BUILD_ROOT


%post -n vigilo-nrpe-config
/sbin/service nrpe condrestart > /dev/null 2>&1 || :


%files -n vigilo-nagios-config
%defattr(644,root,root,755)
%doc COPYING.txt README.txt
%dir %{_sysconfdir}/nagios/vigilo.d
%config(noreplace) %{_sysconfdir}/nagios/vigilo.d/vigilo.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/vigilo-commands.cfg
%attr(755,root,root) %{_libdir}/nagios/plugins/eventhandlers/nagios2vigilo.pl
%attr(644,root,root) %{_libdir}/nagios/plugins/utils_vigilo.py*
%attr(755,root,root) /etc/cron.daily/*.sh
# Sur Red Hat, les plugins ne sont pas fournis avec leur fichier de conf
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/nagios-plugin-commands.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_dummy.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_icmp.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/check_tcp.cfg

%files -n vigilo-nrpe-config
%defattr(644,root,root,755)
%doc COPYING.txt README.txt
%config(noreplace) %{_sysconfdir}/nrpe.d/*.cfg

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


%changelog
* Mon Apr 11 2016 Francois Poirotte <francois.poirotte@c-s.fr>
- Fix rpmlint errors on RHEL 7

* Sat Apr 09 2011 Aurelien Bompard <aurelien.bompard@c-s.fr>
- initial package
