utilsdir = $(nagiospluginsdir)/utils_vigilo/

nagiosplugins_SCRIPTS =    \
	check_cpu              \
	check_https_via_proxy  \
	check_ipmi             \
	check_megaraid         \
	check_raid             \
	check_systemd          \
	check_udp_simple

utils_DATA = utils_vigilo.py
EXTRA_DIST = $(nagiosplugins_SCRIPTS) $(utils_DATA)

install-data-hook:
	cd "$(DESTDIR)$(utilsdir)" && mv -f utils_vigilo.py __init__.py
