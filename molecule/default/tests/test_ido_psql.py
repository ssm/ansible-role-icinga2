import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('icinga_master')


def test_ido_package(host):
    p = host.package("icinga2-ido-pgsql")
    assert p.is_installed


def test_ido_active(host):
    c = host.run('icinga2 feature list')
    assert re.search(
        r"^Enabled features:\s+(?:\S+\s+)*ido-pgsql(?:\s+\S+)*$",
        c.stdout, flags=re.MULTILINE)


def test_service_postgresql(host):
    s = host.service('postgresql')
    assert s.is_enabled
    assert s.is_running


def test_icinga_object_ido(host):
    c = host.run('icinga2 object list --type IdoPgsqlConnection')
    assert re.search(r'type = "IdoPgsqlConnection"', c.stdout)
