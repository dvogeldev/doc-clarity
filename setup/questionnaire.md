# Setup questionnaire

Ask these once. Write the answers into [_shared/defaults.md](../_shared/defaults.md). Later runs read that file. The brief can override a field for one run.

Do not put an API key in the answer file.

1. Who reads the human text, and what do they already know?
2. What must they be able to do after one read?
3. Default audience: `machine`, `human`, or `both`?
4. Write human-readable ASD-STE100 at 80% adherence (`ste-human: 80`), or leave it off (`ste-human: no`)? The 80% target stays off the ISO 24495-1 file.
5. Default climb: `writing`, `diagrams`, `web`, or `video`?
6. Diagrams you want most often: parts, sequence, comparison, or flow?
7. Web page: a plain readable page, or name the colors to use?
8. Video: confirm that render stays on tools already configured here, with no key in the repo.
