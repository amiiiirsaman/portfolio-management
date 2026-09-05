# Portfolio & Resume Refresh — September 2026

**Slug:** `portfolio-refresh-2026-09` · **Type:** feature (content + small behavior changes) · **Status:** approved 2026-09-05 (answers to the four approval questions) · delivered, see resolution.md

## Introduction

The site at sammahdavian.ai and the resume (v8, July 2026) need a targeted refresh before Sam sends the portfolio to Falon Fatemi, a General Partner at Digital Indies. Her LinkedIn post (photo dated 2026-09-05) asks for two kinds of people: engineers who are "deep in multi-level agentic systems, orchestration, memory, tool use and autonomous workflows" and who apply that to real businesses rather than demos, and seasoned founders or operators who have built and run real companies. Sam fits both lanes. The current site already argues "agentic AI that solves the business problem"; what it does not do yet is show the *agent-specialization discipline* (the Claude skills system), surface the four newest engines, or carry current numbers.

The refresh is deliberately **surgical, not a redesign**. Per Sam's instruction, the portfolio must not be reshaped around one post. The same structure, palette, and voice stay. The edits add or sharpen facts so that a reader arriving from that post finds every box ticked without the page looking tailored to them: dark mode by default, a Skills section that explains how agents are specialized through authored skills and why that matters, four newer engines added or updated in the Work section (Brane AI, the AI Claims Testing Pilot, SpendSphere, the Deck Builder), refreshed research metrics, a skills-count stat beside the agent-count stat, no client names anywhere, and a resume that says the same things.

Two facts found during investigation change the plan and are covered below: the four repositories Sam named are all **private** on GitHub (a public link would 404 for any visitor), and the live site already has three GitHub links that point at repositories that do not exist plus two that point at private ones.

## Investigation Summary

- **Site:** one static file, `index.html`. Light theme is the default; the toggle does not persist and ignores the system preference. Project content is a JavaScript array of 42 entries; the home page features 7 of them by name-key. The Skills view has a small card "02b Claude Skills · Agent Specialization" listing skill names that are out of date (my-builder, my-observer, my-roadmap) and says nothing about what a skill is or why it helps.
- **Numbers on the site today vs. verified today:** research citations 451 → Google Scholar now shows **460**; h-index 9 → **10**; i10-index 10. "110+ specialized agents" appears in hero, About, meta description, and resume. Sam's instruction says 150+.
- **Client names:** the site has one explicit client name, "a Blue Cross Blue Shield plan", in the Doczy entry. The rest are anonymized descriptors (a New York health plan, a Fortune 500 airline, a global rail-equipment manufacturer, a national Medicaid health plan, an S&P 500 manufacturer). The resume names employers (AArete, SPLUSM/Brane, Stratus, UCF) and only anonymized clients.
- **GitHub links on the site:** 15 unique. Ten resolve to public repos. **Three are broken** (`financial-contract-analyzer-main`, `agentcore_deployment-main`, `advanced-strands-agent-main`; the real repos have no `-main` suffix). **Two point at private repos** (`deck-builder-v1`, `procurement-knowledge-hub`) and 404 for visitors.
- **The four named repos (all private):**
  - `Brane-AI` (TypeScript) — the Brane Mobility monorepo now carrying **Brane AI**, a data-center siting and approval-intelligence platform for the Central Florida I-4 corridor: screens every census block group in three counties against 35 indicators, prices the mitigations that make a site approvable, and runs two journeys (developer allocation, county/utility evaluation) over one scoring object. Every on-screen number is reproducible through the product's own API (tested gate). Marketing line from its README: replaces a $200K, three-month consultant study with minutes. Repo text uses "synthetic"/"demo" for its Phase-1 data; per Sam, those words will not appear on the site.
  - `AI-Powered-Claims-Testing-Pilot` (Python) — independently prices what each Medicaid claim should pay from contract text and published rate files, generates executable test claims, compares against the payer. Verified figures in its decision log: **394 traceable test cases** from **102 contract rules**, backtested against **213,420 historical claim lines**, **460+ automated tests**, deterministic (no LLM in the pricing chain), one-command regeneration, 29 project skills. The README names the client (MetroPlus); the site will not.
  - `aarete-intel-engine` (TypeScript) — **SpendSphere**: browser-native spend-intelligence platform (React + DuckDB-WASM, zero external requests for core function) covering AP spend, 240K MRO parts lines, payer vendor cost reduction, plus an agentic analyst that writes and runs real SQL and cites its figures. Release gated by a 160+ check browser smoke suite driven by six project skills. Repo holds real client data; must stay private.
  - `deck-builder-v1` (TypeScript) — skills-driven deck pipeline (intake → ingest → calc → plan → compose → QC gate → render → validate) where "skills carry the judgment, scripts carry the precision"; every dollar traced to source or the build stops. Repo contains the firm's PowerPoint template and seeded logins; must stay private.
