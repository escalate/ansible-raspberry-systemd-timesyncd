"""Role testing files using testinfra"""


def test_systemd_timesyncd_service(host):
    """Check systemd-timesyncd service"""
    s = host.service("systemd-timesyncd")
    assert s.is_running
    assert s.is_enabled
