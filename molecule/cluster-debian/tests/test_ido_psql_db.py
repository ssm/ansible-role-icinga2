import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('cluster-debian-master')


def test_service_postgresql(host):
    s = host.service('postgresql')
    assert s.is_enabled
    assert s.is_running


def test_query(host):
    fqdn = host.run('hostname --fqdn').stdout
    c = host.run(
        "su - nagios -s /bin/sh -c %s",
        (
            "env PGPASSWORD=icinga "
            + "psql -h localhost -U icinga -d icinga -A -t -c \""
            + "SELECT icinga_objects.name1 FROM icinga_zones "
            + "LEFT JOIN icinga_objects "
            + "ON icinga_zones.zone_object_id = icinga_objects.object_id "
            + "WHERE icinga_objects.name1 = \'%s\';" % fqdn
            + "\"")
        )
    assert c.rc == 0
    assert c.stdout == fqdn