- **Skills count, verified on disk:** 21 personal skills under `~/.claude/skills/` and ~115 project-skill folders across repos on D:\ (about 90 unique names after removing the vendored `my-*` copies). "50+" is conservative and defensible.
- **Resume:** v8 PDF was produced in LibreOffice Writer. No `.docx`/`.odt` source exists in the repo or in the usual folders on this machine.

## Affected Areas & Files

| Area | File | Change |
|---|---|---|
| Theme default + persistence | `index.html` (head CSS, `/* F7 dark mode */` script) | dark by default, remember toggle |
| Hero KPIs, creds, meta tags | `index.html` (`.kpis`, `.creds`, `<meta>`) | 150+ agents, 50+ skills, 460 citations, h-index 10 |
| Skills view | `index.html` (`#view-skills`, card 02b) | rewrite as "Skills & agent specialization" card with explanation |
| Project data | `index.html` (`P`, `FEATURED`) | add Brane AI, SpendSphere; update Claims Testing, Deck Builder; fix 5 links; remove client name; featured 7 → 10 |
| About text | `index.html` (`#view-about`) | numbers only |
| Resume | new `resume/Sam_Mahdavian_Resume.docx` (source) → `Sam_Mahdavian_Resume_20260905.pdf`; update the 3 PDF hrefs | v9 |
| Deliverable hygiene | `specs/…`, `.gitignore` | data-guard scan before anything is committed |

## Requirements

### R1 — Dark mode is the default
- WHEN a first-time visitor loads the page THEN the system SHALL render the dark theme without a flash of the light theme.
- WHEN a visitor toggles the theme THEN the system SHALL remember the choice in the browser (localStorage) and apply it on the next load.
- IF the visitor has never toggled THEN the system SHALL use dark regardless of the operating-system preference (explicit instruction: dark is the default).
- WHEN the page is printed (one-pager) THEN the system SHALL keep the existing light print stylesheet behavior.

### R2 — Hero stats include skills beside agents, and research metrics are current
- WHEN the home page renders THEN the KPI strip SHALL show "150+ specialized agents" and, immediately beside it, "50+ Claude skills authored" (the label may read "agent skills authored" if the word Claude is too narrow; see Q in Approval).
- WHEN any research metric appears (hero KPI, creds link, About "at a glance", About prose, resume) THEN it SHALL read **460 citations** and **h-index 10** (Google Scholar, 2026-09-05).
- WHEN "110+" agents appears anywhere on the site or in meta tags THEN it SHALL be replaced by "150+" so all surfaces agree.

### R3 — Skills section explains agent specialization and its benefit
- WHEN a visitor opens Skills THEN card 02b SHALL be replaced by a card titled "Skills & agent specialization" containing: (a) a one-sentence definition of a skill (a versioned, testable procedure with a trigger, ordered steps, gates, and references that a Claude agent loads on demand); (b) how agents are specialized (workflow skills such as deliverer, tester, investigator, roadmap; capability skills such as data-guard, engine-kit, observatory; domain skills per engine such as onboard-contract, rate-lookup, deck-compose, release-gate); (c) the benefit in three short claims: repeatable engines a teammate regenerates from a clean clone, gates that fail loudly before anything ships, and a strict split between LLM judgment and deterministic precision; (d) the "50+ skills" figure.
- WHEN the card renders THEN it SHALL fit the existing `.skillcard` visual language (chips + one short paragraph); no new section, no new layout.
- WHEN the card lists skills THEN the stale names (my-builder, my-observer, my-roadmap) SHALL be replaced by the real ones (my-deliverer, my-tester, my-investigator, my-roadmap-author/advance, my-observatory, my-data-guard, my-engine-kit, my-skillsmith).

