ssm.icinga2
===========

Install and configure Icinga 2 master and satellites.

Requirements
------------

This role requires you to configure repositories for icinga2, icingaweb2 and
their dependencies. For CentOS/RHEL version 7 this means EPEL and Software
Collections.

You should configure a database server, web server, as well as a php server
(PHP FPM). The icingaweb2 package will use this.

TODO: Write requirements documentation.

Role Variables
--------------

- icinga2_manage_repo: When this is set to a true value, the role will install
  and configure the repository and signing key for the icinga packages.

- icinga2_key_url: The URL for the icinga repo signing key.

- icinga2_repo_url: The URL for the icinga repo.

TODO: Write documentation. In the meantime, see defaults/main.yml

Inventory
---------

For each host, a set of variables determines its role and location in the
icinga2 cluster architecture.

TODO: Refactor inconsistent variable names and use.

Inventory variables
+++++++++++++++++++

- icinga2_zone: The zone name for this host

- icinga2_parent_host: The parent host for CSR autosigning

- icinga2_parent_zone: The parent zone (for --parent_host, or for --endpoint?)

- icinga2_endpoint: A list of parent endpoints to connect to for configuration
  and checks (string, array)

Inventory group: icinga_master
++++++++++++++++++++++++++++++

This group is for hosts in the Icinga 2 master zone. It is expected to run the
configuration master, the TLS Certificate Authority and the icinga web
frontend. For now, it supports one master. The master zone is "master".

TODO: Configuration items:

- master zone name

Inventory group: icinga_satellite
+++++++++++++++++++++++++++++++++

This group is for hosts in the Icinga satellite zones. These run no web
interface, and receive configuration from the master zone. This is tested with
one level of zones below master, but could in theory support nested or chained
zones.

Satellites which share zone name will load balance active checks.

TODO: Configuration items:

- ca host
- trusted parent host
- satellite zone name

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: ssm.icinga2

License
-------

GPLv3

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
