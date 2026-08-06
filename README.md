# 🕵️ OSINT Aggregator

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green) ![Tests](https://img.shields.io/badge/tests-passing-success) ![Status](https://img.shields.io/badge/status-active-brightgreen)

Automated reconnaissance tool that queries multiple intelligence sources for a domain or IP.

## Data Sources
| Source | Info |
|--------|------|
| Shodan | Open ports, services, vulnerabilities |
| VirusTotal | Malware history, reputation |
| WHOIS | Registration info, dates |
| DNS | A, MX, NS, TXT, CNAME records |
| Subdomains | crt.sh certificate transparency |
| GeoIP | Country, city, ASN |

## Installation
```bash
pip install -r requirements.txt
cp config.example.json config.json
# Add your API keys to config.json
```

## Usage
```bash
python osint.py -d example.com
python osint.py -i 8.8.8.8
python osint.py -d example.com -o report.json
```

## Responsible use

This project is published for **defensive research, education, and authorized security testing only**.
Use it exclusively on systems you own or have explicit written permission to assess. The author
assumes no liability for misuse. See `SECURITY.md` for the disclosure policy.