### R4 — Four engines added or updated in Work; featured list grows to ten
- WHEN Work renders THEN `P` SHALL contain a **Brane AI** entry (Founder & Enablement sector, tag "Founder · Brane AI · 2026") describing a data-center siting and approval-intelligence platform: 35 indicators, three counties, two journeys over one scoring object, priced mitigations, approvability score, decision-support framing, every number reproducible through the product API. The words "synthetic", "demo", "mock", "frozen" SHALL NOT appear in it.
- WHEN Work renders THEN the existing "AI Claims Testing Engine · Payer Configuration" entry SHALL be updated to the pilot's verified facts (394 traceable test cases from 102 rules, 213,420 historical claim lines backtested, 460+ automated tests, deterministic pricing with no LLM in the derivation chain, one-command regeneration) and SHALL carry the KPI "~100× faster test-case authoring than hand-written" as Sam's stated figure.
- WHEN Work renders THEN `P` SHALL contain a **SpendSphere · Spend Intelligence Platform** entry (Procurement & Spend sector) and the **AI Deck Builder** entry SHALL be updated to the skills-driven pipeline with its QC gate.
- WHEN the home page renders THEN `FEATURED` SHALL list ten items in this order: 01 Doczy, **02 Brane AI**, **03 AI Claims Testing**, 04 Policy Audit, 05 Fortune 500 Airline (renamed per R5), 06 PADU, 07 SpendSphere, 08 Deck Builder, 09 Multi-Agent Fraud, 10 Credit Risk; and the heading "Seven that show the range" SHALL become "Ten that show the range".
- WHEN a project has no public repository THEN its card SHALL show a "private · walkthrough on request" badge instead of a Code link (no link to a private URL).

### R5 — No client names; better project names
- WHEN the site renders THEN no client organization name SHALL appear anywhere (the Blue Cross Blue Shield mention becomes "a national Blue-plan payer" → see Approval question; default: "a large regional health plan").
- WHEN a project name or tag currently leads with a client descriptor ("Fortune 500 Airline Spend Analysis", tag "New York health plan · Signed SOW 2026", "MRO Spend Intelligence · Rail Manufacturing", tag "Global rail-equipment manufacturer") THEN it SHALL be renamed to a product-style name (e.g., "TailSpend · Supplier Intelligence Engine", "Claims Testing Engine · Contract-to-Test Pipeline", "MRO Spend Intelligence · Parts & Vendor Analytics") with the industry kept in the tag ("Aviation · Production", "Medicaid managed care · Pilot 2026", "Rail manufacturing · 2026").
- WHEN the resume renders THEN it SHALL keep employer names and anonymized client descriptors exactly as v8 does (no client names are present today).

### R6 — Every external link resolves
- WHEN any GitHub link on the site is followed THEN it SHALL return a public repository (three `-main` links fixed to their real names; two private-repo links replaced by the private badge from R4).

### R7 — Resume v9 matches the site
- WHEN the resume is regenerated THEN it SHALL: change 110+ → 150+ agents; 451/9 → 460/10; add "50+ authored Claude skills" to the Agentic AI competency line; add one bullet under AArete for the Claims Testing pilot with the 100× figure and the 394/102/213,420 facts; add Brane AI to the Brane entry (data-center siting platform, 2026) and change that entry's dates to "2020 – Present" **only if Sam confirms**; keep to two pages; keep all v8 hyperlinks.
- WHEN the site links to the resume THEN all three hrefs SHALL point at the new dated file, and the previous file SHALL remain in the repo so old links still work.
- WHEN the resume source is created THEN it SHALL be committed as an editable `.docx` under `resume/` so v10 does not start from a PDF again.

### R8 — Deliverable hygiene
- WHEN the work is complete and before Sam commits THEN a data-guard scan SHALL run over `index.html`, the resume PDF, and `specs/` and report zero PHI/PII and zero client names.

## Implementation Plan (non-binding)

