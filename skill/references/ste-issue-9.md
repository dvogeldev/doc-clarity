# ASD-STE100 Issue 9 - agent digest

ASD-STE100 Simplified Technical English (Issue 9, Jan 2025). Core rules and constraints for deterministic technical writing.

The replacement list that `ste_check.py` enforces is in [ste-rules.md](ste-rules.md). This file is the rule digest. It does not contain the controlled dictionary.

STE is a controlled natural language for technical documentation. Goal: clear, unambiguous text that non-native English readers (and LLMs and translators) can parse reliably. Two parts: writing rules (grammar and style) and a controlled dictionary (approved words, meanings, and parts of speech).

## Core operating principles for an agent

- Prefer dictionary-approved words. Use them only with the approved meaning and part of speech.
- Technical nouns and technical verbs (domain terms from a company glossary or terminology database) are allowed when they fit the defined categories.
- Short sentences, one idea or topic per sentence, active voice preferred.
- Procedures: imperative form, max about 20 words per sentence. Descriptive text: gradual information, no imperatives.
- No contractions, no omitted words, no complex tenses, no long multi-word nouns (more than 3 words without restructuring).
- American English spelling by default.
- Always prefer vertical lists over long series in running text.

## Section 1 - Words

**1.1** Use only dictionary-approved words, technical nouns, or technical verbs.

**1.2** Use approved words only in their specified part of speech.

**1.3** Use them only with their approved meaning (often narrower than general English).

**1.4** Use only approved verb and adjective forms (base, simple present, simple past, simple future, past participle as adjective). No other tenses.

**1.5-1.11 Technical nouns.** 22 categories: parts, vehicles, tools, materials, facilities, systems, math and science, navigation, numbers and units, quoted text, roles and organizations, body parts, personal effects, medical, documents and standards, environment, colors, damage, IT and computer, civil and military operations, law and regulations, animals and plants. Use short, consistent, non-jargon terms approved in the subject field. Do not verb them.

**1.12-1.13 Technical verbs.** 4 categories: manufacturing processes, computer processes, subject-field instructions, law and regulations. Prefer dictionary verbs when possible. Do not noun them.

**1.14** American English spelling unless official directives override. Keep quoted text as-is.

## Section 2 - Multi-word nouns

**2.1** Max 3 words. Break longer ones with prepositions or restructure.

**2.2** For official long technical nouns: write the full form once, then use a shorter form, an abbreviation, or hyphens. A hyphenated unit counts as one word. Never force hyphens to fake a short count.

## Section 3 - Verbs

**3.1-3.2** Only these forms and tenses: infinitive, imperative, simple present, simple past, simple future, past participle (as adjective). No perfect, progressive, or complex constructions.

**3.3** A past participle used as an adjective shows a condition (before the noun, or after be, become, or stay).

**3.4** No auxiliary plus past participle for complex or passive constructions.

**3.5** "-ing" only as a technical noun, or as a modifier inside a technical noun.

**3.6** Prefer active voice. Passive only in descriptive writing when the agent is unknown.

**3.7** Describe actions with approved verbs, not nouns.

## Section 4 - Sentences

**4.1** Short, clear sentences. One topic per sentence in descriptive text. Procedures use the imperative.

**4.2** Do not omit words. Do not use contractions.

**4.3** Use vertical lists for a complex series. Use a colon, then items that start with a capital. Use a period only on full sentences or on the last item.

**4.4** Use approved connecting words and phrases (and, but, then, thus, as a result, this, these, and the other approved connectors).

**4.5** Use articles (a, an, the) or demonstratives (this, these) where needed. Do not drop them for shortness. No article before an alphanumeric identifier that acts as a proper noun.

## Section 5 - Procedural writing

**5.1** Max 20 words per sentence. Notes: 25. Safety instructions obey the same limit.

**5.2** One instruction per sentence unless the actions occur at the same time.

**5.3** Imperative form only for instructions. Avoid "must" except for a critical safety condition.

**5.4** Write the condition first, then a comma, then the command.

**5.5** Notes give information only. A note never gives an instruction.

## Section 6 - Descriptive writing

Give information gradually. One topic per sentence and per paragraph. Use key words and phrases. Keep paragraphs focused and reasonably short. Use a logical structure. Do not write dense blocks.

## Section 7 - Safety instructions

Use clear warning, caution, and note language. Make a negative command explicit (`DO NOT`). Keep the instruction short and direct.

## Section 8 - Punctuation and word count

Use standard English punctuation. The semicolon is discouraged. Word-count rules apply especially to procedures (20) and notes (25). Numbers plus units, proper nouns, abbreviations, and similar items have specific counting treatments in the standard. Keep quoted text as-is.

## Section 9 - Writing practices

Use a different sentence construction when a word-for-word replacement fails. Keep a consistent style. Issue 9 adds inclusive-language guidance and possessive-form rules. Avoid false friends, Latin abbreviations, and similar traps.

## Agent usage notes

- The dictionary is mandatory for full compliance. This digest covers the rules. Part 2 of the standard contains the controlled vocabulary: approved words in uppercase, non-approved words with alternatives, meanings, and examples. Without the dictionary, prefer short, high-frequency technical vocabulary and flag domain terms for a glossary check.
- Technical nouns and technical verbs must come from the user's company glossary or subject-field terminology. Do not invent them.
- Output should be auditable: short sentences, explicit subjects, active voice, and vertical lists where they help.
- STE improves machine translation and LLM reliability because the vocabulary and the sentence patterns are constrained.
- This is a controlled standard, not "simplified English" in the marketing sense. Precision wins when precision and brevity conflict.

## Sources

ASD-STE100 Issue 9 (Jan 2025). The full standard is available from ASD/STEMG at <https://www.asd-ste100.org/>. These rules are summarized for agent context. Cross-check the dictionary for production use.
