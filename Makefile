NAME = nagios-plugins
LIBDIR = $(PREFIX)/lib
PLUGINDIR = $(LIBDIR)/nagios/plugins

SUBSTFILES = \
	$(basename $(wildcard conf/*.in)) \
	$(basename $(wildcard plugins/*.in)) \
	nrpe.cfg

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
	sed -e 's,@LIBDIR@,$(LIBDIR),g' -e 's,@PYTHON@,$(PYTHON),g' $^ > $@

nrpe.cfg: nrpe.cfg.in
	sed -e 's,@LIBDIR@,$(LIBDIR),g;s,@BINDIR@,$(BINDIR),g;s,@SYSCONFDIR@,$(SYSCONFDIR),g' nrpe.cfg.in > nrpe.cfg

install: install_files install_users install_permissions

install_users:

install_files: $(SUBSTFILES)
	mkdir -p $(DESTDIR)$(PLUGINDIR)/;
	install -p -m 755 plugins/check_* $(DESTDIR)$(PLUGINDIR)/;
	rm -f $(DESTDIR)$(PLUGINDIR)/*.in
	mkdir -p $(DESTDIR)$(CONFDIR)/
	cp -p conf/*.cfg $(DESTDIR)$(CONFDIR)/
	mkdir -p $(DESTDIR)$(SYSCONFDIR)/nrpe.d/
	install -p -m 644 nrpe.cfg $(DESTDIR)$(SYSCONFDIR)/nrpe.d/vigilo.cfg

install_permissions:

clean:
	find $(CURDIR) -name "*~" -exec rm {} \;
	rm -f $(SUBSTFILES)

SVN_REV = $(shell LANGUAGE=C LC_ALL=C svn info 2>/dev/null | awk '/^Revision:/ { print $$2 }')
rpm: clean pkg/$(NAME).$(DISTRO).spec
	mkdir -p build/$(NAME)
	rsync -a --exclude .svn --delete ./ build/$(NAME)
	mkdir -p build/rpm/{$(NAME),BUILD,TMP}
	cd build; tar -cjf rpm/$(NAME)/$(NAME).tar.bz2 $(NAME)
	cp pkg/$(NAME).$(DISTRO).spec build/rpm/$(NAME)/vigilo-$(NAME).spec
	rpmbuild -ba --define "_topdir $(CURDIR)/build/rpm" \
				 --define "_sourcedir %{_topdir}/$(NAME)" \
				 --define "_specdir %{_topdir}/$(NAME)" \
				 --define "_rpmdir %{_topdir}/$(NAME)" \
				 --define "_srcrpmdir %{_topdir}/$(NAME)" \
				 --define "_tmppath %{_topdir}/TMP" \
				 --define "_builddir %{_topdir}/BUILD" \
				 --define "svn .svn$(SVN_REV)" \
				 --define "dist .$(DIST_TAG)" \
				 $(RPMBUILD_OPTS) \
				 build/rpm/$(NAME)/vigilo-$(NAME).spec
	mkdir -p dist
	find build/rpm/$(NAME) -type f -name "*.rpm" | xargs cp -a -f -t dist/


.PHONY: all install install_users install_files install_permissions clean rpm