**Approach.** All site edits are made in place in `index.html` with the file's CRLF endings preserved. Content edits are data edits to the `P` array and small HTML edits; the only behavior change is a ~6-line theme bootstrap placed in `<head>` so dark applies before first paint. The resume is rebuilt as a `.docx` mirroring v8's layout (my-word skill), converted to PDF with LibreOffice headless (the same producer as v8), and verified by text extraction. Nothing is committed or pushed; files changed are reported.

**Planned changes (ordered).**
1. `index.html` head: add `<script>` before `<style>` that sets `data-theme` from localStorage or defaults to `dark`; update `setTheme()` to persist; set the toggle glyph accordingly. Add `color-scheme` meta for form controls.
2. `index.html` meta description / og:description: 110+ → 150+, add skills phrase.
3. Hero `.kpis`: 110+ → 150+; insert `50+ / Claude skills authored` KPI directly after it; 451 → 460; 9 → 10. `.creds`: "460 citations · Scholar". About prose and at-a-glance: same numbers.
4. Skills card 02b → "Skills & agent specialization" (R3), same markup pattern.
5. `P`: add Brane AI and SpendSphere objects (with `arch` flow arrays in the existing format); update Claims Testing and Deck Builder objects; rename per R5; fix the three `-main` links; replace two private links with `pub:false` + badge (add a tiny `private` badge alongside the existing `badge-pub` style); remove the Blue Cross Blue Shield phrase.
6. `FEATURED` → ten keys; heading text; palette label "Work · 30+ projects" → "40+" (P will be 44).
7. Resume: build `resume/Sam_Mahdavian_Resume.docx` from v8's extracted text with the R7 edits; `soffice --headless --convert-to pdf`; save as `Sam_Mahdavian_Resume_20260905.pdf`; update the 3 hrefs.
8. Gates: grep for client names and banned words; `gh api` on every GitHub link; pypdf text check; data-guard scan.

**Optional, outside the site (not started unless asked):** a four-sentence LinkedIn DM to Falon Fatemi that names what was built and what Sam would want to run, linking the portfolio. Her name is spelled **Falon**, not Felon.

