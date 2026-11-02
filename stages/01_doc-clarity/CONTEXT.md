# 01_doc-clarity - write the checked text

One job: rewrite the brief into machine text, human text, or both, with the meaning unchanged.

## Inputs
- Working (this run): `../../inbox/brief.md`
- Reference (every run): `../../_shared/defaults.md`
- Reference (every run): `references/writing.md`
- Reference (every run): `references/ste-issue-9.md`
- Reference (every run): `references/ste-rules.md`
- Reference (every run): `references/plain-language.md`

Do NOT load: other stages, their references, earlier slugs, `_shared/ladder.md`, `_shared/sources.md`.

## Process
1. If `inbox/brief.md` is missing or empty, stop. Tell the person to copy `_templates/brief.md` to `inbox/brief.md`.
2. Read `audiences`, `ste-human`, `slug`, and `climb-to` from the brief. If a field is missing, use `_shared/defaults.md`.
3. Rewrite under `references/writing.md`. Write the files it names. Meaning stays the same.
4. Run the check commands in `references/writing.md` from the workspace root.

## Outputs
- `output/current.md`
- `output/{slug}/manifest.md`
- `output/{slug}/machine/text.md` when the brief asks for machine
- `output/{slug}/ste-human/text.md` when the brief sets `ste-human: 80`
- `output/{slug}/human/text.md` when the brief asks for ISO 24495-1 text

## Check
`ste_check.py` writes `check.md` beside `machine/text.md` and beside `ste-human/text.md`. It does not run on `human/text.md`. The first line is `pass` or `fail: <why>`. A fail stops the run. Fix the text and run the script again. Then a person reads one section of each file aloud and confirms they can do, or understand, the thing on one reading. When more than one file exists, the person also confirms they make the same claims. They add the line `human: pass` to each script-written `check.md`. For the ISO file, the person writes `check.md` with first line `pass` or `fail: <why>` and the line `human: pass`. The 80% target is a check on `ste-human/text.md` only. Edit the text in place. The next stage reads whatever is here.
