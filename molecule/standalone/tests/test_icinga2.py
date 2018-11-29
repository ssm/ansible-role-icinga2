import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_icinga2_package(host):
    p = host.package("icinga2")
    assert p.is_installed


def test_icinga2_service(host):
    s = host.service('icinga2')
    assert s.is_running
    assert s.is_enabled
