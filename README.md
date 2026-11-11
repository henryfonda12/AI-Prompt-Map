# AI Prompt Map

**69 ready-to-use prompts for working with AI, organized by situation.** They help you keep thinking when an agent does the work, ask AI for more, and verify the result harder.

Every prompt stands on its own: pick your situation, copy the prompt, fill in your own fields, and paste it into any chat or agent.

**Open the map:** `index.html` is a single page. It works with a double-click and offline (except for the fonts).

## How to pick a prompt

- **By situation.** “An agent is writing code”, “The AI says done”, “Reviewing a PR before merging”, “A document has to survive a hostile review”: 36 situations, each with a route of 1–3 prompts in the right order.
- **By stage of work.** Eight islands, from start to finish:

  | Island | Blocks |
  |---|---|
  | Start | one-liners, standing instructions, universal multi-prompt |
  | Framing | delegate or not, the brief, an unfamiliar task |
  | Making | architecture, code and debugging, writing |
  | Checking | code review, verification, document synthesis, high-stakes decisions, red team |
  | Scale | multi-agent work, long sessions |
  | Finish and grow | finishing a task, calibrating your skills |
  | Ambition | altitude, depth, range |
  | Fresh eyes | fresh eyes, prototype instead of permission |

- **By phase and place.** Filters for BEFORE / DURING / AFTER / ONGOING and any chat / same chat / new chat / agent with tools.
- **By search.** A word from a situation, the prompt text, or a number (`9.1`). Press `/` to jump to search.
- **No time.** 14 one-liners for the moment right after the AI answers.

Fields like `[MY HYPOTHESIS]` are yours to fill in before you send. That's the whole point. The Copy button copies the prompt and reminds you which fields are yours.

## What's inside

| Path | What it is |
|---|---|
| `source/ai-prompt-map.md` | The source: every prompt, the situation table, the checklist, the glossary. This is the only file you edit. |
| `src/parse.py` | Parses the source into JSON word for word and validates its structure. |
| `src/template.html` | The interface: islands, routes, search, filters, copying. |
| `src/build.py` | Inserts the data into the template. |
| `build.sh` | Rebuilds everything with one command. |
| `index.html` | The finished page. |
| `dist/` | Intermediate data and the page without the `<!doctype>` wrapper. |

## How to update

1. Edit `source/ai-prompt-map.md` following the rules in its “New prompt template and editing rules” section.
2. Run `./build.sh` (needs only Python 3). If anything is wrong, the build stops with exit code 1, lists the errors and **leaves** `index.html` and `dist/` **untouched**. The build checks that:
   - every line of the source made it into the data;
   - every prompt has a ```` ```text ```` block and no number is repeated;
   - block and prompt headings follow the template;
   - every `[N.M](#N-...)` link points to an existing prompt in its own block;
   - every block belongs to an island;
   - every section the template relies on is present.
3. Open `index.html`.

Islands are defined in `src/template.html`, in the `ISLES` constant. **A new block must be added to an island**, or the build stops. Routes are built automatically from the “Situation and prompt” table: “then” is the next step, “or” is an alternative, and a comma pairs prompts that go together.
