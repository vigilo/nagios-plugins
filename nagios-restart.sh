#!/bin/sh

# Redémarrage régulier de Nagios pour éviter les fuites de mémoire de l'ePN.
# Ticket Vigilo #905. Tickets Nagios :
#  * http://tracker.nagios.org/view.php?id=71
#  * http://tracker.nagios.org/view.php?id=92

/etc/init.d/nagios stop
sleep 2
pkill nagios
sleep 2
/etc/init.d/nagios start
