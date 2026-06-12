# Walkthrough — Kabelo Motsumi (Procurement Fraud)

**INSTRUCTOR USE ONLY — Do not distribute to students.**

---

## Forensic Chain

Physical trash → blockchain trace → Luno exchange (burner account `k.seretse`) → Orange Botswana residential IP slip → ISP subscriber Kabelo Motsumi → LinkedIn (employer + Kagiso Supplies connection) → Coinbase Egmont return (KYC, bank account) → burner LinkedByCookies → personal Google account (`kabelo.motsumi`) → VPN cutover date → Gmail vendor thread → Drive income ledger → Keep BIP39 mnemonic → behavioral trail (DCEC searches, Gemini prompts)

---

## Phase 1 — Dumpster Dive and Blockchain Trace

**Q1: BTC address from trash**
`3C9akyM5Fb8Av3V2ouVRzcS3ZBJ6tfGoLx`

Found on a crumpled handwritten note: `KM btc: 3C9akyM5Fb8Av3V2ouVRzcS3ZBJ6tfGoLx`. The initials "KM" are noted but not yet explained — they become significant in Phase 5.

**Q2: Primary exchange**
`Luno`

Blockchain analysis shows multiple incoming deposits spaced weeks apart from a single external sending address (`1KgJ7dQxBnZ4R3T...Xm8Yz2` per the Luno return). Funds are swept to exchange custodial infrastructure. Students who follow the sweep addresses, or who receive instructor confirmation, identify Luno — the dominant exchange operating in southern Africa. The spaced-deposit pattern from a single sender is consistent with a recurring payment arrangement.

Luno is reachable via direct legal process (South Africa). Send this request immediately.

**Q3: Second exchange**
`Coinbase`

Outgoing transactions from the deposit address include a sweep to `bc1qa7fp3nt2m8wjsck5hg4vy1ed9r0xzqb6l8up`, which resolves to Coinbase custodial infrastructure (the `bc1q` Bech32 format is common to Coinbase). Because Coinbase is U.S.-regulated, records require an Egmont channel: FIA Botswana submits to FinCEN, which compels Coinbase under the Bank Secrecy Act. The Egmont return takes 2–3 weeks; students should submit this request now in parallel with the Luno request. Distribute `injects/coinbase-egmont-response.pdf` at the start of Phase 4.

---

## Phase 2 — Exchange Legal Return and Burner Account Baseline

Distribute `injects/luno-legal-return.pdf` and `kabo-seretse-operational.zip`.

**Q4: Luno account email**
`k.seretse@kgale-mail.test`

From the Luno legal return, Account Information section. The account is registered under the fictitious persona "Kabo Seretse." No employer, no phone, no biographical depth.

**Q5: Luno account created**
`28 August 2025`

From the Luno legal return. The account was created recently relative to the deposit history, confirming it was purpose-built for the scheme. The Luno login records show four sessions — all from AS39351 31173 Services AB (Mullvad VPN) across UK, Germany, and Netherlands. The subject was disciplined about the exchange: he never logged in to Luno without VPN. The Google subscriber info tells a different story.

**Q6: Residential IP slip**
`41.138.76.55`

From the burner account's Google SubscriberInfo HTML (`kabo-seretse-operational/[email].GoogleAccount.SubscriberInfo_001/Google Account/[email].SubscriberInfo.html`). All other sessions are from AS39351 (Mullvad VPN). This single login geolocates to Orange Botswana — a Gaborone residential ISP — and does not match any commercial ASN.

CyberChef tip for students: open the SubscriberInfo HTML in a browser, copy the IP Activity table, paste into CyberChef, apply *Extract IP addresses* → *Unique* to get a clean list for ASN lookup.

Distribute `injects/orange-isp-subscriber-return.pdf` once students have identified this IP and looked it up on bgp.he.net or ipinfo.io.

**Q7: ISP subscriber name**
`Kabelo Motsumi`

