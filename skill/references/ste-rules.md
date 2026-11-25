# Simplified Technical English - machine-facing rules

The Issue 9 writing rules are in [ste-issue-9.md](ste-issue-9.md). This file is the replacement list `_tools/ste_check.py` enforces. It is not the official dictionary. Do not certify a document against this file. When this list and the digest disagree, follow the digest, then make the checker pass or record `clarity-exceptions`.

ASD owns ASD-STE100. Get the official PDF from <https://www.asd-ste100.org/>.

## Vocabulary

- **Approved words only, one meaning each.** Every word carries exactly one part of speech and one sense within this document set.
- **No synonyms.** Once `use` is the verb for employing something, never `utilize`, `employ`, or `apply` for the same act anywhere in the workspace.
- **No idioms, metaphors, jargon, or invented words.** "At the end of the day" becomes "finally"; "leverage" becomes "use".
- **Approved replacements** (keep in sync with `_tools/ste_check.py`):

| Write this | Not this |
|---|---|
| use | utilize, employ |
| help | assist, facilitate |
| start | commence, initiate |
| stop | end (a process), discontinue, terminate |
| before | prior to |
| to | in order to |
| if | in the event of |
| because | due to the fact that |
| about | approximately, regarding, concerning |
| enough | sufficient |
| get | obtain |
| need | require, necessitate |
| try | attempt |
| show | demonstrate, indicate |
| find out | determine |
| make sure | ensure |
| carry out | implement |
| check | verify, monitor |
| tell | notify |
| part | portion |
| have | possess |
| buy | purchase |
| send | transmit |
| whether | whether or not |

## Sentences

- **Max 20 words** per sentence (25 for descriptive, non-procedural text).
- **One action per sentence.** Split compound actions: "Close the valve. Open the vent." Never write "Close the valve and open the vent" inside a procedure.
- **Condition before action.** "If the valve is open, close it." A trailing condition gets lost by machine readers mid-procedure.
- **Imperative for instructions.** "Close the valve." Never "The valve should be closed" or "You will need to close the valve".
- **Active voice.** Passive only when the actor is unknown or irrelevant; the checker flags the rest.
- **Repeat the noun** instead of an ambiguous pronoun when two nouns could own it. "The pump feeds the tank. The tank vents to air." Not "…It vents to air."
- **Verb beats noun.** "Inspect the valve", not "perform an inspection of the valve"; "measure", not "make a measurement".

## Procedures

- One step, one action, steps in execution order.
- Warnings, cautions, and notes precede the step they protect, with their standard signal words (`WARNING:` injury risk, `CAUTION:` damage risk, `NOTE:` information only).
- More than about 7 sub-steps: split into two steps.

## Structure

- Headings name their content exactly. A machine scanning headings routes correctly on headings alone.
- One topic per paragraph. Paragraphs short.

## Local additions

None yet.

Append approved technical names and technical verbs here when a run needs a word the approved list does not have. Add the same word to `_tools/ste_check.py` in the same change.
