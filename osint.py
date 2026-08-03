#!/usr/bin/env python3
"""
OSINT Aggregator - Multi-source intelligence gathering
Author: nadirzhon | github.com/nadirzhon
"""

import argparse
import json
import socket
import requests
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def get_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def dns_lookup(domain):
    results = {}
    try:
        import dns.resolver
        for rtype in ["A", "MX", "NS", "TXT"]:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                results[rtype] = [str(r) for r in answers]
            except Exception:
                results[rtype] = []
    except ImportError:
        results["error"] = "dnspython not installed"
    return results

def whois_lookup(domain):
    try:
        import whois
        w = whois.whois(domain)
        return {
            "registrar": str(w.registrar),
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
        }
    except Exception as e:
        return {"error": str(e)}

def get_subdomains_crtsh(domain):
    try:
        r = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=10)
        subs = set()
        for entry in r.json():
            for n in entry.get("name_value", "").split("\n"):
                if n.endswith(f".{domain}"):
                    subs.add(n.strip())
        return sorted(subs)
    except Exception as e:
        return [f"Error: {e}"]

def geoip_lookup(ip):
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        data = r.json()
        return {"country": data.get("country_name"), "city": data.get("city"),
                "asn": data.get("asn"), "org": data.get("org")}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="OSINT Aggregator")
    parser.add_argument("-d", "--domain")
    parser.add_argument("-i", "--ip")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    if not args.domain and not args.ip:
        parser.error("Provide --domain or --ip")

    report = {"generated": datetime.now().isoformat()}

    if args.domain:
        print(f"{Fore.CYAN}[*] DNS Lookup: {args.domain}{Style.RESET_ALL}")
        report["dns"] = dns_lookup(args.domain)
        print(json.dumps(report["dns"], indent=2))

        print(f"\n{Fore.CYAN}[*] WHOIS: {args.domain}{Style.RESET_ALL}")
        report["whois"] = whois_lookup(args.domain)
        print(json.dumps(report["whois"], indent=2))

        print(f"\n{Fore.CYAN}[*] Subdomains (crt.sh):{Style.RESET_ALL}")
        subs = get_subdomains_crtsh(args.domain)
        report["subdomains"] = subs
        for s in subs[:20]:
            print(f"  {s}")

        try:
            ip = socket.gethostbyname(args.domain)
            args.ip = ip
            print(f"\n{Fore.GREEN}[*] Resolved {args.domain} -> {ip}{Style.RESET_ALL}")
        except Exception:
            pass

    if args.ip:
        print(f"\n{Fore.CYAN}[*] GeoIP: {args.ip}{Style.RESET_ALL}")
        report["geoip"] = geoip_lookup(args.ip)
        print(json.dumps(report["geoip"], indent=2))

    if args.output:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=2)
        print(f"\n[*] Saved to {args.output}")

if __name__ == "__main__":
    main()
