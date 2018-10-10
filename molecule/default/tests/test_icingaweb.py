import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('icinga_master')


@pytest.mark.parametrize("package", [
    "icingaweb2",
    "icingacli",
])
def test_package(host, package):
    p = host.package(package)
    assert p.is_installed


def test_curl(host):
    c = host.run('curl -v http://localhost/icingaweb2/setup')
    assert c.rc == 0
