# Exercise Questions — mathteachersforhire.shop

Work through the levels in order. Each level builds on the previous.

---

## Level 1 — Basic Reconnaissance

Run the core query: `mathteachersforhire.shop`

1. What IP address does the domain resolve to?
2. What hosting provider/ISP controls that IP block?
3. When was the domain registered?
4. What registrar/nameserver provider is being used? What does that suggest about privacy?
5. The WHOIS shows no registrant contact info. Why?
6. What do the MX records tell you about email setup for this domain?

---

## Level 2 — Pattern Recognition

Run enrichment: `enrich vd dd us vt`

7. ViewDNS reports multiple subdomains. List all subdomains you can find.
8. One of the subdomain names is also the name of a well-known open-source browser proxy project used specifically to bypass school web filters. Which one?
9. How many other domains share the same IP address as mathteachersforhire.shop?
10. Review the co-hosted domains. One contains what appears to be a school abbreviation. Name it and speculate about the target.
11. The operator appears to have registered the same brand across multiple TLDs. List the TLD variants you can find.
12. URLScan shows historical scans of the domain. What is the earliest scan date? What does that tell you about when this domain became active?
13. VirusTotal flags this domain. How many engines flag it and as what category?

---

## Level 3 — First Pivot: The Froggies IP

14. One subdomain in the URLScan results resolves to a **different IP address** than the main domain. Which subdomain, and what is that IP?
15. Run a core query against that new IP. What does the PTR (reverse DNS) record reveal?
16. The PTR record points to a subdomain. What is the apex domain? Run a full query on it.
17. What nameserver provider does this apex domain use? How does that differ from the main domain?
18. What state/region is the registrant located in (check WHOIS)?
19. When was this domain first registered? Is it older or newer than mathteachersforhire.shop?
20. What does the MX record reveal about how the operator handles email?
21. The TXT records for this domain contain two notable non-SPF entries. What are they, and what does each enable as a potential pivot?

---

## Level 4 — Infrastructure Mapping: The Froggies IP Cluster

Run ViewDNS reverse IP on the pivot IP from Level 3.

22. How many domains share that IP? How does this compare to the main domain's IP?
23. `use.frogiesarcade.win` resolves to multiple IPs. How many? What does this suggest?
24. Several domains on this IP appear to target specific school districts or educational institutions. List every school/district name you can identify.
25. List all TLD variants of the operator's primary brand that appear in the results.
26. One domain on this IP contains what appears to be a personal name or handle. What is it?
27. The operator uses a custom TXT record that names their hosting project. What is the project name?

---

## Level 5 — Subdomains and Tech Stack

Query frogiesarcade.win with ViewDNS enrichment. For the tech stack, run Censys on `69.164.251.210`.

28. How many subdomains does ViewDNS find for frogiesarcade.win?
29. One subdomain is named after a real K-12 web filtering product that is widely deployed in schools. Name it — and explain the significance.
30. Two subdomains reference a specific proxy protocol used in school-bypass tooling. What are they?
31. Several subdomains are named after characters from a Japanese music franchise. What are the names and what might they suggest about the operator?
32. What web server software is running on port 80 of the primary IP? How does this match the HTTP headers from mathteachersforhire.shop?
33. Censys shows multiple instances of the same application framework running on different ports. What framework, and how many instances? What does this tell you about the architecture?
34. frogiesarcade.win has 5 historical IPs. Pivot on each one via ViewDNS reverse IP. For each, note the hosting provider and any interesting co-hosted domains. Which pivot yields the most useful results?
35. One historical IP reveals three domains registered within 9 days of each other, all at the same registrar. List the domains, registrar, and registration dates.

---

## Level 6 — Attribution: The ubghub.org Chain

36. URLScan history for frogiesarcade.win shows a domain that appears multiple times across different scan sessions. What domain is it?
37. Run a full query on that domain. What registrar is it using? How does that compare to jorkingit.shop and furywars.online?
38. URLScan history for that domain reveals what appears to be a GitHub Pages preview URL. What GitHub username does it reveal?
39. What personal domain does this operator appear to control (also seen in URLScan results)?
40. Query that personal domain. What is its registration date — is it the oldest domain in this cluster?
41. URLScan for the personal domain reveals two more linked domains. What are they? Query each one.
42. One of those domains uses an educational-sounding name with an active subdomain using a different proxy protocol name. What domain and subdomain?
43. Draw the full attribution chain: starting from mathteachersforhire.shop, trace each pivot step to the GitHub username.

---

## Bonus — Analyst Questions

44. What is your overall characterization of this operation? (One paragraph: what is it, who runs it, what's the goal, how sophisticated is it?)
45. The operator has used at least three different registrars across their domain portfolio. List the registrars and which domains use each. Why might an operator use multiple registrars?
46. What does the timeline of domain registrations and hosting migrations tell you about the operator's evolution and intent?
47. The `moonlight.mathteachersforhire.shop` subdomain resolves to a third unique IP. Query it. What is unusual about the network WHOIS for that IP block?
48. If you were a school network administrator, what specific indicators would you add to your blocklist? Be specific: IPs, domains, ASNs, patterns, and any behavioral signatures.
49. What does the presence of `admin.frogiesarcade.win` suggest? What would you do next if you were conducting authorized penetration testing rather than passive OSINT?
50. Three of the school-district domains (austinisd.net, denisonisd.org, columbiapublicschools.org) are plausibly real domain names for those organizations. How would you verify whether these are impersonation domains or legitimate district-registered domains? What's the fastest check?
