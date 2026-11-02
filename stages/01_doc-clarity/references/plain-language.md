# Plain language - human-facing rules

Distilled from ISO 24495-1:2023 (Plain language, Part 1: Governing principles and guidelines). Official record: <https://www.iso.org/standard/78907.html>. The definition the standard builds on: people can find what they need, understand it, and use it, with the effort a person would consider reasonable.

## Four principles

- **Relevant.** The text contains what the reader needs for their purpose, and nothing that buries it. Irrelevant detail is a cost the reader pays.
- **Findable.** The reader reaches what they need without hunting: most important information first, task-oriented headings, a visible structure that matches how the reader thinks about the work.
- **Understandable.** Vocabulary the reader already holds, sentences short enough to hold in mind, concrete nouns, no ambiguity the reader must resolve. Define any term they might not hold, at first use.
- **Usable.** After one read, the reader can do the thing: act, decide, or complete the task. This is the test the other three serve.

## Process (plain language is a process, not a style)

1. **Know the readers.** Who they are, what they already know, what they come to do. Name them in the output's frontmatter: `readers: new operators onboarding`.
2. **Define the purpose as the reader's task.** "To reset the sync key", not "to inform about sync key management".
3. **Write to that.**
   - Most important thing first; reader's goal in the opening, not background.
   - Headings phrased as tasks or questions: "How to reset the sync key", not "Sync key overview".
   - One idea per paragraph, one action per sentence where instructions appear.
   - Address the reader as "you"; active voice; verbs over noun phrases ("decide", not "make a decision").
   - Aim under 20 words a sentence; split rather than compress.
   - Contractions and warmth are allowed. This is for people, so it should sound like a person.
4. **Assess.** Reread as the target reader. For high-stakes docs, test with a real one: can they do the task after one read? Iterate.

## Where plain language differs from STE

| Plain language (human) | STE (machine) |
|---|---|
| "You" encouraged | Imperative only; no "you will need to" |
| Contractions fine | No contractions |
| Reader's own vocabulary | Approved vocabulary only |
| Warmth and tone matter | Tone is irrelevant; ambiguity is the only enemy |
| Sentence limits are aims | Sentence limits are hard rules |

When one document must serve both audiences, split it. Use one file per audience, and cross-link the files.
