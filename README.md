# sammahdavian.ai — portfolio

Self-contained portfolio site for Sam (Amirsaman) Mahdavian, PhD.

## Files
- `index.html` — the entire site (hero video and diagrams are embedded; the résumé button links to the PDF below)
- `Sam_Mahdavian_Resume.pdf` — downloadable résumé (AI Solutions version), referenced by the "Download résumé" buttons
- `og-image.png` — social/link-preview image (referenced as https://sammahdavian.ai/og-image.png)
- `CNAME` — custom domain for GitHub Pages (sammahdavian.ai)

## Deploy (GitHub Pages)
1. Put all four files in the repo root.
2. Settings → Pages → Deploy from branch `main` (`/root`).
3. Settings → Pages → Custom domain: `sammahdavian.ai`.
4. At your DNS provider, point `@` to GitHub Pages IPs (185.199.108–111.153) and `www` CNAME → `amiiiirsaman.github.io`.
5. Enable "Enforce HTTPS".

To update the site, edit `index.html`. To update the résumé, replace `Sam_Mahdavian_Resume.pdf` (keep the filename).
