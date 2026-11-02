# Writing rung - machine text and human text

One job: turn the brief into text a machine can act on, text a person can use, or both. Change how the text says things. Do not change what it says.

## Audiences

Read `audiences` and `ste-human` from the brief. If a field is absent, use `_shared/defaults.md`.

- `machine`: full ASD-STE100. Write `machine/text.md`.
- `human`: ISO 24495-1 plain language. Write `human/text.md`.
- `both`: write those two files. One audience per file.
- `ste-human: 80`: also write `ste-human/text.md`. This is human-readable ASD-STE100 at 80% adherence.

The 80% target belongs only to `ste-human/text.md`. It does not apply to `human/text.md`.

## Machine file

Apply every rule in `ste-issue-9.md`. The output shows the effect of the rules. It does not mention the rules.

Also apply the replacement table in `ste-rules.md`. That table is the word list `ste_check.py` rejects. The digest does not contain the dictionary. When you need a word the table does not list, follow the digest: use a short high-frequency word, or a technical name the brief already gives. Do not invent a technical noun or a technical verb.

## Human-readable STE file

Write `ste-human/text.md` only when `ste-human` is `80`.

Aim for 80% adherence to ASD-STE100. Keep these rules from `ste-issue-9.md`:

- One idea in each sentence.
- Active voice.
- The approved word when `ste-rules.md` lists a replacement.
- Short sentences. Procedures stay at 20 words. Other sentences stay within 25.
- One instruction in each procedure sentence. Put the condition first.

The other 20% is tone. You may use "you" and contractions. You may address the reader in descriptive text. You may keep a common word when the approved word makes the sentence hard for a person to say. Record that word under `clarity-exceptions`. Do not drop a condition.

## ISO file

Apply every principle in `plain-language.md`. Follow that file only.

Do not apply `ste-issue-9.md`. Do not apply the 80% target. Do not run `ste_check.py` on this file.

## Meaning

Do not add a claim the brief does not contain. Do not drop a condition. Code blocks, config, and data pass through untouched.

If a rule fights the meaning, the meaning wins. Record the exception in frontmatter under `clarity-exceptions:` with a reason.

If you need a technical name and the approved list has no word for it, use a name the brief already gives. Add it under Local additions in `ste-rules.md` and to `_tools/ste_check.py` in the same change. The categories are in `ste-issue-9.md` sections 1.5-1.13.

When more than one file exists, they make the same claims. The ISO file may be warmer. The 80% file may use "you" and contractions. Neither file may know something the machine file does not.

## Files

Write these under `stages/01_doc-clarity/output/`. `{slug}` is the brief's slug. Use lowercase hyphens.

`current.md` at `output/current.md`:

```markdown
# Current run

slug: {slug}
path: {slug}/
```

`output/{slug}/manifest.md`:

```markdown
# Manifest

- slug: `{slug}`
- title: `{title}`
- audiences: `machine` or `human` or `both`
- ste-human: `80` or `no`
- machine: `machine/text.md` or `none`
- ste-human: `ste-human/text.md` or `none`
- human: `human/text.md` or `none`
```

Machine frontmatter:

```markdown
---
audience: machine
standard: ASD-STE100
adherence: full
slug:
title:
clarity-exceptions:
---
```

Human-readable STE frontmatter:

```markdown
---
audience: ste-human
standard: ASD-STE100
adherence: 80
slug:
title:
clarity-exceptions:
---
```

ISO frontmatter:

```markdown
---
audience: human
standard: ISO-24495-1
slug:
title:
readers:
purpose:
clarity-exceptions:
---
```

The first heading of a human file states the reader's task. The first heading of a machine file names the topic.

## Check command

From the workspace root, run one command for each file you wrote.

```bash
python _tools/ste_check.py stages/01_doc-clarity/output/{slug}/machine/text.md --audience machine
python _tools/ste_check.py stages/01_doc-clarity/output/{slug}/ste-human/text.md --audience human
```

Run a command only for a file you wrote. Do not run the script on `human/text.md`.

The script writes `check.md` in that file's folder. The first line must be `pass`. A `fail:` stops the run. Fix the text and run the script again. A second run replaces `check.md`, so add `human: pass` only after the script passes and the person has read the text.

For `human/text.md`, the person writes `check.md`. The first line is `pass` or `fail: <why>`. The file also contains the line `human: pass`.
