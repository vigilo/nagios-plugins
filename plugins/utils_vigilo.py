# -*- coding: utf-8 -*-
# vim: fileencoding=utf-8 sw=4 ts=4 et ai
# Copyright (C) 2015-2016 CS-SI
# License: GNU GPL v2 <http://www.gnu.org/licenses/gpl-2.0.html>

import sys


# Codes d'état pour les services
OK          = 0
WARNING     = 1
CRITICAL    = 2
UNKNOWN     = 3

# Codes d'état pour les hôtes
UP          = 0
DOWN        = 2
UNREACHABLE = 3


def get_state(state, service=True):
    """
    Retourne le nom associé à un code d'état.

    @param state: Code d'état.
    @type state: C{int}
    @param service: Indique si le code d'état porte sur un service (C{True})
        ou sur un hôte (C{False})
    @type service: C{bool}
    @return: Nom de l'état correspondant au code donné
    @rtype: C{str}
    """
    states = {
        'services': {
            0: 'OK',
            1: 'WARNING',
            2: 'CRITICAL',
            3: 'UNKNOWN',
        },

        'hosts': {
            0: 'UP',
            1: 'DOWN',
            3: 'UNREACHABLE',
        },
    }
    if service:
        mapping = states['services']
    else:
        mapping = states['hosts']
    return mapping.get(state, mapping[3])


def exit_nagios(state, message, metrics=None):
    """
    Affiche l'état et les performances d'un service/hôte supervisé
    au format Nagios puis quitte le script.

    @param state: Code d'état (OK, WARNING, ...) à retourner.
    @type state: C{int}
    @param message: Message de retour de la sonde.
        Le message sera automatiquement préfixe du nom
        de l'état (ex : "OK: ...").
    @type message: C{str}
    @param metrics: Données de performances, sous la forme d'un dictionnaire :
        -   avec le nom de la métrique en clé et sa valeur (C{int} ou C{float})
        -   avec le nom de la métrique en clé et un tuple
            C{(valeur, warn, crit, min, max)} en guise de valeur
    @type metrics: C{dict}
    """
    if metrics is None:
        metrics = {}

    perfdata = []
    for k, v in metrics.items():
        if isinstance(v, (str, unicode, int, float)):
            perfdata.append("'%s'=%s" % (k, v))
        else:
            perfdata.append("'%s'=%s" % (k, ';'.join(str(s) for s in v)))
    if perfdata:
        message += '|' + ' '.join(perfdata)

    print "%s: %s" % (get_state(state), message)
    sys.exit(state)


def check_range(value, threshold):
    """
    Teste si une valeur se situe hors d'une plage autorisée (seuils),
    défini selon le format de Nagios décrit ici:
    http://nagiosplug.sourceforge.net/developer-guidelines.html#THRESHOLDFORMAT

    @param value: Valeur à tester.
    @type value: C{float}
    @param threshold: Plage autorisée (seuils) au format Nagios.
    @type threshold: C{str}
    @return: Return True si la valeur se trouve hors de la plage autorisée
        ou False si elle se trouve dans la plage autorisée.
    @raise ValueError: La description de la plage autorisée est invalide.
    """
    # Adapté du code du Collector (base.pm:isOutOfBounds)
    # Si des changements sont apportés, il faut aussi les répercuter
    # dans vigilo.connector_metro.threshold:is_out_of_bounds.
    inside = threshold.startswith('@')
    if inside:
        threshold = threshold[1:]
    if not threshold:
        threshold = ":"

    if ":" not in threshold:
        threshold = float(threshold)
        if inside:
            return value >= 0 and value <= threshold
        return value < 0 or value > threshold

    if threshold == ":":
        return inside

    low, up = threshold.split(':', 2)
    if low == '~' or not low:
        up = float(up)
        if inside:
            return (value <= up)
        else:
            return (value > up)

    if not up:
        low = float(low)
        if inside:
            return (value >= low)
        else:
            return (value < low)

    low = float(low)
    up = float(up)
    if low > up:
        raise ValueError('Invalid threshold')

    if inside:
        return (value >= low and value <= up)
    else:
        return (value < low or value > up)

