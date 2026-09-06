# Resolution — Portfolio & Resume Refresh (2026-09-05)

**Spec:** `requirements.md` in this folder · **Outcome:** delivered · **Iterations:** 1 (one rebuild of the resume to fit two pages; one URL fix in the screenshot harness)

## What shipped

**Site (`index.html`)**
- Dark theme is the default. A four-line bootstrap in `<head>` reads `localStorage.theme` and sets `data-theme` before CSS loads (no light flash). The toggle now persists the choice. Print stylesheet untouched.
- Hero KPI strip is nine cells: 150+ specialized agents, 50+ Claude skills authored (new), 460 research citations, 10 h-index. Grid is 9 columns desktop, 3 at ≤900px, 2 at ≤520px. Meta description, Open Graph, JSON-LD, About, footer status, and the 60-second view all say 150+ / 460 / 10.
- Skills card 02b rewritten as "Skills & Agent Specialization · 50+ authored" with a short explanatory paragraph (what a skill is, workflow/capability/domain skills, the three benefits) and current skill names.
- Work data: added **Brane AI** (Founder sector) and **SpendSphere** (Procurement); rewrote **AI Claims Testing Automation** (verified figures: 394 tests, 102 rules, 213,420 lines backtested, 460+ pytest, ~100× as Sam's figure) and **AI Deck Builder** (skills-driven v2). Renamed "Fortune 500 Airline Spend Analysis" → "TailSpend · Supplier Intelligence Engine" and "MRO Spend Intelligence · Rail Manufacturing" → "… · Parts & Vendor Analytics"; industry and scale stay in tags. Removed the one explicit client name (Blue Cross Blue Shield → "a large regional health plan"). Project count 42 → 44.
- Featured list is ten: Doczy, Brane AI, AI Claims Testing, Policy Audit, TailSpend, PADU, SpendSphere, AI Deck Builder, Multi-Agent Fraud, Credit Risk. Heading "Ten that show the range".
- Links: three broken `-main` GitHub URLs fixed; TailSpend now links its real public repo; two private-repo links removed. New `priv:1` flag renders a "private · walkthrough on request" badge on the card and a note in the modal (five entries).
- Resume links (5) point at `Sam_Mahdavian_Resume_20260905.pdf`; the July file stays in the repo for old links.

**Resume**
- New editable source `resume/build_resume.py` (python-docx) → `resume/Sam_Mahdavian_Resume.docx`; `resume/export_pdf.ps1` exports via Microsoft Word COM (LibreOffice is not installed; docx-js is not installed). Two pages, US Letter, 11 hyperlinks preserved.
- Content changes vs v8: 150+ agents; 460 citations / h-index 10 / i10 10; most-cited paper 139 citations; "50+ Claude skills" in summary, competencies, and a new AArete bullet; new Claims Testing bullet; Brane entry now "2020 - Present" with a Brane AI bullet (per Sam); SpendSphere and Deck Builder lines under Selected Solutions. No client names.
- Copied to `Sam_Mahdavian_Resume_20260905.pdf` and to the undated alias `Sam_Mahdavian_Resume.pdf`. `resume/*.pdf` is gitignored to avoid a third copy.

## Deviations from the plan
- Resume built with python-docx + Word instead of docx-js + LibreOffice (neither available). Same result; the runbook is two commands.
- "Private" badge is shown on five entries, not four: Procurement Knowledge Hub also linked a private repo.
- Brane AI describes 40 indicators (per the product's master requirements, Aug 2026) rather than the 35 in the older README.

## Test results (executed inline; no subagent per session policy)
| Test | Result | Evidence |
|---|---|---|
| T1 dark default, no flash | PASS | Headless Edge screenshot of a fresh profile renders dark; bootstrap runs before `<style>` |
| T2 toggle persists | NOT BROWSER-VERIFIED | Code path reviewed (`setTheme` writes `localStorage.theme`; head script reads it). Headless run cannot click. Verify with one click + reload. |
| T3 dark contrast | PASS (spot) | Home, Skills, Work, About, modal screenshots readable; no white boxes |
| T4 print unaffected | PASS (by inspection) | `@media print` block untouched |
| T5 hero KPIs | PASS | Nine cells in the specified order; count-up runs |
| T6 featured ten + modals | PASS | 01–10 in order; `#p=` deep links open Brane AI and Claims Testing modals with all sections |
| T7 banned words / names | PASS | Automated gate: zero hits |
| T8 link gate | PASS | 14 GitHub URLs, all `public` via `gh api` |
| T9 skills card | PASS | Screenshot; stale names absent |
| T10 resume | PASS | 2 pages; contains 150+, 460, h-index 10, 50+, 394, 213,420, 100×; no 110+/451; 11 links |
| T11 regression | PASS (partial) | Work grid, filters, palette label, About render; JS parses (3 blocks) |
| T12 data guard | PASS with expected findings | Only Sam's own email/phone (intentional) and Luhn false positives inside base64 diagram data (pre-existing). Zero client names, zero PHI. |

Known cosmetic: at a 420px headless window the hero text clips on the right; identical on the previously deployed version, so not a regression (likely the headless viewport, not the CSS).

## Files changed
`index.html`, `Sam_Mahdavian_Resume.pdf` (updated alias), `Sam_Mahdavian_Resume_20260905.pdf` (new), `resume/build_resume.py`, `resume/export_pdf.ps1`, `resume/Sam_Mahdavian_Resume.docx` (new), `.gitignore`, `specs/steering/project-map.md`, `specs/portfolio-refresh-2026-09/{requirements,resolution}.md`. Not committed.

## Round 2 (2026-09-05, evening) — page-one curation, generic names, GitHub cleanup
- Generic names: SpendSphere → "Spend Intelligence Platform · AP, MRO & Payer Vendor Analytics"; Doczy AARIA → "Conversational Contract Analytics · Text-to-SQL Agent"; ReImagine → "Provider Network Optimization · Geospatial Network AI"; PolicyPulse removed from copy; TailSpend → "Supplier Intelligence Engine · Aviation Spend"; Invoice Transcription → "Invoice Straight-Through Processor". Doczy kept (public AWS blog + patent). Resume bullet renamed and PDF regenerated under the same dated filename.
- Featured ten: Doczy · Brane Mobility · Brane AI · Claims Testing · Policy Audit · Supplier Intelligence · Invoice Straight-Through · Advanced Pricing · PADU · Credit Risk. Deck Builder, spend platform, and Fraud (Demo/POC) moved off page one; all remain in Work.
- Featured cards are now `div[role=button]` with keyboard support and render the entry's first link (brane-mobility.app, AWS blog, Code) or the private badge. First KPI reordered to the dollar/scale figure on Brane Mobility, Invoice, Pricing (values unchanged).
- Hero: fourth lens "Operator / Investor". About: "Founder" row in At a glance. Featured subtitle rewritten.
- GitHub: profile README updated (40+ systems, 150+ agents, 50+ skills, 460 citations, h-index 10, Brane line, internal product name removed). Five private repos given descriptions; zero repos without one. Two forks with own commits made private (re-archived). **The 19 zero-commit forks could not be deleted: the gh token lacks the `delete_repo` scope, which needs an interactive `gh auth refresh -h github.com -s delete_repo`.** Pinned repos cannot be changed via API; manual swap suggested (customer-service demo → advanced-pricing-engine).
- Verified: JS parses, all ten featured keys resolve, banned-name gate clean, screenshots of Home/About/phone width.
