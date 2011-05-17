NAME = nagios-plugins
PKGNAME = vigilo-$(NAME)
SYSCONFDIR = /etc
LIBDIR = /usr/lib
PLUGINDIR = /usr/lib$(if $(realpath /usr/lib64),64,)/nagios/plugins
EVENTHANDLERDIR = $(PLUGINDIR)/eventhandlers
VIGILOCONFDIR = $(SYSCONFDIR)/nagios/vigilo.d
PYTHON = /usr/bin/python
DESTDIR =

VERSION := $(shell cat VERSION.txt)

SUBSTFILES = \
	$(basename $(wildcard conf/*.in)) \
	$(basename $(wildcard plugins/*.in)) \
	nrpe.cfg nagios-plugin-commands.cfg

all: $(SUBSTFILES)

define find-distro
if [ -f /etc/debian_version ]; then \
	echo "debian" ;\
elif [ -f /etc/mandriva-release ]; then \
	echo "mandriva" ;\
elif [ -f /etc/redhat-release ]; then \
	echo "redhat" ;\
else \
	echo "unknown" ;\
fi
endef
DISTRO := $(shell $(find-distro))
DIST_TAG = $(DISTRO)

ifeq ($(DISTRO),debian)
	NPCONFDIR = $(SYSCONFDIR)/nagios-plugins/config
else ifeq ($(DISTRO),mandriva)
	NPCONFDIR = $(SYSCONFDIR)/nagios/plugins.d
else ifeq ($(DISTRO),redhat)
	NPCONFDIR = $(SYSCONFDIR)/nagios/plugins.d
else
	NPCONFDIR = $(SYSCONFDIR)/nagios/plugins.d
endif

conf/%: conf/%.in
	sed -e 's,@PLUGINDIR@,$(PLUGINDIR),g' $^ > $@

plugins/%: plugins/%.in
	sed -e 's,@PLUGINDIR@,$(PLUGINDIR),g' -e 's,@PYTHON@,$(PYTHON),g' $^ > $@

%.cfg: %.cfg.in
	sed -e 's,@PLUGINDIR@,$(PLUGINDIR),g;s,@BINDIR@,$(BINDIR),g;s,@SYSCONFDIR@,$(SYSCONFDIR),g' $^ > $@


install: $(SUBSTFILES)
	mkdir -p $(DESTDIR)$(PLUGINDIR)/;
	install -p -m 755 plugins/check_* $(DESTDIR)$(PLUGINDIR)/;
	rm -f $(DESTDIR)$(PLUGINDIR)/*.in
	mkdir -p $(DESTDIR)$(NPCONFDIR)/
	cp -p conf/*.cfg $(DESTDIR)$(NPCONFDIR)/
	mkdir -p $(DESTDIR)$(SYSCONFDIR)/nrpe.d/
	mkdir -p $(DESTDIR)$(VIGILOCONFDIR)/
	install -p -m 644 nrpe.cfg $(DESTDIR)$(SYSCONFDIR)/nrpe.d/vigilo.cfg
	install -p -m 644 vigilo.cfg $(DESTDIR)$(VIGILOCONFDIR)/vigilo.cfg
	install -p -m 644 vigilo-commands.cfg $(DESTDIR)$(NPCONFDIR)/vigilo-commands.cfg
	mkdir -p $(DESTDIR)$(EVENTHANDLERDIR)/;
	install -p -m 755 plugins/eventhandlers/service_notification_event $(DESTDIR)$(EVENTHANDLERDIR)/;
ifeq ($(DISTRO),redhat)
	# Sur Red Hat, les plugins ne sont pas fournis avec leur fichier de conf
	install -p -m 644 nagios-plugin-commands.cfg $(DESTDIR)$(NPCONFDIR)/nagios-plugin-commands.cfg
endif


clean:
	find $(CURDIR) -name "*~" -exec rm {} \;
	rm -rf build
	rm -f $(SUBSTFILES)


SVN_REV = $(shell LANGUAGE=C LC_ALL=C svn info 2>/dev/null | awk '/^Revision:/ { print $$2 }')

sdist: dist/$(PKGNAME)-$(VERSION)$(if $(RELEASE),,-r$(SVN_REV)).tar.gz
dist/$(PKGNAME)-$(VERSION).tar.gz dist/$(PKGNAME)-$(VERSION)%.tar.gz:
	mkdir -p build/sdist/$(PKGNAME)-$(VERSION)
	rsync -aL --exclude .svn --exclude /dist --exclude /build --delete ./ build/sdist/$(PKGNAME)-$(VERSION)
	mkdir -p dist
	cd build/sdist; tar -czf $(CURDIR)/$@ $(PKGNAME)-$(VERSION)
	@echo "Source tarball is: $@"

rpm: clean pkg/$(NAME).$(DISTRO).spec dist/$(PKGNAME)-$(VERSION).tar.gz
	mkdir -p build/rpm/{$(NAME),BUILD,TMP}
	mv dist/$(PKGNAME)-$(VERSION).tar.gz build/rpm/$(NAME)/
	sed -e 's/@VERSION@/'`cat VERSION.txt`'/g' pkg/$(NAME).$(DISTRO).spec \
		> build/rpm/$(NAME)/$(PKGNAME).spec
	rpmbuild -ba --define "_topdir $(CURDIR)/build/rpm" \
				 --define "_sourcedir %{_topdir}/$(NAME)" \
				 --define "_specdir %{_topdir}/$(NAME)" \
				 --define "_rpmdir %{_topdir}/$(NAME)" \
				 --define "_srcrpmdir %{_topdir}/$(NAME)" \
				 --define "_tmppath %{_topdir}/TMP" \
				 --define "_builddir %{_topdir}/BUILD" \
				 $(if $(RELEASE),,--define "svn .svn$(SVN_REV)") \
				 --define "dist .$(DIST_TAG)" \
				 $(RPMBUILD_OPTS) \
				 build/rpm/$(NAME)/$(PKGNAME).spec
	mkdir -p dist
	find build/rpm/$(NAME) -type f -name "*.rpm" | xargs cp -a -f -t dist/


.PHONY: all install clean rpm sdist
