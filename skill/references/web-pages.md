# Web pages rung - one HTML file

Ask for the output in HTML. Write one self-contained page. The reader can open it from disk. No install, no network, no build step.

The page is discardable. It is for this topic and this run. Do not turn it into a product framework.

## Input

Load one accepted writing file. Use the human file when it exists. Use the 80-percent file only when the human file was not written. Use the machine file only when neither of those exists, and write so a person can use the page. Do not load a second writing file. Require the person to have passed that file's check.

When a passed `figures.md` exists for this run, read it too. When it does not exist, build from the writing only.

## Rules

- The page helps the reader do the purpose named in the writing. Put the most important thing first.
- Add interaction only when it helps that purpose: show a step, compare two states the writing already names, or move a control the writing already describes.
- Do not add a claim, a metric, or a section the writing does not contain.
- Inline the CSS and the script. Do not use a remote font, script, or image URL.
- When `figures.md` exists and `figures` is not `none`, draw those figures in the page. Inline an SVG or a simple HTML figure. Do not depend on a PNG path outside the file.
- Use real headings. The reader can reach every control from the keyboard. Text and its background must contrast enough to read.
- Name the page with the writing's title.
- This rung does not certify WCAG. It does keep headings, keyboard access, and contrast so a person can use the page.

## File

Write `page.html` in the target folder the requester names. When no folder is named, stop and ask.

## Check

A person opens `page.html` from disk and does the purpose named in the writing. They can find it, understand it, and use it on one pass. They say pass, or they write `page.check.md` beside the file with first line `pass` or `fail: <why>`. A fail stops the run. Edit the page in place. After a pass, delete the check file. The video rung does not read this page.
