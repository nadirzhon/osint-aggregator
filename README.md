# 🕵️ OSINT Aggregator

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
