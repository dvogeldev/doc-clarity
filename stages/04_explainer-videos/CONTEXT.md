# 04_explainer-videos - script the explainer

One job: write the narration and the shot list for a short explainer, then render only after that text passes.

## Inputs
- Working (this run): `../01_doc-clarity/output/current.md`
- Working (this run): `../02_diagrams/output/`
- Reference (every run): `references/videos.md`

Do NOT load: stage 01 references, the HTML page, `_shared/ladder.md`, `_shared/sources.md`, earlier slugs.

## Process
1. If `current.md` is missing, stop and say so.
2. Open the manifest at the path `current.md` gives. Ignore a path value of `none`. For each writing file the manifest lists, the matching `check.md` must start with `pass` and contain `human: pass`. If it does not, stop.
3. If `figures.md` exists for this slug, its `check.md` must start with `pass`. If it does not, stop. If `figures.md` does not exist, use the writing only.
4. Write `narration.md`, `shots.md`, and `manifest.md` under `output/{slug}/`, as `references/videos.md` specifies.
5. Stop for the check. Do not render in this step.
6. After `check.md` starts with `pass`, render only if this session can already render. Do not ask for an API key. Do not store a key. If you cannot render, set `render: not-produced` and the reason.

## Outputs
- `output/{slug}/narration.md`
- `output/{slug}/shots.md`
- `output/{slug}/manifest.md`
- a video file only after step 6

## Check
A person reads the narration aloud against the writing. The claims match. The order matches. They write `output/{slug}/check.md`. The first line is `pass` or `fail: <why>`. A fail stops the run. Render is process step 6 and runs only after this pass. If a video file exists, the person watches it once and confirms the picture matches `shots.md`. They set the first line back to `fail: <why>` if it does not.
