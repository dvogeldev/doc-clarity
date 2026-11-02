# setup - set the defaults once

One job: record defaults the brief can override.

## Inputs
- Working (this run): `questionnaire.md`

Do NOT load: stage outputs, stage references, earlier runs.

## Process
1. Ask the questions in `questionnaire.md`.
2. Write the answers into `../_shared/defaults.md`.
3. Do not put an API key in that file.

## Outputs
- `../_shared/defaults.md`

## Check
A person reads `_shared/defaults.md` and confirms the readers, the default audience, and the default climb.
