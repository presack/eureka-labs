# School Proxy Investigation

## Scenario

Your school district's network team has noticed students accessing content that bypasses the web filter. One student's traffic was flagged terminating at **mathteachersforhire.shop**. The domain name sounds innocuous — but something doesn't add up.

Your job is to investigate this domain, characterize what it's actually doing, and map as much of the related infrastructure as you can find. A full investigation will take you through six pivot levels, multiple IP addresses, and ultimately to a GitHub username — all using passive, tool-assisted reconnaissance only.

## Starting point

```
mathteachersforhire.shop
```

## Tools available

Use StealthOps console mode. The core query gives you DNS, WHOIS, MX, NS, and TXT. Enrichment providers useful for this case:

| Alias | Provider | Why |
|---|---|---|
| `vd` | ViewDNS | Subdomains, reverse IP, IP history |
| `dd` | DNSDumpster | DNS map |
| `us` | URLScan | Historical scans, linked resources |
| `vt` | VirusTotal | Reputation, detection |
| `ab` | AbuseIPDB | IP abuse history |
| `cs` | Censys | Port/banner/tech stack (IP only) |

**Core query with headers:**
```
reload mathteachersforhire.shop --headers
```

**Console enrichment:**
```
mathteachersforhire.shop
enrich vd dd us vt
```

**Pivot to an IP:**
```
<ip-address>
enrich vd ab cs
```

## What to document

As you work, track:
- What the domain is actually serving (tech stack, purpose)
- Who operates it (registrant fingerprints, personal handles)
- What other infrastructure they control (IPs, domains, subdomains)
- Which specific organizations appear to be targeted
- How the operator's infrastructure has evolved over time

## Exercise scope

This is a **six-level exercise**. Each level is complete when you can answer all its questions:

| Level | Focus | Key technique |
|---|---|---|
| 1 | Basic recon | Core query interpretation |
| 2 | Pattern recognition | Subdomains, co-hosted domains, TLD variants |
| 3 | First pivot | PTR lookup → primary operator domain |
| 4 | Infrastructure mapping | Reverse IP on pivot IP, school district targets |
| 5 | Deep analysis | Subdomain analysis, tech stack (Censys), historical IP pivots |
| 6 | Attribution | URLScan chain → GitHub username |

## Exercise questions

See [questions.md](questions.md) — work Levels 1–6 in order, then Bonus.

## What this case demonstrates

- Educational-sounding domain names as a filter evasion technique
- PTR records as a pivot path to primary infrastructure
- TXT records as operator-identifying artifacts
- URLScan historical data as a cross-domain correlation tool
- Registrar fingerprinting across a domain portfolio
- Historical IP pivoting to map infrastructure evolution
- Censys/Shodan for tech stack fingerprinting
- Full attribution chain from anonymous domain to GitHub identity, using passive OSINT only
