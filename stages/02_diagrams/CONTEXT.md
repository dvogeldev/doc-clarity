# 02_diagrams - draw the claims

One job: replace a hard paragraph with a figure that shows a claim the writing already makes.

## Inputs
- Working (this run): `../01_doc-clarity/output/current.md`
- Reference (every run): `references/diagrams.md`

Do NOT load: stage 01 references, stage 03, stage 04, `_shared/ladder.md`, `_shared/sources.md`, earlier slugs.

## Process
1. If `current.md` is missing, stop and say so.
2. Open the manifest at the path `current.md` gives. Ignore a path value of `none`. For each writing file the manifest lists, the matching `check.md` must start with `pass` and contain `human: pass`. If it does not, stop.
3. Read `human/text.md` when the manifest lists it. That file is ISO 24495-1. Read `ste-human/text.md` only when `human` is `none`. Otherwise read the machine text. Do not load a second writing file. Then follow `references/diagrams.md`.
4. Write `output/{slug}/figures.md` and the source files it names. Use the same slug as `current.md`.

## Outputs
- `output/{slug}/figures.md`
- one editable source per figure, or no source when `figures: none`

## Check
A person checks each figure against the claim sentence. The figure shows that claim and no other claim. They write `output/{slug}/check.md`. The first line is `pass` or `fail: <why>`. A fail stops the run. Edit the source in place. The next stage reads whatever is here.
