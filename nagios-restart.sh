#!/bin/sh

# Redémarrage régulier de Nagios pour éviter les fuites de mémoire de l'ePN.
# Ticket Vigilo #905. Tickets Nagios :
#  * http://tracker.nagios.org/view.php?id=71
#  * http://tracker.nagios.org/view.php?id=92

# On tente de déterminer l'emplacement du fichier de PID de Nagios
# à partir des emplacements les plus probables pour le fichier nagios.cfg.
nagios_pidfile=
for d in /etc/nagios3 /etc/nagios; do
    if test -f "$d/nagios.cfg"; then
        possible_pidfile=`egrep "^[[:space:]]*lock_file" "$d/nagios.cfg"|cut -d= -f2`
        # Élimine les espaces éventuels autour du chemin.
        possible_pidfile=`echo $possible_pidfile`
        if test -f $possible_pidfile; then
            nagios_pidfile=$possible_pidfile
            break
        fi
    fi
done

# Pas de fichier de PID, on ne fait rien
# (Nagios s'est probablement arrêté correctement entre temps).
if test -z "$nagios_pidfile"; then
    exit 0
fi
nagios_pid=`head -n 1 $nagios_pidfile`

# On ne fait rien si Nagios n'est pas en cours d'exécution.
if ! ps -p $nagios_pid > /dev/null 2>&1; then
    exit 0
fi

/etc/init.d/nagios stop
sleep 2

# On envoie un signal SIGTERM au processus principal de Nagios
# ainsi qu'à tous ses sous-processus dans le cas où le "stop" classique
# n'aurait pas suffit.
kill -- -$nagios_pid 2>/dev/null
sleep 2

/etc/init.d/nagios start
