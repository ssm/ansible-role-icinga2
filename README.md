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

- icinga2_manage_repo: When this is set to a true value, the role will install
  and configure the repository and signing key for the icinga packages.

- icinga2_key_url: The URL for the icinga repo signing key. Used only if
  icinga2_manage_repo is set to a true value.

- icinga2_repo_url: The URL for the icinga repo. Used only if
  icinga2_manage_repo is set to a true value.

TODO: Write documentation. In the meantime, see defaults/main.yml

## Inventory

For each host, a set of variables determines its role and location in the
icinga2 cluster architecture.

TODO: Refactor inconsistent variable names and use.

### Inventory variables

- icinga2_role: The role of this host. "master" or "satellite"

- icinga2_zone: The zone name for this host

- icinga2_parent_host: The parent host for CSR autosigning

- icinga2_parent_zone: The parent zone (for --parent_host, or for --endpoint?)

- icinga2_endpoint: A list of parent endpoints to connect to for configuration
  and checks (string, array)

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
