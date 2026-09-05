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
