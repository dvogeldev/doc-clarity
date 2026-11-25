# Diagrams rung - one claim in each figure

Use a figure when a relationship, a sequence, a comparison, or a layout is easier to see than to read. The figure replaces that paragraph. Do not draw a figure that repeats every sentence.

Karpathy's test for this rung: a diagram can be easier to process, parse, and understand than the paragraph it replaces.

## Input

Load one accepted writing file. Use the human file when it exists. Use the 80-percent file only when the human file was not written. Use the machine file only when neither of those exists. Do not load a second writing file. Require the person to have passed that file's check.

## Rules

- One claim in each figure. The claim is a sentence that already exists in the writing file you loaded.
- Labels use the nouns from that writing. Do not invent a synonym.
- Write an editable source: Mermaid (`.mmd`) or SVG (`.svg`). A person must be able to correct the figure without a new image.
- A PNG is optional. It must match the source. Use an image tool only when this session already has one.
- Write a caption that says what the reader should see. Plain language. One or two short sentences.
- No new claims. If the writing does not say it, the figure does not show it.
- If no figure helps, set `figures: none` and say why in one sentence.

## figures.md

Write `figures.md` and each figure source in the target folder the requester names. When no folder is named, stop and ask.

```markdown
# Figures

- writing: path of the file you drew from
- figures: 1

## 1. Claim sentence as the heading

- claim: the sentence from the writing
- caption: what the reader should see
- source: `figure-1.mmd`
- image: `figure-1.png` or `none`
```

Use `figures: none` and no `##` sections when you draw nothing.

## Check

A person checks each figure against the claim sentence. The figure shows that claim and no other claim. They say pass, or they write `figures.check.md` beside `figures.md` with first line `pass` or `fail: <why>`. A fail stops the run. Edit the source in place. After a pass, delete the check file.
