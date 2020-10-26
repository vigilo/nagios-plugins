DIST_SUBDIRS = handlers plugins conf selinux
SUBDIRS = . handlers plugins conf selinux

CLEANFILES = $(nagiosplugins_SCRIPTS) $(nagiospluginsconf_DATA) $(nagiosvigiloconf_DATA)
EXTRA_DIST = *.txt *.in

nagiospluginsconf_DATA = nagios-plugin-commands.cfg vigilo-commands.cfg
nagiosvigiloconf_DATA = vigilo.cfg
nrpeconf_DATA = vigilo-nrpe-config.cfg

%.cfg: %.cfg.in Makefile
	$(SED) -e 's,@PLUGINDIR[@],$(nagiospluginsdir),g' \
		-e 's,@BINDIR[@],$(bindir),g' \
		-e 's,@NEHDIR[@],$(nagioshandlersdir),g' \
		-e 's,@SYSCONFDIR[@],$(sysconfdir),g' $< > $@
	$(TOUCH) --reference=$< $@

