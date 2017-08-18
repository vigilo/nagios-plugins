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

Il faut ensuite ajouter la configuration spécifique de Vigilo dans Nagios,
pour cela, editer le fichier `/etc/nagios/nagios.cfg` et supprimer ou
commenter les lignes qui commencent par ``cfg_file`` ou ``cfg_dir``. Puis,
ajouter les lignes suivantes ::

    # Command definitions for Nagios plugins
    cfg_dir=/etc/nagios/plugins.d/
    # Vigilo specific files
    cfg_dir=/etc/nagios/vigilo.d/
    # Vigiconf-generated conf file
    cfg_dir=/etc/vigilo/vigiconf/prod/nagios

    #activation de la prise en charge des données de performance
    process_performance_data=1
    host_perfdata_command=process-host-perfdata
    service_perfdata_command=process-service-perfdata
    #activation de la vérification de la fraîcheur
    check_host_freshness=1
    #utilisation du format européen pour les dates
    date_format=euro
    #activation des installations de grande envergure
    use_large_installation_tweaks=1


Enfin, si vous désirez utiliser NRPE, veillez à ce que la ligne suivante soit
présente dans ``/etc/nagios/nrpe.cfg``::

    include_dir=/etc/nrpe.d/


License
-------
Les plugins Nagios de Vigilo sont sous licence `GPL v2`_.


.. _documentation officielle: Vigilo_
.. _Vigilo: http://www.vigilo-nms.com
.. _Nagios: http://nagios.org
.. _NRPE: http://exchange.nagios.org/directory/Addons/Monitoring-Agents/NRPE-%252D-Nagios-Remote-Plugin-Executor/details
.. _socat: http://www.dest-unreach.org/socat/
.. _GPL v2: http://www.gnu.org/licenses/gpl-2.0.html

.. vim: set syntax=rst fileencoding=utf-8 tw=78 :



