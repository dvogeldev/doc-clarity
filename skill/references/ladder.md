# Ladder - four rungs for understanding model output

Andrej Karpathy, 2 Oct 2026, described four ways to make model output easier to understand. The post is the source. See [sources.md](sources.md).

He presents the rungs as a climb. Each one can replace a wall of text. The skill runs them in order so a person can correct the claims in writing before a figure, a page, or a video repeats those claims. Stop after any check that passes. The brief field `climb-to` names the last rung.

## 1. Writing

Ask for ASD-STE100. Use short sentences, one idea each, active voice, and a controlled vocabulary. When full STE sounds too rigid for a person, ask for 80 percent of the way to ASD-STE100.

The skill splits that rung by reader. The contract is [writing.md](writing.md).

- Machine readers get full ASD-STE100.
- Human-readable ASD-STE100, when the brief sets `ste-human: 80`, targets 80 percent adherence.
- People get plain language under ISO 24495-1. That file does not use the 80 percent target.

## 2. Diagrams

Use a figure when it is easier to process, parse, and understand than a paragraph. One claim in each figure. No new claims. The contract is [diagrams.md](diagrams.md).

## 3. Web pages

Ask for the output in HTML. One self-contained page. Interaction only when it helps the reader do the task. The page is discardable. The contract is [web-pages.md](web-pages.md).

## 4. Explainer videos

This is the rung he is most bullish on: a custom explainer on the topic. The example shape from the post is a 3b1b-style video, with narration from a voice tool you already have, or a free local alternative. The skill writes the narration and the shots first. It renders only after that check passes. It never stores an API key. The contract is [videos.md](videos.md).

## Why the order is fixed

A wrong claim is cheap to fix in writing and expensive inside a video. Later rungs repeat the checked claims. They do not extend them. The page and the video both read the writing and any passed figures. The page is not an input to the video.

## Oversight

The person owns the check at every rung. The agent drafts. The person decides the meaning is right before the next rung starts. As models do more of the legwork, the human work moves up into oversight and understanding. Custom pages and videos are now cheap enough to make for one topic and then discard.
