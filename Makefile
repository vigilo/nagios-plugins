NAME = nagios-plugins
PREFIX = /usr
LIBDIR = $(PREFIX)/lib
PLUGINDIR = $(LIBDIR)/nagios/plugins
SYSCONFDIR = /etc

SUBSTFILES = \
	$(basename $(wildcard conf/*.in)) \
	$(basename $(wildcard plugins/*.in)) \
	nrpe_local.cfg

all: $(SUBSTFILES)

include buildenv/Makefile.common

ifeq ($(DISTRO),debian)
	CONFDIR = $(SYSCONFDIR)/nagios-plugins/config
else ifeq ($(DISTRO),mandriva)
	CONFDIR = $(SYSCONFDIR)/nagios/plugins.d
else ifeq ($(DISTRO),redhat)
	CONFDIR = $(SYSCONFDIR)/nagios/objects
else
	CONFDIR = $(SYSCONFDIR)/nagios/plugins.d
endif

conf/%: conf/%.in
	sed -e 's,@LIBDIR@,$(LIBDIR),g' $^ > $@

plugins/%: plugins/%.in
	sed -e 's,@LIBDIR@,$(LIBDIR),g' $^ > $@

nrpe_local.cfg: nrpe_local.cfg.in
	sed -e 's,@LIBDIR@,$(LIBDIR),g;s,@BINDIR@,$(BINDIR),g;s,@SYSCONFDIR@,$(SYSCONFDIR),g' nrpe_local.cfg.in > nrpe_local.cfg

install: install_files install_users install_permissions

install_users:

install_files: $(SUBSTFILES)
	mkdir -p $(DESTDIR)$(PLUGINDIR)/;
	install -p -m 755 plugins/check_* $(DESTDIR)$(PLUGINDIR)/;
	rm -f $(DESTDIR)$(PLUGINDIR)/*.in
	mkdir -p $(DESTDIR)$(CONFDIR)/
	cp -p conf/*.cfg $(DESTDIR)$(CONFDIR)/

install_permissions:

clean:
	find $(CURDIR) -name "*~" -exec rm {} \;
	rm -f $(SUBSTFILES)

.PHONY: all install install_users install_files install_permissions clean