From the Orange Botswana subscriber return. IP `41.138.76.55` was assigned to Kabelo Motsumi, Plot 5672, Extension 12, Gaborone continuously from 1 January 2025 to 22 May 2025. Last observed activity: 22 May 2025, 23:47 CAT — the day before the VPN cutover on the personal account.

Distribute `injects/linkedin-kabelo-motsumi.pdf` once students have read the ISP return and know the subscriber name. The LinkedIn profile confirms employer (TlouKago Construction Supplies) and surfaces Tshepiso Kgosi (Kagiso Supplies) under "People also viewed." Students should record this connection even if its significance is not yet clear.

---

## Phase 3 — Burner Account Content and Account Correlation

**Q8: VPN provider**
`Mullvad`

From the burner account search history (`kabo-seretse-operational/My Activity/Search/MyActivity.html`). The search sequence is entirely operational: Mullvad download page, whether a crypto exchange logs VPN IPs, Mullvad no-log policy, how to delete Google account activity permanently, "Luno login IP logs law enforcement request." The last search shows direct awareness of legal exposure. No personal browsing, no entertainment, no social media — this account has no life outside of concealment research.

**Q9: Linked real account (LinkedByCookies)**
`kabelo.motsumi@kgale-mail.test`

From the LinkedByCookies CSV in the burner account's GoogleAccountTargetAssociation folder. The file lists one relevant entry: `kabelo.motsumi@kgale-mail.test`. Both accounts were active in the same Chrome session on the same physical machine. The LinkedByPhone and LinkedBySecondaryEmail files for the burner account independently corroborate this — both also list `kabelo.motsumi@kgale-mail.test`, because the same phone number (+267 74 962 195) and recovery email were used to set up both accounts.

This is a triple correlation (cookies + phone + secondary email) that is very difficult to explain away.

Distribute `kabo-seretse-operational.zip` is already in hand. Hold the personal account return (`kabelo-motsumi-personal.zip`) until students have established: (a) the LinkedByCookies link; (b) the ISP subscriber name; and (c) that the initials "KM" from the trash note match "Kabelo Motsumi."

---

## Phase 4 — Coinbase Egmont Return

Distribute `injects/coinbase-egmont-response.pdf`.

**Q10: Coinbase KYC name**
`Kabelo Kefilwe Motsumi`

From the Egmont return, Account Information section. Unlike the Luno account (pseudonym, VPN), the subject used his real name, real passport (BP-1038845), real residential address (Plot 5672, Extension 12, Gaborone), and real email on Coinbase. The middle name "Kefilwe" does not appear elsewhere in the dataset and serves as an additional corroborating identifier for any prosecution document.

Opsec failure discussion: the subject applied careful opsec to Luno (the locally reachable exchange) but apparently did not anticipate that (a) blockchain analysis would trace the second-hop address to Coinbase, or (b) that a U.S.-regulated exchange was reachable through the Egmont channel. The most disciplined cover breaks down where the subject didn't know the legal process existed.

**Q11: Coinbase BTC address**
`bc1qa7fp3nt2m8wjsck5hg4vy1ed9r0xzqb6l8up`

From the Egmont return. This is the same second-hop address students identified on the blockchain in Phase 1. Students should confirm the match. The personal Gmail also contains a Coinbase activation email (002 Mar 2025) independently listing this address — corroborating the Egmont return with data the subject created himself.

**Q12: Wire account ending**
`4219`

From the Egmont return. Five BTC-to-USD liquidations were wired to Stanbic Bank Botswana, account ending 4219. Total wired: $8,881.00 across five transactions. This account number reappears in the personal Gmail bank alert (Phase 6), independently corroborating the Egmont data.

---

## Phase 5 — Personal Account: Identity and Login Records

Distribute the `kabelo-motsumi-personal` search warrant return once students have confirmed all three: LinkedByCookies link, ISP subscriber name, and "KM" initials resolved.

**Q13: Personal account name**
`Kabelo Motsumi`