**Risks & unknowns.** The 150+ agent figure and the ~100× figure are Sam's; the site will state them without a footnote, so they need to be numbers Sam will defend in conversation. The Brane entry's date range on the resume is a factual question only Sam can answer. LibreOffice availability on this machine is unverified (v8's producer suggests it is installed).

## Adversarial Review of This Plan

Things that could make this refresh backfire, and how the plan handles each:

1. **Linking private repos would look careless to exactly this reader.** A GP who clicks "Code" and gets a 404 concludes the portfolio is unmaintained. The site already has five such links today. Fix: R6 and the private badge. Making the repos public instead is *not* recommended: `aarete-intel-engine` holds real client spend data, the Claims pilot README names the client, and `deck-builder-v1` ships the firm's template and seeded logins.
2. **Inflating numbers is the fastest way to lose an operator's trust.** Jumping 110+ → 150+ agents and adding "~100×" with no basis invites the one question that ends the conversation. Mitigation: the Claims KPI cites the concrete facts (394 cases, 102 rules, 213,420 lines) next to the ratio; the plan asks Sam to confirm both figures at approval rather than assuming.
3. **"Don't change it dramatically" vs. "answer her post."** The temptation is to add an "agentic workforce" banner. That would read as tailored and cheapen the page. Instead, the three things her post asks for are already answerable with facts we are adding anyway: orchestration/memory/tool use (Skills card + engine entries), real businesses not demos (Claims pilot, SpendSphere, Brane AI all in production or pilot with named outcomes), founder/operator (Brane AI as a 2026 founder entry, 0→25 team already on About). No new section, no new copy addressed to her.
4. **Removing every descriptor makes the work look fake.** "A health plan" three times reads like filler. Plan keeps industry and scale ("Medicaid managed care", "Fortune 500 airline" in tags only) and removes names. Sam decides the line (Approval question 2).
5. **Dark default can break contrast or the print one-pager.** The dark token set already exists and has been visible via the toggle, but the video poster, the signature mask, and the `.creds` hover were tuned for light first. Test plan checks these. The print stylesheet forces light tokens, unaffected.
6. **Flash of light theme.** Setting the theme in the existing script at the bottom of the body would flash. Plan puts the bootstrap in `<head>` before CSS.
7. **Rebuilding the resume from a PDF risks silent drift.** Fix: extracted v8 text is the source of truth; a diff of v8 text vs v9 text is part of the test plan, and the `.docx` becomes the versioned source.
8. **Brane AI positioning contradiction.** The repo's own docs call it a demo with synthetic data; Sam's instruction is not to use those words. The plan describes what is true and shipped (the engine, indicators, journeys, reproducibility gate) and avoids production claims it cannot support (no "in production", no customer counts). This is the honest middle: it is a founder-built product in 2026, which is exactly what her second lane asks for.
9. **Scope creep into a redesign.** Every change above is a data edit, a card rewrite in the same component, or a six-line script. The one structural change (7 → 10 featured) reuses the existing renderer.
10. **Name error.** The user wrote "Felon Fatemi"; her name is Falon Fatemi. Nothing on the site names her, so no risk there, but any DM must use the correct spelling.

## Test Plan

**Environment:** local, `python -m http.server 8080` in the repo root, Chrome or Edge. No credentials needed (static site). `specs/test-context.local.md`: not required.

**T1 — Dark default, no flash.** Open http://localhost:8080/ in a fresh incognito window. Expect: dark background (#131210) on first paint; the toggle shows the sun glyph. DevTools → Application → Local Storage: no key yet. Reload: still dark.

**T2 — Toggle persists.** Click the theme button. Expect light theme; localStorage key `theme=light`. Reload: light persists. Click again → dark, key `theme=dark`.

**T3 — Dark contrast spot-check.** In dark: hero video poster edges, signature mark in About, `.creds` links hover, project cards, modal. Expect readable text (no dark-on-dark), no white boxes.

**T4 — Print unaffected.** Open any project → "Print one-pager" → print preview is light with header hidden (as today).

**T5 — Hero KPIs.** Expect the KPI strip, in order: $40M+, $500M+, 150+ specialized agents, 50+ Claude skills authored, 2.5M+, 442B+, 99%+, 460 research citations, 10 h-index. Count-up animation runs on all nine. Creds row shows "460 citations · Scholar".

**T6 — Featured ten.** Home → "Ten that show the range" → exactly ten buttons numbered 01–10 in the R4 order. Click 02 → Brane AI modal; click 03 → Claims Testing modal. Each modal shows Problem, Approach, Architecture, Tech stack, Output, Impact, Framework.

**T7 — Banned words and names gate.** `grep -i -E "synthetic|frozen data|mock data|Blue Cross|MetroPlus|Primient|Humana" index.html` (after stripping the `--sig` line) → zero hits. `grep -c "110+" index.html` → 0.

**T8 — Link gate.** Extract every `https://github.com/amiiiirsaman/...` URL from `index.html`; `gh api repos/<owner>/<name> --jq .visibility` → every result `public`. No `deck-builder-v1` or `procurement-knowledge-hub` URLs present. Work cards for Brane AI, Claims Testing, SpendSphere, Deck Builder, Procurement Knowledge Hub show the private badge.

**T9 — Skills card.** Skills view → card 02b titled "Skills & agent specialization"; contains "50+", the definition sentence, at least eight real skill names, and the three benefit claims. No "my-builder", "my-observer", "my-roadmap" (bare) strings anywhere.

**T10 — Resume.** `pypdf` text extraction of the new PDF: contains "150+", "460 citations", "h-index 10", "50+", "394", "213,420", "100×"; does not contain "110+", "451", "MetroPlus". Page count = 2. All eleven v8 hyperlinks present. Diff of v8 text vs v9 text shows only the intended edits. All three resume hrefs in `index.html` point at `Sam_Mahdavian_Resume_20260905.pdf`; the file downloads from the local server.

**T11 — Regression.** ⌘K palette opens and lists 44 projects; filters on Work view still work; About and Contact render unchanged; `#p=<slug>` deep link opens the right modal for a new entry (e.g. Brane AI).

**T12 — Data guard.** `/my-data-guard` over `index.html`, the new PDF, and `specs/` → no findings.
