---
audience: machine
standard: ASD-STE100
adherence: full
slug: dvd-daily-briefing
title: Daily AI briefing
clarity-exceptions:
---

# Daily AI briefing

One HTML file leaves this workspace each local day. The file uses dvogeldev styling. David Vogel is the reader.

## Where things live

- `stages/` holds the daily pipeline, in order.
- `_shared/` holds voice, rules, sources, brief shape, and the visual system.
- `_templates/` holds the blank candidates list and the blank brief.
- `_tools/` holds the checks, the HTML renderer, `links.py`, and the morning runner.
- `setup/` holds the factory answers and the daily cadence.

## Route

Start today's run at `stages/01_gather/CONTEXT.md`. Stop at that stage check.

Go to `stages/02_brief/CONTEXT.md` after the gather check starts with `pass`. Stop at that stage check.

Go to `stages/03_render/CONTEXT.md` after the brief check starts with `pass`. Stop at the dated HTML file.

If the person asks for status, scan `stages/*/output/` and any `check.md`. Report the files that exist.

If voice, sources, or styling change, edit `_shared/`. Keep the new rule out of a day's output.

## The one rule

Read the previous stage `check.md` before the next stage starts. The first line is `pass`.

Run the pipeline once each local day. The deliverable is `stages/03_render/output/YYYY-MM-DD.html`.

Open `stages/03_render/output/latest.html` for the newest file. In that folder, `index.html` lists the dated files.

## Stage jobs

`01_gather` writes a sourced list of today's candidates.

`02_brief` turns today's candidates into the brief.

`03_render` renders the passed brief to one HTML file.

Each stage script writes that stage `check.md`.

## Run limits

Use the machine local date. Do not label a time CT.

Search only the channels in `_shared/sources.md`. Open the page. Then keep the url.

File only stories that appear in today's `candidates.md`, with the same url.

Do not invent a number, a quote, a product name, or a url.

Copy the three Top of Mind stories again into the section each story belongs to. Use the same words.

Do not add a story to fill a section. If a required section has no real item, leave it empty.

If that section stays empty, the check fails. If the check fails, the run stops.

On a daily run, leave `_shared/` and `_tools/` unchanged.

If today's HTML file exists and the render check starts with `pass` for that date, stop. Do not rewrite the file.

## Page shape

The section order comes from `stages/02_brief/examples/2026-08-11-ai-news.pdf`.

The visual system is dvogeldev, in `_shared/briefing.css`.

The five section titles live in `_shared/chrome.json`.

The titles are Top of Mind, Launches & Releases, Research & Papers, Tooling & SDKs, and Business & Builder Tactics.

## Morning run

`_tools/daily.sh` starts the run. The script calls `grok` with `setup/daily-prompt.md`.

The script exits when today's HTML file exists and the render check starts with `pass` for that date.

A run log is `setup/logs/YYYY-MM-DD.log`.

The clock time is 07:30 local.

The unit files are `setup/systemd/dvd-daily-briefing.service` and `setup/systemd/dvd-daily-briefing.timer`.

`Persistent=false`. A missed morning stays missed.

The units are not installed. `systemctl --user` answers on this machine. No cron daemon is running.

A Grok scheduled task can stand in until a person enables the timer. The task runs only while a Grok session for this workspace is open.

The task expires 7 days after creation. The task does not fire at 07:30.

The notes are in `setup/schedule.md`. The previous session recorded task `01a1e5f4-d2ec-7481-861f-194cd3ea20b3`.

That task is not running.

A missed day stays empty until a person starts that date.

For a date other than today, run `python -I _tools/check_candidates.py --date YYYY-MM-DD`.

## Timer install

Install the 07:30 timer with the commands below. Then remove the Grok scheduled task. One run each day is the limit.

```bash
mkdir -p ~/.config/systemd/user
cp setup/systemd/dvd-daily-briefing.service setup/systemd/dvd-daily-briefing.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now dvd-daily-briefing.timer
```

## Agent entry

`CLAUDE.md` points at `AGENTS.md`. `AGENTS.md` is the agent map of these same claims.
