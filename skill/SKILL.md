---
name: doc-clarity
description: Rewrite a document or topic into checked writing - full ASD-STE100 for agents and code, ISO 24495-1 plain language for people - then optionally climb to a diagram, a web page, or an explainer video. A run writes only into the target project; nothing is stored outside it. Use when asked to run the doc-clarity pipeline, to make a document agent-readable or human-readable, on "doc-clarity", "climb-to", or a request to change the doc-clarity defaults.
---

# Doc Clarity

One topic goes in. Checked writing comes out. A diagram, a web page, or an explainer video follows when the run climbs. Every rung stops for a human check before the next rung starts.

A run writes only into the target project the requester names. The target repo's git history is the run's record. Nothing is stored outside the target project.

## What a run needs

The request names three things. Stop and ask when one is missing.

- **Target.** The file paths the writing goes to. Example: `AGENTS.md` for the machine file, `README.md` for the human file, in the requester's repo.
- **Source.** The notes, the draft, or the file that holds the meaning. The writing rung may change the wording. It may not change the claims.
- **Audience.** `machine` (full ASD-STE100), `human` (ISO 24495-1 plain language), or `both`.

Optional fields: `climb-to` (`writing`, `diagrams`, `web`, `video`), and `ste-human: 80` for a human-readable STE file. A missing field takes its value from [defaults.md](defaults.md).

Build the brief from the request with [references/brief.md](references/brief.md). The brief lives in the conversation. Write it to disk only when the requester asks.

## Workflow

```
The request names the target, the source, and the audience
  ↓
Build the brief. Load references/writing.md and the rule files it names.
  ↓
Write the output files at the target paths.
  ↓
Run the checker on each STE file you wrote. Fix the text until the checker passes.
  ↓
Stop for the human check. Do not start the next rung.
  ↓
After the person passes: delete the check files. Commit only when the person asks.
```

## The one rule

Nothing climbs until the person passes the last rung's check. Your part is to draft, run the checker, and stop.

## Checks

For each full-STE or 80-percent file you wrote, run the checker with the absolute path of this skill's folder:

```bash
python /home/david/.agents/skills/doc-clarity/_tools/ste_check.py <output file> --audience machine --check <output file>.check.md
```

Use `--audience human` for the 80-percent file. Do not run the checker on an ISO plain-language file. The `--check` option names the check file; without it, the checker writes `check.md` beside the input, which collides when two outputs share a folder.

The checker writes the check file. The first line is `pass` or `fail: <why>`. A fail stops the run. Fix the text and run the checker again.

Then the person reads one section of each file aloud. They confirm they can do, or understand, the thing on one reading. When more than one file exists, they confirm the files make the same claims. They say pass, or they add the line `human: pass` to each check file.

After a pass, delete the check files. The commit is the run's record.

## The ladder

Writing first. A wrong claim is cheap to fix in writing and expensive inside a video. Later rungs repeat the accepted writing. They do not extend it. The reason the order is fixed: [references/ladder.md](references/ladder.md).

| Rung | Writes | Contract |
|---|---|---|
| 1. Writing | the machine file (with its Mermaid map) and the human file, at the target paths | [references/writing.md](references/writing.md) |
| 2. Diagrams | `figures.md` and editable figure sources, in the target folder | [references/diagrams.md](references/diagrams.md) |
| 3. Web page | one self-contained `page.html`, in the target folder | [references/web-pages.md](references/web-pages.md) |
| 4. Explainer video | `narration.md`, `shots.md`, `manifest.md`, in the target folder | [references/videos.md](references/videos.md) |

Each rung reads the last rung's accepted files at their target paths. Each rung stops for its own human check. Skip the web page when the climb asks for a video and not a page. The video does not read the page.

## Defaults

When asked to change the defaults for every future run, walk [references/questionnaire.md](references/questionnaire.md) and write the answers into [defaults.md](defaults.md). Do not store an API key anywhere.

## Status

When asked for the status of a run, look at the run's files at their target paths and at any `.check.md` files beside them. Report what exists and which checks pass. Do not write new files.

## Common pitfalls

| Issue | How to handle |
|---|---|
| The rules are summarized from memory | Read the reference file. It is the contract. |
| A later rung invents a claim | Later rungs repeat the accepted writing. They add no facts. |
| You write `human: pass` yourself | Only the person passes a check. You stop at the check. |
| A run writes outside the target project | Never. The target repo holds the run's files and its record. |
| A rung runs out of order | Writing runs first. No rung is skipped except the web page rule above. |
| A delivered repo doc carries the run's frontmatter | Strip the run's frontmatter from a delivered README or agent map unless the requester wants it kept. |
| A machine file has no Mermaid map | Every machine file carries a Mermaid map near the top. The map replaces the prose it repeats. |
