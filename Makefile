NAME = nagios-plugins
NEHDIR = $(NPLUGDIR)/eventhandlers
PYTHON = /usr/bin/python

SUBSTFILES = \
	$(basename $(wildcard conf/*.in)) \
	$(basename $(wildcard plugins/*.in)) \
	nrpe.cfg nagios-plugin-commands.cfg \
	vigilo.cfg vigilo-commands.cfg

all: $(SUBSTFILES)

include buildenv/Makefile.common.nopython


conf/%: conf/%.in
	sed -e 's,@PLUGINDIR@,$(NPLUGDIR),g' $^ > $@

plugins/%: plugins/%.in
	sed -e 's,@PLUGINDIR@,$(NPLUGDIR),g' -e 's,@PYTHON@,$(PYTHON),g' $^ > $@

%.cfg: %.cfg.in
	sed -e 's,@PLUGINDIR@,$(NPLUGDIR),g' \
	    -e 's,@BINDIR@,$(BINDIR),g' \
	    -e 's,@NEHDIR@,$(NEHDIR),g' \
	    -e 's,@SYSCONFDIR@,$(SYSCONFDIR),g' $^ > $@


install: $(SUBSTFILES)
	mkdir -p $(DESTDIR)$(NPLUGDIR)/
	mkdir -p $(DESTDIR)$(NPCONFDIR)/
	mkdir -p $(DESTDIR)$(NRPECONFDIR)/
	mkdir -p $(DESTDIR)$(NCONFDIR)/vigilo.d/
	mkdir -p $(DESTDIR)$(NEHDIR)/
	mkdir -p $(DESTDIR)/etc/cron.daily/
	install -p -m 644 nrpe.cfg $(DESTDIR)$(NRPECONFDIR)/vigilo.cfg
	install -p -m 644 vigilo.cfg $(DESTDIR)$(NCONFDIR)/vigilo.d/vigilo.cfg
	install -p -m 644 vigilo-commands.cfg $(DESTDIR)$(NPCONFDIR)/vigilo-commands.cfg
	# Installation des configurations génériques.
	install -p -m 644 nrpe.cfg $(DESTDIR)$(NRPECONFDIR)/vigilo.cfg
	install -p -m 644 vigilo.cfg $(DESTDIR)$(NCONFDIR)/vigilo.d/
	install -p -m 644 vigilo-commands.cfg $(DESTDIR)$(NPCONFDIR)/
	# Installation des handlers.
	install -p -m 755 handlers/*.pl $(DESTDIR)$(NEHDIR)/
	# Installations des tâches périodiques (cron).
	install -p -m 755 nagios-restart.sh $(DESTDIR)/etc/cron.daily/vigilo-nagios-restart.sh
	# Installation des plugins Nagios.
	install -p -m 755 plugins/check_* $(DESTDIR)$(NPLUGDIR)/
	install -p -m 755 plugins/utils_vigilo.py $(DESTDIR)$(NPLUGDIR)/
	rm -f $(DESTDIR)$(NPLUGDIR)/*.in
	# Installation des configurations des plugins Nagios.
	install -p -m 644 conf/check_cpu.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_ipmi.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_megaraid.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_proxy_ssl.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_udp_simple.cfg $(DESTDIR)$(NPCONFDIR)/
ifeq ($(DISTRO),redhat)
	# Sur Red Hat, les plugins ne sont pas fournis avec leur configuration.
	install -p -m 644 nagios-plugin-commands.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_tcp.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_dummy.cfg $(DESTDIR)$(NPCONFDIR)/
	install -p -m 644 conf/check_icmp.cfg $(DESTDIR)$(NPCONFDIR)/
endif
ifeq ($(DISTRO),debian)
	# Sur Debian, check_icmp est fourni sans son fichier de configuration.
	install -p -m 644 conf/check_icmp.cfg $(DESTDIR)$(NPCONFDIR)/
endif


clean: clean_common
	rm -f $(SUBSTFILES)



.PHONY: all install clean
