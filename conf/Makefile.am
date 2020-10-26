EXTRA_DIST = *.cfg.in
CLEANFILES = $(nagiospluginsconf_DATA)

nagiospluginsconf_DATA = \
	check_cpu.cfg        \
	check_dummy.cfg      \
	check_icmp.cfg       \
	check_ipmi.cfg       \
	check_megaraid.cfg   \
	check_proxy_ssl.cfg  \
	check_systemd.cfg  \
	check_tcp.cfg        \
	check_udp_simple.cfg

check_%: check_%.in Makefile
	$(SED) -e 's,@PLUGINDIR[@],$(nagiospluginsdir),g' $< > $@
	$(TOUCH) --reference=$< $@