From the personal account SubscriberInfo HTML. The registered name resolves the "KM" initials from the trash note. The alternate email (`kabelo.motsumi@tloukago.test`) confirms the employer connection without needing the LinkedIn profile.

**Q14: Employer**
`TlouKago Construction Supplies`

Confirmed from the personal account's work email domain (`tloukago.test`) and the LinkedIn profile. The LinkedIn profile also lists Tshepiso Kgosi under "People also viewed" — Sales Representative at Kagiso Supplies. This connection, first noted at Phase 2 as an unresolved lead, is confirmed in Phase 6 when the Gmail thread is opened.

**Q15: VPN cutover date**
`23 May 2025`

The personal account's IP Activity table shows logins from `41.138.76.55` (Orange Botswana) through mid-May 2025, then VPN-routed logins from late May onward. The Coinbase Egmont return states explicitly: "residential to 23 May 2025; VPN-routed thereafter." The search history corroborates: the first DCEC search was on 23 May 2025. The Orange ISP return shows last observed activity on `41.138.76.55` as 22 May 2025, 23:47 CAT.

All three sources converge on 23 May 2025 as the inflection point — the day the subject became concerned about legal exposure and changed his behavior across all platforms simultaneously.

The personal account's LinkedByCookies file does NOT list the burner account. It lists a work email, an archive account, and `mpho.motsumi@gmail.test` (a family member sharing the device). However, LinkedByPhone and LinkedBySecondaryEmail on the personal account both list `k.seretse@kgale-mail.test` — the same phone number and recovery email were registered to both accounts. The phone/secondary email link is bidirectional; the cookie link is one-directional (burner sees personal; personal does not see burner because the burner was created after the cookie session that linked them was established). Use this as a discussion point about what different association types capture.

---

## Phase 6 — Personal Account: Gmail

**Q16: Vendor email address**
`tshepiso.kgosi@kagisosupp.test`

Tshepiso Kgosi, Sales Representative at Kagiso Supplies (per LinkedIn). Key emails in the thread:

- `006` (07 Mar 2025): "Revised Quote — Q1 Steel Order" — "further to our conversation last week... Looking forward to a continued relationship"
- `037` (09 Apr 2025): "Adjusted copy" — "Use this version when forwarding to accounts. Same arrangement as before. — T."
- `040` (10 Apr 2025, sent from work address): "Q2 Steel Supply — Vendor Recommendation" — Kabelo emails his manager recommending Kagiso Supplies for the Q2 contract
- `064` (14 May 2025): "Re: batch" — "keep this off the work thread. Accounts is asking questions about the last batch. Use the personal address going forward."
- `067` (16 May 2025): "Re: April arrangement" — Kabelo writes back: "April payment has not reflected yet. We agreed on the 15th."

