---
audience: human
standard: ISO-24495-1
slug: dvd-daily-briefing
title: Daily AI briefing
readers: David Vogel
purpose: open today's brief, see how a day runs, and know where a change to voice, sources, or styling goes
clarity-exceptions:
---

# Open today's AI brief

Open `stages/03_render/output/latest.html`. That file is today's brief.

The dated copy is `stages/03_render/output/YYYY-MM-DD.html`. `index.html` in the same folder lists every dated file.

You are the reader. You get one AI news brief each local day. The page uses dvogeldev styling.

The section order follows the August 11, 2026 specimen at `stages/02_brief/examples/2026-08-11-ai-news.pdf`. The visual system is dvogeldev, in `_shared/briefing.css`.

## What is on the page

Five section titles live in `_shared/chrome.json`:

- Top of Mind
- Launches & Releases
- Research & Papers
- Tooling & SDKs
- Business & Builder Tactics

## How a day moves

Read the previous stage `check.md` before the next stage starts. The first line is `pass`. The pipeline runs once each local day.

1. Gather writes a sourced list of today's candidates. Start at `stages/01_gather/CONTEXT.md`. Stop at that stage check.
2. The brief turns those candidates into the day's brief. Start at `stages/02_brief/CONTEXT.md` after gather passes. Stop at that stage check.
3. Render writes one HTML file from the passed brief. Start at `stages/03_render/CONTEXT.md` after the brief passes. Stop when the dated file exists.

Each stage script writes that stage's `check.md`.

If you ask for status, look in `stages/*/output/` and any `check.md`. Report the files that exist.

If today's HTML file is already there and the render check starts with `pass` for that date, stop. Do not rewrite the file.

## Change the voice, the sources, or the styling

Edit `_shared/`. Keep the new rule out of one day's output.

On a daily run, leave `_shared/` and `_tools/` unchanged.

## What a run may say

Search only the channels in `_shared/sources.md`. Open the page before you keep the url.

Use a story only when it is in today's `candidates.md`, and keep the same url. Do not invent a number, a quote, a product name, or a url.

Copy the three Top of Mind stories again into the section each story belongs to. Use the same words.

Do not add a story to fill a section. If a required section has no real item, leave it empty. If that section stays empty, the check fails. If the check fails, the run stops.

Use the machine's local date. Do not label a time CT.

## When the brief runs

The runner is `_tools/daily.sh`. It calls `grok` with `setup/daily-prompt.md`.

If today's file already passed its check, the runner exits. The log is `setup/logs/YYYY-MM-DD.log`.

The clock time is 07:30 local. The unit files are `setup/systemd/dvd-daily-briefing.service` and `setup/systemd/dvd-daily-briefing.timer`. `Persistent=false`, so a missed morning stays missed.

Those units are not installed. `systemctl --user` answers on this machine. No cron daemon is running.

A Grok scheduled task can stand in until a person enables the timer. It runs only while a Grok session for this workspace is open. It expires 7 days after creation. It does not fire at 07:30. The notes are in `setup/schedule.md`.

The previous session recorded task `01a1e5f4-d2ec-7481-861f-194cd3ea20b3`. That task is not running.

A missed day stays empty until you start that date. For another date, run:

```bash
python -I _tools/check_candidates.py --date YYYY-MM-DD
```

## Turn on the 07:30 timer

```bash
mkdir -p ~/.config/systemd/user
cp setup/systemd/dvd-daily-briefing.service setup/systemd/dvd-daily-briefing.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now dvd-daily-briefing.timer
```

Then remove the Grok scheduled task so the day is not produced twice.

## Where the pieces live

| Folder | What it holds |
|---|---|
| `stages/` | the daily pipeline, in order |
| `_shared/` | voice, rules, sources, brief shape, and the visual system |
| `_templates/` | the blank candidates list and the blank brief |
| `_tools/` | the checks, the HTML renderer, `links.py`, and the morning runner |
| `setup/` | the factory answers and the daily cadence |

`CLAUDE.md` points at `AGENTS.md`. `AGENTS.md` is the agent map of these same claims.
