AC_INIT([vigilo-nagios-plugins], [m4_esyscmd_s([cat VERSION.txt])], [], [], [https://www.vigilo-nms.com/])
AC_PREREQ([2.59])
AC_CANONICAL_HOST
AM_INIT_AUTOMAKE([1.9 foreign])

AC_PROG_MKDIR_P
AC_PROG_SED

AC_PATH_PROG(TOUCH, touch)
if test "x$TOUCH" = "x"; then
  AC_MSG_ERROR([touch not found])
fi

AC_PATH_PROG(RMDIR, rmdir)
if test "x$RMDIR" = "x"; then
  AC_MSG_ERROR([rmdir not found])
fi

AC_ARG_VAR(nrpeconfdir,  [[SYSCONFDIR/nrpe.d] NRPE configuration directory])
if test -z "$nrpeconfdir"; then
   nrpeconfdir='${sysconfdir}/nrpe.d'; fi

AC_ARG_VAR(nagiosvigiloconfdir,  [[SYSCONFDIR/nagios/vigilo.d] Nagios Vigilo-related configuration directory])
if test -z "$nagiosvigiloconfdir"; then
   nagiosvigiloconfdir='${sysconfdir}/nagios/vigilo.d'; fi

AC_ARG_VAR(nagiospluginsconfdir,  [[SYSCONFDIR/nagios/plugins.d] Nagios plugins configuration directory])
if test -z "$nagiospluginsconfdir"; then
   nagiospluginsconfdir='${sysconfdir}/nagios/plugins.d'; fi

AC_ARG_VAR(nagiospluginsdir,  [[LIBDIR/nagios/plugins] Nagios plugins directory])
if test -z "$nagiospluginsdir"; then
   nagiospluginsdir='${libdir}/nagios/plugins'; fi

AC_ARG_VAR(nagioshandlersdir,  [[LIBDIR/nagios/plugins/eventhandlers] Nagios event handlers directory])
if test -z "$nagioshandlersdir"; then
   nagioshandlersdir='${libdir}/nagios/plugins/eventhandlers'; fi


AC_CONFIG_FILES([Makefile handlers/Makefile plugins/Makefile conf/Makefile selinux/Makefile])

AC_SUBST(VERSION)

AC_OUTPUT
