# OpenScanner Development Roadmap

OpenScanner is a terminal-based OSINT platform designed to collect, organize, analyze, and report on publicly available information. The goal is to evolve from a simple username scanner into a complete investigation framework.

---

# Version 1.0 – Foundation

Focus: Core functionality, stability, and usability.

## Username Intelligence
- [ ] Search usernames across hundreds of websites
- [ ] Categorize results (Social, Gaming, Development, Forums, etc.)
- [ ] Color-coded output
- [ ] Display profile URLs
- [ ] JSON export
- [ ] CSV export
- [ ] Save scan results locally
- [ ] Scan history

## User Interface
- [ ] Interactive terminal menu
- [ ] ASCII startup banner
- [ ] Progress bars
- [ ] Scan statistics
- [ ] Error handling and logging

## Performance
- [ ] Multi-threaded scanning
- [ ] Configurable timeout values
- [ ] Configurable thread count
- [ ] Retry failed requests

## Data Storage
- [ ] SQLite database integration
- [ ] Store previous scans
- [ ] Store discovered usernames
- [ ] Search previous results

---

# Version 1.5 – Enhanced Username Investigation

Focus: Gathering more information from discovered profiles.

## Profile Analysis
- [ ] Detect profile existence
- [ ] Collect profile metadata where available
- [ ] Account creation dates
- [ ] Follower counts
- [ ] Biography extraction
- [ ] Website extraction

## Username Variations
- [ ] Generate common username variations
- [ ] Search generated variants
- [ ] Detect likely alternate accounts

## Cross-Link Detection
- [ ] Detect linked websites
- [ ] Detect linked social media accounts
- [ ] Detect public email addresses

---

# Version 2.0 – Intelligence Collection Modules

Focus: Expanding beyond usernames.

## Email Intelligence
- [ ] Email validation
- [ ] Domain analysis
- [ ] MX record lookup
- [ ] Mail provider detection
- [ ] Disposable email detection
- [ ] Gravatar lookup
- [ ] Public account association checks

## Domain Intelligence
- [ ] WHOIS lookup
- [ ] DNS record collection
- [ ] MX records
- [ ] TXT records
- [ ] SPF analysis
- [ ] DMARC analysis
- [ ] SSL certificate inspection
- [ ] Subdomain enumeration
- [ ] Registrar identification

## Technology Fingerprinting
- [ ] Detect web technologies
- [ ] Identify hosting providers
- [ ] Detect CDN usage
- [ ] Detect frameworks and CMS platforms

## IP Intelligence
- [ ] Geolocation lookup
- [ ] ASN lookup
- [ ] ISP detection
- [ ] Reverse DNS lookup
- [ ] Reputation checks
- [ ] Threat intelligence integration

## Phone Number Intelligence
- [ ] Carrier lookup
- [ ] Country identification
- [ ] Number type detection
- [ ] Timezone detection

---

# Version 2.5 – Metadata Analysis

Focus: Extracting information from files.

## Image Metadata
- [ ] EXIF extraction
- [ ] GPS coordinate extraction
- [ ] Camera information
- [ ] Device information

## Document Metadata
- [ ] PDF metadata extraction
- [ ] Microsoft Office metadata extraction
- [ ] Author identification
- [ ] Software identification
- [ ] Creation timestamps
- [ ] Modification timestamps

## Hashing
- [ ] MD5 generation
- [ ] SHA1 generation
- [ ] SHA256 generation

---

# Version 3.0 – Case Management System

Focus: Organizing investigations.

## Case Creation
- [ ] Create investigations
- [ ] Edit investigations
- [ ] Delete investigations
- [ ] Archive investigations

## Investigation Workspace
- [ ] Dedicated case directories
- [ ] Automatic evidence storage
- [ ] Case summaries
- [ ] Investigation status tracking

## Notes System
- [ ] Add notes
- [ ] Edit notes
- [ ] Timestamp notes
- [ ] Search notes

## Evidence Locker
- [ ] Save screenshots
- [ ] Save HTML pages
- [ ] Save JSON results
- [ ] Save metadata reports

## Tagging
- [ ] Custom tags
- [ ] Evidence categorization
- [ ] Search by tags

---

# Version 3.5 – Reporting System

Focus: Presenting findings.

## Report Generation
- [ ] Markdown reports
- [ ] HTML reports
- [ ] PDF reports
- [ ] JSON reports

## Report Sections
- [ ] Executive summary
- [ ] Findings
- [ ] Evidence
- [ ] Sources
- [ ] Timeline
- [ ] Recommendations

## Exports
- [ ] Case export
- [ ] Evidence export
- [ ] Database export

---

# Version 4.0 – Correlation Engine

Focus: Connecting collected information.

## Entity Correlation
- [ ] Correlate usernames
- [ ] Correlate domains
- [ ] Correlate emails
- [ ] Correlate IP addresses
- [ ] Correlate websites

## Relationship Mapping
- [ ] Account relationships
- [ ] Domain ownership relationships
- [ ] Infrastructure relationships
- [ ] Social profile relationships

## Confidence Scoring
- [ ] Match confidence calculation
- [ ] Similarity analysis
- [ ] Relationship ranking

---

# Version 4.5 – Timeline Analysis

Focus: Reconstructing events.

## Timeline Builder
- [ ] Account creation events
- [ ] Domain registration events
- [ ] Certificate issuance events
- [ ] Metadata timestamps

## Chronological Investigation View
- [ ] Sort findings by date
- [ ] Visual timeline export
- [ ] Event correlation

---

# Version 5.0 – Investigation Platform

Focus: Full-featured OSINT workflow.

## Investigation Dashboard
- [ ] Investigation overview
- [ ] Active cases
- [ ] Recent scans
- [ ] Evidence statistics

## Search Engine
- [ ] Global database search
- [ ] Search across cases
- [ ] Search evidence
- [ ] Search notes

## Automation
- [ ] Scheduled scans
- [ ] Watchlists
- [ ] Alerting system
- [ ] Automatic report generation

## Plugins
- [ ] Plugin framework
- [ ] Community modules
- [ ] Third-party integrations

---

# Future Ideas

## Visualization
- [ ] Relationship graphs
- [ ] Network diagrams
- [ ] Investigation maps
- [ ] Timeline graphs

## API
- [ ] REST API
- [ ] Authentication system
- [ ] Remote investigation support

## Collaboration
- [ ] Multi-user investigations
- [ ] Shared evidence
- [ ] Team notes
- [ ] Role permissions

## Machine Learning
- [ ] Entity matching assistance
- [ ] Similar username prediction
- [ ] Pattern detection
- [ ] Automated correlation suggestions

---

# Long-Term Goal

Transform OpenScanner from a simple username scanner into a complete OSINT investigation platform capable of:

- Collecting public intelligence
- Organizing investigations
- Correlating entities
- Preserving evidence
- Generating professional reports
- Supporting complete investigative workflows
