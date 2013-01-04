NAME = nagios-plugins
NEHDIR = $(NPLUGDIR)/eventhandlers
PYTHON = /usr/bin/python

SUBSTFILES = \
	$(basename $(wildcard conf/*.in)) \
	$(basename $(wildcard plugins/*.in)) \
	nrpe.cfg nagios-plugin-commands.cfg

all: $(SUBSTFILES)

include buildenv/Makefile.common.nopython


conf/%: conf/%.in
	sed -e 's,@PLUGINDIR@,$(NPLUGDIR),g' $^ > $@
	#sed -e 's,@LIBDIR@,$(LIBDIR),g;s,@EVENTHANDLERDIR@,$(NEHDIR),g' $^ > $@

plugins/%: plugins/%.in
	sed -e 's,@PLUGINDIR@,$(NPLUGDIR),g' -e 's,@PYTHON@,$(PYTHON),g' $^ > $@

%.cfg: %.cfg.in
	sed -e 's,@PLUGINDIR@,$(NPLUGDIR),g;s,@BINDIR@,$(BINDIR),g;s,@SYSCONFDIR@,$(SYSCONFDIR),g' $^ > $@


install: $(SUBSTFILES)
	mkdir -p $(DESTDIR)$(NPLUGDIR)/
	install -p -m 755 plugins/check_* $(DESTDIR)$(NPLUGDIR)/
	rm -f $(DESTDIR)$(NPLUGDIR)/*.in
	mkdir -p $(DESTDIR)$(NPCONFDIR)/
	cp -p conf/*.cfg $(DESTDIR)$(NPCONFDIR)/
	mkdir -p $(DESTDIR)$(NRPECONFDIR)/
	mkdir -p $(DESTDIR)$(NCONFDIR)/vigilo.d/
	install -p -m 644 nrpe.cfg $(DESTDIR)$(NRPECONFDIR)/vigilo.cfg
	install -p -m 644 vigilo.cfg $(DESTDIR)$(NCONFDIR)/vigilo.d/vigilo.cfg
	install -p -m 644 vigilo-commands.cfg $(DESTDIR)$(NPCONFDIR)/vigilo-commands.cfg
	mkdir -p $(DESTDIR)$(NEHDIR)/
	install -p -m 755 handlers/*.pl $(DESTDIR)$(NEHDIR)/
	mkdir -p $(DESTDIR)/etc/cron.daily/
	install -p -m 755 nagios-restart.sh $(DESTDIR)/etc/cron.daily/vigilo-nagios-restart.sh
ifeq ($(DISTRO),redhat)
	# Sur Red Hat, les plugins ne sont pas fournis avec leur fichier de conf
	install -p -m 644 nagios-plugin-commands.cfg $(DESTDIR)$(NPCONFDIR)/nagios-plugin-commands.cfg
endif


clean: clean_common
	rm -f $(SUBSTFILES)



.PHONY: all install clean
