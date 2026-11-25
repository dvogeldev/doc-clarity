# Explainer videos rung - text first, then a render

The narration and the shot list come first. A video file comes only after a person passes the text, and only when this session can already render one.

Karpathy's example prompt is: create a 3b1b-style video explainer on the topic, and use a voice tool for narration. He also says to ask for a free alternative that uses local compute when you do not have a voice API. The skill follows the local path unless a voice tool is already configured.

## Input

Load one accepted writing file. Use the human file when it exists. Use the 80-percent file only when the human file was not written. Use the machine file only when neither of those exists. Do not load a second writing file. Require the person to have passed that file's check.

When a passed `figures.md` exists for this run, read it too. When it does not exist, use the writing only.

## Narration

- Put one idea in each sentence. Keep the same claims and the same order. You may split a sentence. You may not add a claim.
- Say the purpose in the first two sentences.
- Use words a person can say aloud. Plain language wins over a robotic reading. Keep the approved word when the writing already chose it.
- Aim for one to three minutes. Split a longer topic into two runs.

## Shots

- Use one shot for each narration sentence, or a small group of sentences that show one picture.
- Each shot names what is on screen and which narration lines play.
- Use a figure from the diagrams rung when that figure carries the claim. Do not invent a picture that adds a claim.
- "3b1b style" means a clear visual buildup: one idea on screen, and the picture changes with the sentence. Do not copy a creator's assets, brand colors, or footage.

## Voice and render

- Do not ask for an API key. Do not write a key into any file.
- If the session has no render tool, stop after the text files. In `manifest.md` set `render: not-produced` and the reason.
- If the session can render after the check passes, write the video next to the text and set `render:` to the file name.

## Files

Write these in the target folder the requester names. When no folder is named, stop and ask.

`narration.md` is the spoken text, one sentence per line, with the purpose in the first two lines.

`shots.md` is a numbered list. Each item names the picture and the narration lines that play over it.

`manifest.md`:

```markdown
# Manifest

- writing: path of the file you spoke from
- narration: `narration.md`
- shots: `shots.md`
- render: a file name, or `not-produced`
- reason: write this line only when render is `not-produced`
```

## Check

A person reads the narration aloud against the writing. The claims match. The order matches. They say pass, or they write `narration.check.md` beside the text with first line `pass` or `fail: <why>`. A fail stops the run. Render happens only after this pass. If a video file exists, the person watches it once and confirms the picture matches `shots.md`. If it does not, they set the check back to `fail:` and the reason. After a pass, delete the check file.
