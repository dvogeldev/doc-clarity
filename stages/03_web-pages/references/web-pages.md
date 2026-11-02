# Web pages rung - one HTML file

Ask for the output in HTML. Write one self-contained page. The reader can open it from disk. No install, no network, no build step.

The page is discardable. It is for this topic and this run. Do not turn it into a product framework.

## Rules

- Visible sentences come from `human/text.md` when the manifest lists it. That file is ISO 24495-1. Use `ste-human/text.md` only when `human` is `none`. Otherwise use the machine writing, and write so a person can use the page.
- The page helps the reader do the purpose named in the writing. Put the most important thing first.
- Add interaction only when it helps that purpose: show a step, compare two states the writing already names, or move a control the writing already describes.
- Do not add a claim, a metric, or a section the writing does not contain.
- Inline the CSS and the script. Do not use a remote font, script, or image URL.
- When `figures.md` exists and `figures` is not `none`, draw those figures in the page. Inline an SVG or a simple HTML figure. Do not depend on a PNG path outside the file.
- Use real headings. The reader can reach every control from the keyboard. Text and its background must contrast enough to read.
- Name the page with the writing's title.
- This stage does not certify WCAG. It does keep headings, keyboard access, and contrast so a person can use the page.

## File

Write `stages/03_web-pages/output/{slug}/page.html`. `{slug}` comes from stage 01 `current.md`.
