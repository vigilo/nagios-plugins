Nagios Plugins
==============

Ce composant fournit un ensemble de plugins Nagios_ utilisables dans Vigilo_,
et déjà associés à un test dans VigiConf.

Comme son nom ne l'indique pas, il fournit aussi un fichier de configuration
pour Nagios permettant de le faire fonctionner avec Vigilo, et un fichier de
configuration pour NRPE_ pour déclarer les plugins fournis.

Pour les détails du fonctionnement des plugins Nagios, se reporter à la
`documentation officielle`_.


Dépendances
-----------
Les dépendances des plugins fournis sont spécifiques à chaque plugin. Par
exemple: ``curl``, ``ipmitool``, ``megaraid``, etc.

L'intégration de Nagios à Vigilo nécessite la présence de l'utilitaire socat_.


Installation
------------
L'installation se fait par la commande ``make install`` (à exécuter en
``root``).


License
-------
Les plugins Nagios de Vigilo sont sous licence `GPL v2`_.


.. _documentation officielle: Vigilo_
.. _Vigilo: http://www.projet-vigilo.org
.. _Nagios: http://nagios.org
.. _NRPE: http://exchange.nagios.org/directory/Addons/Monitoring-Agents/NRPE-%252D-Nagios-Remote-Plugin-Executor/details
.. _socat: http://www.dest-unreach.org/socat/
.. _GPL v2: http://www.gnu.org/licenses/gpl-2.0.html

.. vim: set syntax=rst fileencoding=utf-8 tw=78 :


