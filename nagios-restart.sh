#!/bin/sh
# Copyright (C) 2011-2013 CS-SI
# License: GNU GPL v2 <http://www.gnu.org/licenses/gpl-2.0.html>

# Redémarrage régulier de Nagios pour éviter les fuites de mémoire de l'ePN.
# Ticket Vigilo #905. Tickets Nagios :
#  * http://tracker.nagios.org/view.php?id=71
#  * http://tracker.nagios.org/view.php?id=92

/etc/init.d/nagios stop
for i in `seq 20`; do
    pgrep -u nagios nagios >/dev/null || break
    sleep 1
done

# S'il reste des processus Nagios en vie, on les tue.
pgrep -u nagios nagios >/dev/null
if [ $? -eq 0 ]; then
    # On compte ici sur le fait que l'utilisateur "nagios"
    # a des droits restreints et ne peut pas killer d'autres
    # processus sans rapport avec Nagios (et en particulier,
    # pas le script courant exécuté en tant que "root").
    sudo -u nagios pkill -KILL -u nagios nagios
fi

/etc/init.d/nagios start
