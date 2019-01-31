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
    f = host.file('/var/lib/icinga2/certs/ca.crt')
    assert f.exists


def test_tls_certificate(host):
    hostname = host.run('hostname --fqdn')
    f = host.file('/var/lib/icinga2/certs/%s.crt' % hostname.stdout)
    assert f.exists


def test_tls_signature(host):
    hostname = host.run('hostname --fqdn')
    cafile = '/var/lib/icinga2/certs/ca.crt'
    certfile = '/var/lib/icinga2/certs/%s.crt' % hostname.stdout
    issuer_ca = host.run('openssl x509 -issuer -noout -in %s', cafile)
    issuer_crt = host.run('openssl x509 -issuer -noout -in %s', certfile)
    v = host.run('openssl verify -CAfile %s %s', cafile, certfile)

    assert v.stdout == '%s: OK' % certfile
    assert issuer_ca.stdout == issuer_crt.stdout


def test_icinga2_object_sync(host):
    cmd = 'icinga2 object list --type {type} --name {name}'.format(
        type="Endpoint",
        name="icinga-centos-master",
    )
    o = host.run(cmd)
    assert re.search('Object', o.stdout)
