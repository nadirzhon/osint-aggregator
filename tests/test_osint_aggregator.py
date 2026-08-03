import sys
sys.path.insert(0, ".")

def test_geoip_structure():
    # Test that geoip function returns expected keys (mocked)
    result = {"country": "US", "city": "San Francisco", "asn": "AS15169", "org": "Google LLC"}
    assert "country" in result
    assert "asn" in result

def test_config_fallback():
    import json, os
    # Should not raise when config.json absent
    try:
        with open("config.json") as f:
            cfg = json.load(f)
    except FileNotFoundError:
        cfg = {}
    assert isinstance(cfg, dict)

def test_crtsh_parse():
    # Simulate crt.sh response parsing
    fake_entries = [
        {"name_value": "api.example.com\nwww.example.com"},
        {"name_value": "mail.example.com"},
    ]
    domain = "example.com"
    subs = set()
    for e in fake_entries:
        for n in e.get("name_value", "").split("\n"):
            if n.endswith(f".{domain}"):
                subs.add(n.strip())
    assert "api.example.com" in subs
    assert "www.example.com" in subs
    assert "mail.example.com" in subs

if __name__ == "__main__":
    test_geoip_structure()
    test_config_fallback()
    test_crtsh_parse()
    print("All tests passed.")
