# Gaborone Financial Crimes Investigation

## Scenario

You are a digital forensic analyst at the Directorate on Corruption and Economic Crime (DCEC) in Gaborone, Botswana.

**Background:** A tip has been received from Molapo Building Supplies, a construction materials competitor of Kagiso Supplies. The tipster alleges that Kagiso Supplies has been winning procurement contracts they should not be winning, and that there are rumors of corrupt dealings in the award process. Your supervisor has tasked you to investigate.

As a first step, you decide to examine discarded materials from Kagiso Supplies to look for leads.

**Your task:** Search the trash provided by your instructor. Document everything you find. Once you have identified a lead, follow it.

## Starting Point

Physical examination of discarded materials at Kagiso Supplies premises, Gaborone.

## Investigation Path

This is an **eight-phase** exercise. Each phase unlocks the next.

| Phase | Focus |
|---|---|
| 1 | Physical lead and blockchain trace |
| 2 | Exchange legal return and burner account baseline |
| 3 | Burner account content and account correlation |
| 4 | Coinbase Egmont return |
| 5 | Personal account: identity and login records |
| 6 | Personal account: Gmail |
| 7 | Personal account: Drive and Keep |
| 8 | Behavioral trail |

Work through phases in order. New evidence is distributed by your instructor as you establish each prior forensic link.

## Evidence Files

The burner account Google search warrant return is available on the files server:

```
/files/kabelo-motsumi/kabo-seretse-operational.zip
```

Download this when your instructor advises. Additional search warrant returns and documents will be distributed physically at appropriate phases.

## Tools

| Tool | Purpose |
|---|---|
| Public blockchain explorer | Trace the BTC address — blockstream.info or blockchain.com |
| bgp.he.net | ASN and prefix lookups for IP analysis |
| ipinfo.io | Geolocation and ASN attribution, free with login |
| Spur (spur.us) | VPN and datacenter IP classification |
| CyberChef (gchq.github.io/CyberChef) | Extract and deduplicate IPs from documents: paste text → *Extract IP addresses* → *Unique* |
| File browser + text editor | .json, .html, .csv, .txt files in the account returns |
| Spreadsheet application | .xlsx files from Drive exports |
| Web browser | Open Mail/html/ files directly — no email software required |

## What to Document

At each phase, record every identifier you extract: BTC addresses, email addresses, IP addresses, names, account numbers, dates. Note what each one tells you and what it connects to. Leads that appear unresolved early often become critical later.
