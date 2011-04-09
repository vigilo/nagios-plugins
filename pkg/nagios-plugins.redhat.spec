%define module  nagios-plugins
%define name    vigilo-%{module}
%define version 1.8
%define release 1%{?svn}%{?dist}
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
#Buildarch:  noarch  # On installe dans _libdir

Requires:   vigilo-nagios-plugins-cpu
Requires:   vigilo-nagios-plugins-https_via_proxy
Requires:   vigilo-nagios-plugins-ipmi
Requires:   vigilo-nagios-plugins-megaraid
Requires:   vigilo-nagios-plugins-raid
Requires:   vigilo-nagios-plugins-sysuptime
Requires:   vigilo-nagios-plugins-udp_simple


%description
Additional Nagios plugins
Additionnal plugins for the Nagios supervision system
This application is part of the Vigilo Project <http://vigilo-project.org>


%package    -n vigilo-nagios-config
Summary:    Nagios configuration for Vigilo
Group:      System/Servers
Requires:   nagios >= 3
Requires:   socat

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


%clean
rm -rf $RPM_BUILD_ROOT


%post -n vigilo-nrpe-config
/sbin/service nrpe condrestart > /dev/null 2>&1 || :


#%files
#%defattr(644,root,root,755)
#%doc COPYING

%files -n vigilo-nagios-config
%defattr(644,root,root,755)
%doc COPYING
%dir %{_sysconfdir}/nagios/vigilo.d
%config(noreplace) %{_sysconfdir}/nagios/vigilo.d/vigilo.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/vigilo-commands.cfg
# Sur Red Hat, les plugins ne sont pas fournis avec leur fichier de conf
%config(noreplace) %{_sysconfdir}/nagios/%{nagios_plugins_cfg}/nagios-plugin-commands.cfg

%files -n vigilo-nrpe-config
%defattr(644,root,root,755)
%doc COPYING
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
* Sat Apr 09 2011 Aurelien Bompard <aurelien.bompard@c-s.fr> 
- initial package
