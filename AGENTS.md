# Doc clarity

One topic goes in. Checked writing comes out, then a diagram, a web page, or an explainer video when the brief climbs. Each rung is a file a person can open and correct before the next rung starts.

## Where things live

| Folder | What it holds |
|---|---|
| `inbox/` | the current brief: one topic per run |
| `stages/` | the pipeline, in execution order |
| `_shared/` | factory: the ladder, the source list, the defaults |
| `_templates/` | the blank brief |
| `_tools/` | `links.py` and `ste_check.py` |
| `setup/` | one-time questions for the defaults |

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| starting a new run | copy [_templates/brief.md](_templates/brief.md) to `inbox/brief.md`, then [01_doc-clarity](stages/01_doc-clarity/CONTEXT.md) | that stage's check |
| a stage check passed and the brief climbs higher | the next stage in [CONTEXT.md](CONTEXT.md) | that stage's check |
| asked for status | scan `stages/*/output/` and any `check.md` | report what exists |
| setting up defaults | [questionnaire](setup/questionnaire.md) | answers written to `_shared/defaults.md` |

## The one rule

Nothing moves to the next stage until the last stage's check passes. A run may stop after any pass.
