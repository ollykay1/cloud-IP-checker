from utils.ip_lookup import lookup_ip

def test_lookup_valid_ip():
    result = lookup_ip("8.8.8.8")
    assert "ip" in result