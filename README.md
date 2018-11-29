# ssm.icinga2

Install and configure Icinga 2 master and satellites.

## Requirements

This role requires you to configure repositories for icinga2, icingaweb2 and
their dependencies. For CentOS/RHEL version 7 this means EPEL and Software
Collections.

You should configure a database server, web server, as well as a php server
(PHP FPM). The icingaweb2 package will use this.

TODO: Write requirements documentation.

## Role Variables

- icinga2\_manage\_repo: When this is set to a true value, the role
  will install and configure the repository and signing key for the
  icinga packages.

- icinga2\_key\_url: The URL for the icinga repo signing key. Used
  only if icinga2\_manage\_repo is set to a true value.

- icinga2\_repo\_url: The URL for the icinga repo. Used only if
  icinga2\_manage\_repo is set to a true value.

TODO: Write documentation. In the meantime, see defaults/main.yml

## Inventory

For each host, a set of variables determines its role and location in the
icinga2 cluster architecture.

TODO: Refactor inconsistent variable names and use.

### Inventory variables

- icinga2\_role: The role of this host. "standalone", "master" or
  "satellite".  Default is "standalone".

  If the role is "standalone", no cluster PKI actions will be
  performed.

  If the role is "master", a cluster PKI CA will be initialized.

  If the role is "satellite", a PKI CSR will be generated on this
  host, and submitted to the host indicated by the
  "icinga2\_parent\_host" variable.

  The "satellite" role requires another host in the same play having
  the "master" role already configured, as well as properly configured
  icinga2\_parent\_host and icinga2\_parent\_zone variables.

- icinga2\_zone: The zone name for this host.  Default is the value of
  inventory\_hostname

- icinga2\_parent\_host: The parent host for CSR signing.

- icinga2\_parent\_zone: The parent zone (for --parent\_host, or for
  --endpoint?)

- icinga2\_endpoint: A list of parent endpoints to connect to for
  configuration and checks (string, array)

- icinga2\_ido\_database: The database name used for the IDO
  database. Default is "icinga".

- icinga2\_ido\_host: The hostname used when connecting the the IDO
  database. Default is "localhost".

- icinga2\_ido\_username: The username for authenticating to the IDO
  database. Default is "icinga".

- icinga2\_ido\_password: The password for authenticating to the IDO
  database. Default is "icinga"

  Please change this password as soon as practically possible.

## Example Playbook

Order the hosts in the inventory so the master is provisioned first. The
satellites and the clients need the master to be operational.

    - hosts:
        - master
        - satellites
      roles:
         - role: ssm.icinga2

## License

GPLv3
