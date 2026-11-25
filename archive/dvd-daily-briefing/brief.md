---
slug: dvd-daily-briefing
title: Daily AI briefing
audiences: both
ste-human: no
climb-to: writing
readers: David Vogel
purpose: open today's brief, see how a day runs, and know where a change to voice, sources, or styling goes
---

# Brief - one topic for one run

## Source

The repo is the daily AI briefing for David Vogel. One HTML file leaves the workspace each local day. The file uses dvogeldev styling.

Open `stages/03_render/output/latest.html` for the newest file. The dated file is `stages/03_render/output/YYYY-MM-DD.html`. `index.html` in that folder lists the dated files.

The section order comes from `stages/02_brief/examples/2026-08-11-ai-news.pdf` (August 11, 2026). The visual system is dvogeldev, in `_shared/briefing.css`.

The five section titles live in `_shared/chrome.json`:

- Top of Mind
- Launches & Releases
- Research & Papers
- Tooling & SDKs
- Business & Builder Tactics

Folders:

- `stages/` holds the daily pipeline, in order.
- `_shared/` holds voice, rules, sources, brief shape, and the visual system.
- `_templates/` holds the blank candidates list and the blank brief.
- `_tools/` holds the checks, the HTML renderer, `links.py`, and the morning runner.
- `setup/` holds the factory answers and the daily cadence.

Route:

- Start today's run at `stages/01_gather/CONTEXT.md`. Stop at that stage check.
- Go to `stages/02_brief/CONTEXT.md` after the gather check starts with `pass`. Stop at that stage check.
- Go to `stages/03_render/CONTEXT.md` after the brief check starts with `pass`. Stop at the dated HTML file.
- If the person asks for status, scan `stages/*/output/` and any `check.md`. Report the files that exist.
- If voice, sources, or styling change, edit `_shared/`. Keep the new rule out of a day's output.

Stage jobs:

- `01_gather` writes a sourced list of today's candidates.
- `02_brief` turns today's candidates into the brief.
- `03_render` renders the passed brief to one HTML file.
- Each stage script writes that stage `check.md`.

The one rule: read the previous stage `check.md` before the next stage starts. The first line is `pass`. Run the pipeline once each local day.

Run limits:

- Use the machine local date. Do not label a time CT.
- Search only the channels in `_shared/sources.md`. Open the page. Then keep the url.
- File only stories that appear in today's `candidates.md`, with the same url.
- Do not invent a number, a quote, a product name, or a url.
- Copy the three Top of Mind stories again into the section each story belongs to. Use the same words.
- Do not add a story to fill a section. If a required section has no real item, leave it empty. The check fails. The run stops.
- On a daily run, leave `_shared/` and `_tools/` unchanged.
- If today's HTML file exists and the render check starts with `pass` for that date, stop. Do not rewrite the file.

Morning run:

- `_tools/daily.sh` starts the run. The script calls `grok` with `setup/daily-prompt.md`.
- The script exits when today's HTML file exists and the render check starts with `pass` for that date.
- A run log is `setup/logs/YYYY-MM-DD.log`.
- The clock time is 07:30 local.
- The unit files are `setup/systemd/dvd-daily-briefing.service` and `setup/systemd/dvd-daily-briefing.timer`.
- `Persistent=false`. A missed morning stays missed.
- The units are not installed. `systemctl --user` answers on this machine. No cron daemon is running.
- A Grok scheduled task can stand in until a person enables the timer. It runs only while a Grok session for this workspace is open. It expires 7 days after it was created. It does not fire at 07:30. The notes are in `setup/schedule.md`.
- The previous session recorded task `01a1e5f4-d2ec-7481-861f-194cd3ea20b3`. That task is not running.
- A missed day stays empty until a person starts that date.
- For a date other than today, run `python -I _tools/check_candidates.py --date YYYY-MM-DD`.

Timer install, when a person chooses to turn it on:

```bash
mkdir -p ~/.config/systemd/user
cp setup/systemd/dvd-daily-briefing.service setup/systemd/dvd-daily-briefing.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now dvd-daily-briefing.timer
```

Then remove the Grok scheduled task so the day is not produced twice.

`CLAUDE.md` points at `AGENTS.md`. `AGENTS.md` is the agent map of these same claims.

## Task

After one read the reader can:

1. Open today's brief.
2. Follow a day from gather to brief to HTML, and stop when a check does not start with `pass`.
3. Put a change to voice, sources, or styling in `_shared/`.
4. Say when the morning run is supposed to happen, and that the 07:30 timer is not installed.
5. Install that timer with the commands above, then remove the Grok scheduled task.

## Keep

Keep these names as written: `dvogeldev`, `David Vogel`, `pass`, `CT`, `grok`, `Persistent=false`, `systemctl --user`, the task id `01a1e5f4-d2ec-7481-861f-194cd3ea20b3`, the five section titles, file paths, and the commands. Do not drop a stop condition.
