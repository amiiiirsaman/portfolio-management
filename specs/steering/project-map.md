# Project Map — sammahdavian.ai portfolio (memo, 2026-09-05)

**Stack:** single static page. `index.html` (~384 KB, one file: CSS + HTML + inline JS + base64 media). No build step, no framework, no package manager. Fonts from Google Fonts. Deployed by GitHub Pages.

**Areas**

| Area | Where | Notes |
|---|---|---|
| Site | `index.html` | The deployed page. `index (N).html` copies are gitignored working drafts; `index (15).html` == `index.html` byte-for-byte after CRLF normalization. Edit `index.html` only. |
| Theme | `index.html` lines ~19-30 (`html[data-theme="dark"]` tokens, `:root` light tokens) and the `/* F7 dark mode */` script block | Default is light (no `data-theme` set); toggle has **no persistence** and ignores `prefers-color-scheme`. |
| Project data | `var SECTORS=[...]` (line ~673), `var P=[...]` (line ~682), `var FEATURED=[...]` (line ~744) | `P` = 42 project objects `{name,s,tag,one,kpi,problem,approach,stack,output,impact,fw,links,ind,tt,dg/arch,pub}`. `FEATURED` = substring keys matched against `p.name`; rendered by `renderFeatured()` with 01..NN numbering. |
| Skills view | `<section class="view" id="view-skills">` | `.skillgrid` of `.skillcard`s (01, 02, 02b, 03..08); chips with `class="core"` = primary stack. |
| Hero KPIs | `.kpis > .kpi > .n/.l` | Count-up animation parses the leading number of `.n`. |
| Resume | `Sam_Mahdavian_Resume_20260722.pdf` (linked from 3 places: hero button, recruiter lens strip, command palette) | PDF produced with LibreOffice Writer 24.2; **no editable source in repo or on disk**. |
| Deploy | `.github/workflows/deploy-pages.yml` | Push to `main` → `actions/deploy-pages` uploads repo root. Custom domain via `CNAME` = sammahdavian.ai. |

**Run locally:** `python -m http.server 8080` in repo root → http://localhost:8080/index.html (or open the file directly; everything is inline). Dev loop = save file, hard-refresh.

**Test:** no automated tests. Verify in a real browser + `grep` gates (client names, broken links) + `pypdf` text check for the resume.

**Quirks**
- `index.html` has CRLF line endings; the `(N)` copies have LF. Preserve CRLF when editing `index.html` (or normalize deliberately in one commit).
- Toolchain: Python at `D:\Users\14078\Python311` (not on PATH in fresh shells; `export PATH=/d/Users/14078/Python311:$PATH`, set `PYTHONIOENCODING=utf-8`). `gh` is authenticated as `amiiiirsaman`.
- The `--sig` CSS variable holds a ~10 KB base64 PNG on one line; strip it before grepping/diffing text.

**Update 2026-09-05 (portfolio-refresh-2026-09)**
- Theme: dark is now the default; a `<script>` in `<head>` reads `localStorage.theme` before CSS; `setTheme()` persists.
- Project objects may carry `priv:1` → "private · walkthrough on request" badge (card) + note (modal). `FEATURED` has ten keys.
- Resume runbook: `python resume/build_resume.py` (python-docx, text lives in the script) then `powershell -ExecutionPolicy Bypass -File resume/export_pdf.ps1` (Word COM; LibreOffice is NOT installed). Copy the PDF to `Sam_Mahdavian_Resume_<YYYYMMDD>.pdf` and update the 5 hrefs in `index.html`. Two-page check: `pypdf` page count.
- Headless screenshots: `msedge --headless=new --screenshot=... http://127.0.0.1:<port>/#view-skills` after `python -m http.server <port> --directory D:/Portfolio` (do not append `/` after `index.html`).
- Gates before commit: JS parse of the 3 script blocks, banned-word scan (client names, stale numbers), `gh api repos/... --jq .visibility` for every GitHub link, `my-data-guard` scan (own email/phone and base64 Luhn hits are expected).

## Git workflow
- Remote: `origin` = github.com/amiiiirsaman/portfolio-management. Default and integration branch: `main`.
- Model: **trunk-based** (all history is direct commits on `main`; GitHub Pages deploys from `main` via `.github/workflows/deploy-pages.yml`). Push = `pull --rebase` then push to `main`.
