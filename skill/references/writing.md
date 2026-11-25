# Writing rung - machine text and human text

One job: turn the brief into text a machine can act on, text a person can use, or both. Change how the text says things. Do not change what it says. Write each file at the target path the brief's `targets` names. When no path is named, stop and ask.

## Audiences

Read `audiences` and `ste-human` from the brief. If a field is absent, use [defaults.md](../defaults.md).

- `machine`: full ASD-STE100. Write the machine file at its target path.
- `human`: ISO 24495-1 plain language. Write the human file at its target path.
- `both`: write those two files. One audience per file.
- `ste-human: 80`: also write a human-readable STE file at the target path the requester names.

The 80 percent target belongs only to the 80-percent STE file. It does not apply to the ISO file.

## Machine file

Apply every rule in [ste-issue-9.md](ste-issue-9.md). The output shows the effect of the rules. It does not mention the rules.

Also apply the replacement table in [ste-rules.md](ste-rules.md). That table is the word list `ste_check.py` rejects. When you need a word the table does not list, follow the digest: use a short high-frequency word, or a technical name the brief already gives. Do not invent a technical noun or a technical verb.

## Map in the machine file

Every machine file carries one Mermaid diagram near the top. The diagram maps the document: its parts, its routes, or its flow.

- The diagram repeats claims the text already makes. It adds none.
- Put each claim in a node label or an edge label. A machine reader consumes the map without the prose.
- Replace the prose the diagram carries. Keep prose only for what a label cannot hold.
- Use one diagram for a simple map. Use two when a map and a route flow are both needed.

## Human-readable STE file

Write this file only when `ste-human` is `80`.

Aim for 80 percent adherence to ASD-STE100. Keep these rules from [ste-issue-9.md](ste-issue-9.md):

- One idea in each sentence.
- Active voice.
- The approved word when [ste-rules.md](ste-rules.md) lists a replacement.
- Short sentences. Procedures stay at 20 words. Other sentences stay within 25.
- One instruction in each procedure sentence. Put the condition first.

The other 20 percent is tone. You may use "you" and contractions. You may address the reader in descriptive text. You may keep a common word when the approved word makes the sentence hard for a person to say. Record that word under `clarity-exceptions`. Do not drop a condition.

## ISO file

Apply every principle in [plain-language.md](plain-language.md). Follow that file only.

Do not apply [ste-issue-9.md](ste-issue-9.md). Do not apply the 80 percent target. Do not run `ste_check.py` on this file.

## Meaning

Do not add a claim the brief does not contain. Do not drop a condition. Code blocks, config, and data pass through untouched.

If a rule fights the meaning, the meaning wins. Record the exception in frontmatter under `clarity-exceptions:` with a reason.

If you need a technical name and the approved list has no word for it, use a name the brief already gives. Add it under Local additions in [ste-rules.md](ste-rules.md) and to `_tools/ste_check.py` in the same change. The categories are in [ste-issue-9.md](ste-issue-9.md) sections 1.5-1.13.

When more than one file exists, they make the same claims. The ISO file may be warmer. The 80-percent file may use "you" and contractions. Neither file may know something the machine file does not.

Deliver clean. When the target file is a repo document (a README, an agent map), strip the run's frontmatter from the delivered file unless the requester wants it kept. The frontmatter is the run's draft record, not the document.

## Frontmatter

Each file carries its frontmatter while the run is open.

Machine:

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

Human-readable STE:

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

ISO:

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

Run one command for each STE file you wrote. Use the absolute path of the skill's folder.

```bash
python /home/david/.agents/skills/doc-clarity/_tools/ste_check.py <machine file> --audience machine --check <machine file>.check.md
python /home/david/.agents/skills/doc-clarity/_tools/ste_check.py <80-percent file> --audience human --check <80-percent file>.check.md
```

Run a command only for a file you wrote. Do not run the checker on the ISO file. The person is that file's check.

The checker writes the check file you named. The first line must be `pass`. A `fail:` stops the run. Fix the text and run the checker again. After the person passes, delete the check files. The commit is the run's record.
