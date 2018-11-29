import os
import re

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


def test_tls_ca(host):
    f = host.file('/etc/icinga2/pki/ca.crt')
    assert f.exists


def test_tls_certificate(host):
    hostname = host.run('hostname --fqdn')
    f = host.file('/etc/icinga2/pki/%s.crt' % hostname.stdout)
    assert f.exists


def test_tls_signature(host):
    hostname = host.run('hostname --fqdn')
    cafile = '/etc/icinga2/pki/ca.crt'
    certfile = '/etc/icinga2/pki/%s.crt' % hostname.stdout
    issuer_ca = host.run('openssl x509 -issuer -noout -in %s', cafile)
    issuer_crt = host.run('openssl x509 -issuer -noout -in %s', certfile)
    v = host.run('openssl verify -CAfile %s %s', cafile, certfile)

    assert v.stdout == '%s: OK' % certfile
    assert issuer_ca.stdout == issuer_crt.stdout


def test_icinga2_object_sync(host):
    o = host.run('icinga2 object list --type Endpoint --name monitor-m01')
    assert re.search('Object', o.stdout)
