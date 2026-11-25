# Doc clarity - the skill source

This repository develops the doc-clarity skill. The installed copy that agents run lives at `/home/david/.agents/skills/doc-clarity/`. A run writes only into the target project it is pointed at. This repository holds the skill and the archive. It holds no run state.

Claude Code / agents that look for `CLAUDE.md`: this file is the entry point.

## Where things live

| Folder | What it holds |
|---|---|
| `skill/` | the skill source: `SKILL.md`, `defaults.md`, `references/`, `_tools/ste_check.py` |
| `archive/` | records of runs made under the old workspace model |
| `_tools/` | `links.py` checks every link resolves |

## Route by what you want

| If | Go to | Then |
|---|---|---|
| you are running doc-clarity | the installed skill at `/home/david/.agents/skills/doc-clarity/SKILL.md` | that file |
| you are changing the skill | `skill/` in this repo | copy the change to the installed folder, then commit |
| you want a past run's record | `archive/` | read it there |
| you are checking repo health | `python3 -I _tools/links.py` | fix what it reports |

## The one rule

A change to the skill is made in `skill/` here first. Then the same change is copied to `/home/david/.agents/skills/doc-clarity/`. The two copies must not drift.
