# Explainer videos rung - text first, then a render

The narration and the shot list come first. A video file comes only after a person passes the text, and only when this session can already render one.

Karpathy's example prompt is: create a 3b1b-style video explainer on the topic, and use a voice tool for narration. He also says to ask for a free alternative that uses local compute when you do not have a voice API. This workspace follows the local path unless a voice tool is already configured outside the repo.

## Narration

- Use `human/text.md` when the manifest lists it. That file is ISO 24495-1. Use `ste-human/text.md` only when `human` is `none`. Otherwise use the machine writing.
- Put one idea in each sentence. Keep the same claims and the same order. You may split a sentence. You may not add a claim.
- Say the purpose in the first two sentences.
- Use words a person can say aloud. Plain language wins over a robotic reading. Keep the approved word when the writing already chose it.
- Aim for one to three minutes. Split a longer topic into two runs.

## Shots

- Use one shot for each narration sentence, or a small group of sentences that show one picture.
- Each shot names what is on screen and which narration lines play.
- Use a figure from stage 02 when that figure carries the claim. Do not invent a picture that adds a claim.
- "3b1b style" means a clear visual buildup: one idea on screen, and the picture changes with the sentence. Do not copy a creator's assets, brand colors, or footage.

## Voice and render

- Do not ask for an API key. Do not write a key into this workspace.
- If the session has no render tool, stop after the text files. In `manifest.md` set `render: not-produced` and the reason.
- If the session can render after the check passes, write the video next to the text and set `render:` to the file name.

## Files

Write these under `stages/04_explainer-videos/output/{slug}/`. `{slug}` comes from stage 01 `current.md`.

`narration.md` is the spoken text, one sentence per line, with the purpose in the first two lines.

`shots.md` is a numbered list. Each item names the picture and the narration lines that play over it.

`manifest.md`:

```markdown
# Manifest

- slug: `{slug}`
- writing: path of the file you spoke from
- narration: `narration.md`
- shots: `shots.md`
- render: a file name, or `not-produced`
- reason: write this line only when render is `not-produced`
```
