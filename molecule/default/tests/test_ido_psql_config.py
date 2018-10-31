import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('monitor-m01')


def test_ido_package(host):
    p = host.package("icinga2-ido-pgsql")
    assert p.is_installed


def test_ido_active(host):
    c = host.run('icinga2 feature list')
    assert re.search(
        r"^Enabled features:\s+(?:\S+\s+)*ido-pgsql(?:\s+\S+)*$",
        c.stdout, flags=re.MULTILINE)


def test_icinga2_object(host):
    c = host.run('icinga2 object list --type IdoPgsqlConnection')
    assert c.rc == 0
    assert re.search(
        r"ido-pgsql",
        c.stdout, flags=re.MULTILINE)
