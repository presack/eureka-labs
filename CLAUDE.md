# eureka-labs — Claude Context

## What this repo is

CTF-style cybersecurity training challenges for students. Hands-on exercises in OSINT, digital forensics, penetration testing, and related disciplines. Built around real targets and real pivot chains — not contrived puzzles.

Primary investigation tool is StealthOps (github.com/presack/StealthOps), though challenges may use other tools (crt.sh, Shodan, GitHub OSINT, Wayback Machine, etc.). Deployed via CTFd, an open-source self-hosted CTF platform.

Target audience: students learning practical cybersecurity investigation skills.

## Repo structure

```
eureka-labs/
├── CLAUDE.md
├── ROADMAP.md
├── challenges/
│   ├── osint/
│   │   └── school-proxy/          ← first complete challenge set
│   │       ├── brief.md           ← student-facing scenario (no spoilers)
│   │       ├── questions.md       ← tiered questions (no answers)
│   │       ├── walkthrough.md     ← instructor answer key
│   │       └── ctfd/
│   │           └── challenges.yml ← CTFd import file
│   ├── forensics/                 ← planned
│   └── pentesting/                ← planned
├── ctfd/
│   ├── docker-compose.yml         ← CTFd deployment
│   ├── nginx.conf                 ← TLS termination
│   └── README.md                  ← deployment instructions
└── tools/                         ← helper scripts (planned)
```

## Challenge categories

| Category | Description | Status |
|---|---|---|
| `osint/` | Passive recon, domain/IP investigation, pivot chains, attribution | Active |
| `forensics/` | Digital artifact analysis | Planned |
| `pentesting/` | Authorized assessment techniques | Planned |

## Challenge set format

Each challenge set lives in `challenges/<category>/<case-name>/` and contains:

1. **`brief.md`** — Scenario framing with no spoilers. Sets the scene, names the starting indicator, lists available tools. What the student reads first.
2. **`questions.md`** — Tiered questions (Level 1 through Level N + Bonus). No answers included.
3. **`walkthrough.md`** — Complete analyst-grade answer key with all pivot data, infrastructure maps, and instructor notes. Not published to students.
4. **`ctfd/challenges.yml`** — CTFd import file. One entry per scoreable flag.

## CTFd challenge format

```yaml
- name: "Challenge title"
  author: presack
  category: "OSINT - School Proxy"
  description: |
    Scenario context and question text for the student.
  value: 100
  type: standard
  flags:
    - type: static
      content: "flag-answer-here"
      data: case_insensitive
  hints:
    - content: "Hint text"
      cost: 10
```

Flags are raw answer strings — no `flag{...}` wrapper. This is a training context, not a competition. CTFd configured with case-insensitive matching.

Point values scale with difficulty: Level 1–2 = 50–100 pts, Level 3–4 = 150–200 pts, Level 5–6 = 250–300 pts, Bonus = 400 pts.

## CTFd deployment

See `ctfd/README.md`. Docker Compose + nginx + Let's Encrypt, same pattern as StealthOps cloud deployments. Can run on a shared VM alongside a StealthOps TRAINING_MODE instance (e2-medium recommended for both) or independently.

## Relationship to StealthOps

StealthOps (github.com/presack/StealthOps) is the investigation tool students use to work the challenges. This repo contains challenge content only — no StealthOps code. The first challenge set (`osint/school-proxy`) was developed entirely using StealthOps and all pivot data was collected with it during a real investigation session.

## Design philosophy

- **Real targets, real data.** Challenges use actual domains and IPs with documented real-world behavior.
- **Tiered difficulty.** Each case study has 4–6 levels, each building on the previous. Students who get stuck can still make progress.
- **Walkthroughs are full writeups.** Not just answer lists — complete analyst-grade documentation of the pivot chain. The walkthrough is as valuable as the challenge.
- **Tools are part of the learning.** Questions are written to teach the tool as well as the technique.
