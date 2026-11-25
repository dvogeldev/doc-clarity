# Doc clarity - the skill source

The flow in one line: develop the skill here, install it to `/home/david/.agents/skills/doc-clarity/`, and run it in the target project.

| Rung | Job |
|---|---|
| 1. Writing | rewrite the source into checked writing: full ASD-STE100 for agents, ISO 24495-1 plain language for people |
| 2. Diagrams | replace a prose relationship with a figure, one claim each |
| 3. Web pages | make one self-contained HTML page |
| 4. Explainer videos | script, then render, a short explainer |

The contract for each rung lives in `skill/references/`. The skill entry point is `skill/SKILL.md`.

Climb in that order. Stop at the rung named by `climb-to`. You may skip the web page when the run asks for a video and not a page. You may not skip writing.

Why these four rungs: `skill/references/ladder.md`.
Standards and the posts behind them: `skill/references/sources.md`.

A run never writes here. A run's files and its record live in the target repo's git history.

Status is whatever exists. A rung is complete when its output file exists and the person passed its check.
