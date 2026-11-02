# 03_web-pages - build one HTML page

One job: make one self-contained HTML page the reader can use for this topic.

## Inputs
- Working (this run): `../01_doc-clarity/output/current.md`
- Working (this run): `../02_diagrams/output/`
- Reference (every run): `references/web-pages.md`

Do NOT load: stage 01 references, the video stage, `_shared/ladder.md`, `_shared/sources.md`, earlier slugs.

## Process
1. If `current.md` is missing, stop and say so.
2. Open the manifest at the path `current.md` gives. Ignore a path value of `none`. For each writing file the manifest lists, the matching `check.md` must start with `pass` and contain `human: pass`. If it does not, stop.
3. If `figures.md` exists for this slug, its `check.md` must start with `pass`. If it does not, stop. If `figures.md` does not exist, build from the writing only.
4. Read `human/text.md` when the manifest lists it. That file is ISO 24495-1. Read `ste-human/text.md` only when `human` is `none`. Otherwise read the machine text. Do not load a second writing file. Read `figures.md` when its check passed. Follow `references/web-pages.md`.
5. Write `output/{slug}/page.html`.

## Outputs
- `output/{slug}/page.html`

## Check
A person opens `page.html` from disk and does the purpose named in the writing. They can find it, understand it, and use it on one pass. They write `output/{slug}/check.md`. The first line is `pass` or `fail: <why>`. A fail stops the run. Edit the page in place. The next stage does not read this page.
