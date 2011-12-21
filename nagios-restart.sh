#!/bin/sh

# Redémarrage régulier de Nagios pour éviter les fuites de mémoire de l'ePN.
# Ticket Vigilo #905. Tickets Nagios :
#  * http://tracker.nagios.org/view.php?id=71
#  * http://tracker.nagios.org/view.php?id=92

/etc/init.d/nagios stop
for i in `seq 20`; do
    pgrep nagios >/dev/null || exit 0
    sleep 1
done

# On compte ici sur le fait que l'utilisateur "nagios"
# a des droits restreints et ne peut pas killer d'autres
# processus sans rapport avec Nagios (et en particulier,
# pas le script courant exécuté en tant que "root").
sudo -u nagios pkill -u nagios -KILL nagios

/etc/init.d/nagios start
