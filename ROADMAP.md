# eureka-labs Roadmap

## Immediate

### Port school-proxy case study

A complete challenge set exists in draft form in the StealthOps repo at
`training/case-studies/mathteachersforhire/`. Port it here as `challenges/osint/school-proxy/`.

The draft includes:
- `brief.md` — scenario setup, tool reference, six-level scope description
- `questions.md` — 50 questions across 6 levels + 7 bonus questions
- `walkthrough.md` — complete analyst-grade answer key with full infrastructure map, registrar fingerprint table, operator profile, and timeline
- `raw-data/notes.md` — all 22 queries logged, CTF flag candidate table (14 flags with answers and difficulty ratings)

**Tasks:**
- [ ] Copy and lightly adapt brief.md, questions.md, walkthrough.md into `challenges/osint/school-proxy/`
- [ ] Write `ctfd/challenges.yml` — start with Level 1–4 flags (good scope for first deployment); Level 5–6 and Bonus can be a second tier
- [ ] Decide: publish walkthrough in repo (instructor use) or keep in private branch
- [ ] Write `ctfd/README.md` and `ctfd/docker-compose.yml`

**Available flag answers (from StealthOps raw-data/notes.md):**

| Flag | Answer | Difficulty | Points |
|---|---|---|---|
| IP address of starting domain | `205.209.125.106` | Easy | 50 |
| Open-source proxy named in subdomains | `rammerhead` | Easy | 50 |
| IP of froggies subdomain | `69.164.251.210` | Easy | 100 |
| Operator's primary domain (PTR from froggies IP) | `frogiesarcade.win` | Easy | 100 |
| Registrant state | `Wisconsin` | Medium | 150 |
| Operator email provider | `Zoho` | Medium | 150 |
| Hosting project name (TXT record) | `school-helper101` | Medium | 150 |
| K-12 filter product named as subdomain | `securly` | Medium | 200 |
| Web server on port 80 | `Caddy` | Medium | 200 |
| Number of IPs in load-balanced pool | `5` | Medium | 200 |
| Number of frogiesarcade.win subdomains | `27` | Hard | 250 |
| Number of Express instances on proxy IP | `5` | Hard | 250 |
| GitHub username | `maddox05` | Hard | 300 |
| Oldest operator domain | `maddox.page` | Hard | 300 |

### CTFd infrastructure

- [ ] `ctfd/docker-compose.yml` — CTFd + MariaDB
- [ ] `ctfd/nginx.conf` — TLS termination (mirrors StealthOps deploy pattern)
- [ ] `ctfd/README.md` — deployment steps for GCP e2-medium, certbot, DNS

---

## Planned

### External tools module (extends school-proxy)

The school-proxy case ends where StealthOps ends. A follow-on set covers tools StealthOps doesn't wrap:

| Tool | Technique | What students find |
|---|---|---|
| crt.sh | Certificate transparency | Additional subdomains beyond passive DNS |
| GitHub | Profile OSINT | Repos, commit emails, linked domains from maddox05 profile |
| Wayback Machine | Historical screenshots | What the sites looked like; deleted content |
| Google | Dorking | `"school-helper101"` search; `site:frogiesarcade.win` |
| SecurityTrails | Historical DNS + TXT pivot | Google site verification token across domains |

### New challenge sets

- [ ] **IP characterization** — given a list of IPs, classify each (TOR exit, residential, CDN, shared hosting, data center, anonymous VPN). Teaches Spur, GreyNoise, AbuseIPDB, ipinfo interpretation.
- [ ] **Domain assessment** — given a list of domains, assess legitimacy (legitimate business, brand impersonation, defensive registration, typosquat, phishing, parking). Teaches WHOIS age, registrar patterns, content signals.
- [ ] **Brand impersonation / phishing domain** — start from a reported phishing domain, pivot to infrastructure cluster, identify other lure domains targeting the same brand.
- [ ] **Full pivot chain, different scenario** — new starting domain, different operator profile, different techniques required.
- [ ] **Forensics category** — TBD.
