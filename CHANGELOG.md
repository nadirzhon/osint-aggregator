# Changelog

## [1.1.0] - 2025-07-20
### Added
- Subdomain enumeration via crt.sh certificate transparency logs
- GeoIP enrichment for resolved IPs
- JSON report output (`-o report.json`)

### Fixed
- WHOIS timeout handling for unresponsive registrars
- DNS lookup error handling for non-existent record types

## [1.0.0] - 2025-06-01
### Initial Release
- DNS A/MX/NS/TXT record lookup
- WHOIS registration data
- Shodan and VirusTotal integration
