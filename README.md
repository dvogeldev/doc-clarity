# Doc clarity

You give the skill one topic. It gives that topic back in forms you can check: writing first, then a diagram, a web page, and a short explainer when you want them.

A person and an agent do not share one mixed document. Each reader gets a file written for that reader. You read a section aloud, and you decide when the meaning is right. The agent drafts. You keep the meaning.

**A run writes only into the target project.** The request names the target paths — a `README.md` for people, an `AGENTS.md` for agents, a folder for figures or a page. The target repo's git history is the run's record. Nothing is stored outside it. This repository is the source of the skill, not a place where runs land.

## What a run needs

| Field | What you name |
|---|---|
| Target | the file paths the writing goes to (example: `machine: AGENTS.md, human: README.md`) |
| Source | the notes, the draft, or the file that holds the meaning |
| Audience | `machine` (full ASD-STE100), `human` (ISO 24495-1 plain language), or `both` |
| `climb-to` | optional: `writing`, `diagrams`, `web`, or `video`. Writing always happens. |
| `ste-human` | optional: `80` adds a human-readable STE file. Default `no`. |

Missing fields take their values from [skill/defaults.md](skill/defaults.md).

## The four rungs

| Rung | Writes | Contract |
|---|---|---|
| 1. Writing | the machine file and the human file, at the target paths | [skill/references/writing.md](skill/references/writing.md) |
| 2. Diagrams | `figures.md` and editable figure sources (Mermaid or SVG), one claim each | [skill/references/diagrams.md](skill/references/diagrams.md) |
| 3. Web page | one self-contained `page.html`, openable from disk | [skill/references/web-pages.md](skill/references/web-pages.md) |
| 4. Explainer video | `narration.md` and `shots.md`, then a render only when the session already can | [skill/references/videos.md](skill/references/videos.md) |

Later rungs repeat the writing you already accepted. They do not add new facts. A wrong sentence is cheap to fix in writing and expensive inside a video. Why the order is fixed: [skill/references/ladder.md](skill/references/ladder.md).

## How you accept a file

Nothing climbs until you pass the last rung's check. You may stop after any pass.

- On a full-STE or 80-percent file, a script checks sentence length and the approved word list first. A failure stops the run until the agent fixes the text.
- Then you read one section aloud. You confirm you can do, or understand, the thing on one reading.
- When more than one file exists, you confirm they make the same claims.
- You say pass, or you add the line `human: pass` to the rung's check file. After a pass, the check files are deleted. Your commit is the record.

The agent never writes `human: pass` itself. It drafts, checks with the script, and stops for you.

## Install

The skill runs from the installed copy:

```bash
cp -r skill/. ~/.agents/skills/doc-clarity/
```

A change is made in `skill/` here first, then copied to the installed folder. The two copies must not drift. The entry point is [skill/SKILL.md](skill/SKILL.md).

## The repository

| Path | What it holds |
|---|---|
| [AGENTS.md](AGENTS.md) | the agent map for this repository |
| [skill/](skill/SKILL.md) | the skill source: `SKILL.md`, `defaults.md`, `references/`, `_tools/ste_check.py` |
| [archive/](archive/) | records of runs made under the old workspace model, before runs moved into target projects |
| `_tools/links.py` | the check that links and input paths resolve |
| [LICENSE](LICENSE) | the MIT license |

To change the defaults for every future run, answer [skill/references/questionnaire.md](skill/references/questionnaire.md) once. The answers go into [skill/defaults.md](skill/defaults.md). Do not put an API key in that file.

## Where the rules come from

Two standards, and one public post, are the sources. The working copies in this repo are summaries.

- ASD-STE100 Simplified Technical English, Issue 9, 15 January 2025. [Official site](https://www.asd-ste100.org/). ASD owns the copyright and the trademark.
- ISO 24495-1:2023, Plain language, Part 1. [Official record](https://www.iso.org/standard/78907.html).
- Andrej Karpathy, 2 October 2026, [post 2105819303471976479](https://x.com/karpathy/status/2105819303471976479).

The full list, including talks and related posts, is [skill/references/sources.md](skill/references/sources.md).

## License

This repository is [MIT](LICENSE), copyright 2026 David Vogel.

Two limits sit outside that grant:

- ASD-STE100 and ISO 24495-1 stay with their owners. The files here are working summaries. Certify a document only against the official issue.
- `_tools/links.py` comes from the ICM architect project, copyright 2026 Jake Van Clief, MIT. `ste_check.py` and the plain-language and checker word lists come from the ICM clarity stage, MIT.
