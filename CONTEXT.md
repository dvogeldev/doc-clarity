# Doc clarity - the pipeline

The flow in one line: write the claims so a person can check them, then climb only as far as the brief asks.

| Stage | Job |
|---|---|
| `01_doc-clarity` | rewrite the brief into checked writing |
| `02_diagrams` | replace a prose relationship with a figure |
| `03_web-pages` | make one interactive HTML page |
| `04_explainer-videos` | script, then render, a short explainer |

Each stage's own `CONTEXT.md` holds its inputs, outputs, and check.

Climb in that order. Stop at the rung named by `climb-to` in the brief. You may skip `03_web-pages` when the brief asks for a video and not a page. You may not skip `01_doc-clarity`.

Why these four rungs: [_shared/ladder.md](_shared/ladder.md).
Standards and the posts behind them: [_shared/sources.md](_shared/sources.md).

Factory (stable, every run): `_shared/defaults.md`
Product (new each run): `inbox/brief.md` and each stage's `output/`

Status is whatever exists. A stage is complete when its `output/` holds this run's artifact and the `check.md` files for that run start with `pass`. A `.gitkeep` does not count.