Also relevant:
- `001` (02 Mar 2025): Coinbase activation — independently confirms BTC address `bc1qa7fp3nt2m8wjsck5hg4vy1ed9r0xzqb6l8up`
- `020` (18 Mar 2025): Luno identity verified — personal Luno account, wallet `3QNgmHpV6ApJ7r9kMt8cXuHwJzLsFbnEd` (separate from the burner's Luno account)
- `090` (07 Jun 2025): Bank credit alert — account ending 4219 credited BWP 6,500.00, description "consulting"; no consulting work or clients appear anywhere else in the dataset

**Q17: Implication phrase**
`keep off the work thread`

From `064_re-batch.html` (14 May 2025). Full message: "Kabelo — one thing: keep this off the work thread. Accounts is asking questions about the last batch. Use the personal address going forward, not the office chain. — T."

This is direct evidence of consciousness of impropriety from both parties. The instruction to move communications to personal channels demonstrates that both Tshepiso and Kabelo understood the arrangement was improper and were actively managing their exposure.

---

## Phase 7 — Personal Account: Drive and Keep

**Q18: Income tracker filename**
`side_income_tracker.xlsx`

Located in `Drive/Personal Admin/`. A 30-row spreadsheet recording payments by date, amount, and source. Entries corroborate the Orange Money notifications and bank alerts in Gmail. Self-authored evidence is particularly valuable because it demonstrates knowledge and intent — the subject was tracking receipts for personal reconciliation, which means he knew exactly what he was receiving and from whom.

`crypto_notes.txt` is also present in Drive, connecting the subject's knowledge of cryptocurrency mechanics to the Luno account activity visible in Gmail.

**Q19: Wallet recovery note title**
`Backup`

A Keep note containing 12 dictionary words in a fixed sequence — a BIP39 mnemonic. The title is deliberately innocuous. Only students who recognise the format (12 ordinary English words, not a sentence) will flag it. Prompt any students who don't recognise it: what would 12 random dictionary words stored in a note titled "Backup" most likely be?

This note proves Kabelo held custody of the seed phrase for a Bitcoin wallet. The wallet address from the trash note (`3C9akyM5Fb8Av3V2ouVRzcS3ZBJ6tfGoLx`) is the same address on the Luno legal return. The "Backup" Keep note in the personal account is the recovery key for that wallet — connecting Kabelo's personal account to direct custody of the wallet that received the Kagiso Supplies payments.

---

## Phase 8 — Behavioral Trail

**Q20: First legal search date**
`23 May 2025`

Search: "DCEC Botswana how do investigations start." This is the first of five DCEC-related searches that document the subject's progression from concern to fear to legal strategy:

| Date | Search |
|---|---|
| 23 May 2025 | DCEC Botswana how do investigations start |
| 09 Jun 2025 | how long does DCEC investigation take Botswana |
| 15 Jun 2025 | procurement officer corruption sentence Botswana |
| 20 Jun 2025 | Corruption of Public Officers Act Botswana penalty |
| 18 Aug 2025 | DCEC plea agreement cooperation deal Botswana |

The arc is clear: investigation procedures → timelines → sentences → penalties → plea arrangements. Over three months the subject moved from curiosity about how investigations work to actively researching cooperation deals.

This date (23 May 2025) is the same as the VPN cutover on the personal account and the last observed activity on the Orange Botswana residential IP. Something triggered a change in behaviour across all platforms on 23 May 2025.

**Q21: Gemini prompt (consciousness of guilt)**
`what does a procurement fraud investigation typically look for`

Submitted June 2025. The three forensically relevant Gemini prompts in chronological order:

| Date | Prompt |
|---|---|
| March 2025 | explain how cryptocurrency transactions work and whether they can be traced |
| May 2025 | can deleted Google account activity be recovered by investigators |
| June 2025 | what does a procurement fraud investigation typically look for |

The June prompt is the most legally significant. It demonstrates the subject actively modeling the investigation against his own conduct. Combined with the DCEC search timeline, it establishes a documented progression of legal awareness directly relevant to consciousness of guilt under Botswana criminal procedure.

---

## Key Artifacts Summary

| Artifact | Source | What it proves |
|---|---|---|
| Handwritten note `KM btc: ...` | Physical — trash at Kagiso Supplies | Entry point; unresolved initials; links physical scene to a crypto wallet |
| Blockchain transaction record | Public explorer | Spaced deposits from single sender; sweeps to Luno and Coinbase |
| Luno legal return | `injects/luno-legal-return.pdf` | Account `k.seretse@kgale-mail.test`; created 28 Aug 2025; all Luno login IPs from Mullvad VPN |
| Residential IP slip `41.138.76.55` | `kabo-seretse-operational/` SubscriberInfo | One login breaks the VPN pattern; geolocates to Orange Botswana, Gaborone |
| Orange Botswana ISP return | `injects/orange-isp-subscriber-return.pdf` | IP attributed to Kabelo Motsumi, Plot 5672; assignment through 22 May 2025 |
| LinkedIn profile | `injects/linkedin-kabelo-motsumi.pdf` | Confirms employer TlouKago; surfaces Tshepiso Kgosi (Kagiso Supplies) |
| Coinbase Egmont return | `injects/coinbase-egmont-response.pdf` | KYC: Kabelo Kefilwe Motsumi; real passport and address; 5 wires to Stanbic 4219; VPN cutover 23 May 2025 |
| LinkedByCookies | `kabo-seretse-operational/` Account | `kabelo.motsumi@kgale-mail.test` on same device; confirmed by LinkedByPhone and LinkedBySecondaryEmail |
| Personal account SubscriberInfo | `kabelo-motsumi-personal/` Account | Name Kabelo Motsumi; employer TlouKago; residential IP `41.138.76.55` throughout; VPN from 23 May 2025 |
| Vendor email thread | `kabelo-motsumi-personal/` Mail | Direct link to Kagiso Supplies; "same arrangement"; "keep off the work thread" |
| Bank credit alert (BWP 6,500) | `kabelo-motsumi-personal/` Mail | Account 4219 credited "consulting" 07 Jun 2025 — no consulting in the dataset |
| Coinbase activation email | `kabelo-motsumi-personal/` Mail | Independently confirms BTC address `bc1qa7fp3nt2m8wjsck5hg4vy1ed9r0xzqb6l8up` |
| `side_income_tracker.xlsx` | `kabelo-motsumi-personal/` Drive | Self-maintained payment ledger; self-authored evidence of knowledge and receipt |
| Keep note "Backup" (BIP39 mnemonic) | `kabelo-motsumi-personal/` Keep | Recovery phrase for the Luno wallet from the trash; proves custody |
| Legal awareness searches | `kabelo-motsumi-personal/` Search | DCEC → sentences → plea arrangements; documented progression of legal risk awareness |
| Gemini prompt (Jun 2025) | `kabelo-motsumi-personal/` Gemini | "what does a procurement fraud investigation typically look for" — consciousness of guilt |

---

## Bonus — Case Summary Notes

A strong student summary should cover:

**The scheme:** Kabelo Motsumi, Procurement Officer at TlouKago Construction Supplies, steered purchase orders to Kagiso Supplies in exchange for regular payments routed through Orange Money, bank transfers, and Bitcoin.

**Payment channels:** Orange Money transfers (corroborated by Gmail notifications and the income tracker); bank credits to Stanbic account 4219 described as "consulting" (corroborated by the Egmont return); BTC received at the Luno burner wallet and liquidated via Coinbase to the same Stanbic account.

**Concealment attempt:** Purpose-built burner Google account under a fictitious name and email domain; Mullvad VPN on all Luno sessions and on both accounts after 23 May 2025. The subject apparently did not anticipate blockchain tracing revealing the second-hop Coinbase address, or the existence of the Egmont channel to compel a U.S. exchange.

**Where opsec failed:**
- Single residential IP login in the burner Google account
- Real-name KYC on Coinbase with wire directly to a named Botswana bank account
- LinkedByCookies bridging the burner to the personal account on the same device
- Personal Gmail containing direct evidence of the arrangement the subject created himself
- Self-maintained income tracker
- BIP39 mnemonic stored in Keep connecting the personal account to custody of the burner wallet

**Evidence priority for criminal referral:**

1. **Coinbase Egmont return** — real identity, real passport, real address, bank account, transaction records. Produced by a U.S. exchange under legal compulsion; highly credible.
2. **Orange ISP return** — independently attributes the residential IP to the subject by name and address; corroborates the cookie correlation.
3. **Vendor email thread** — direct communication evidencing the arrangement and Kabelo's awareness of its impropriety ("keep off the work thread").
4. **`side_income_tracker.xlsx`** — self-authored; demonstrates both knowledge and receipt; corroborates third-party financial records.
5. **Legal awareness searches and Gemini prompts** — consciousness of guilt; documents the subject's real-time risk assessment.

Self-authored evidence (the income tracker, "April payment has not reflected," the Gemini prompts) is primary. It demonstrates knowledge and intent in a way that third-party records cannot replicate, and it is created by the subject — meaning it cannot be attributed to investigator error or fabrication.
