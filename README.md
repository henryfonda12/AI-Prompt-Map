# AI Prompt Map

**69 ready-to-use prompts for working with AI, organized by situation.** They help you keep thinking when an agent does the work, ask AI for more, and verify the result harder.

Every prompt stands on its own: pick your situation, copy the prompt, fill in your own fields, and paste it into any chat or agent.

**Who it's for:** anyone who works with ChatGPT, Claude, Gemini or a coding agent every day and wants to stay the one doing the thinking. About a third of the prompts are about code (review, debugging, agents); the rest cover writing, research, decisions and strategy.

**[Open the map →](https://henryfonda12.github.io/AI-Prompt-Map/)**

**First time?** Find your situation in the left column and copy the first prompt of its route. Not sure? Use 2.2 before a task and 15.1 when the AI says it's done.

Prefer it offline? Click **Code → Download ZIP**, unzip, and double-click `index.html`. It's one self-contained page (only the web fonts need a connection).

## How to pick a prompt

- **By situation.** “An agent is writing code”, “The AI says done”, “Reviewing a PR before merging”, “A document has to survive a hostile review”: 36 situations, each with a route of 1–3 prompts in the right order.
- **By stage of work.** The 23 blocks of prompts are grouped into eight islands, from start to finish:

  | Island | Blocks |
  |---|---|
  | Start | one-liners, standing instructions, universal multi-prompt |
  | Framing | delegate or not, the brief, an unfamiliar task |
  | Making | architecture, code and debugging, writing |
  | Checking | code review, verification, document synthesis, high-stakes decisions, red teaming |
  | Scale | multi-agent work, long sessions |
  | Finish and grow | finishing a task, calibrating your skills |
  | Ambition | aiming higher, going deeper, going wider |
  | Fresh eyes | fresh eyes, prototype instead of permission |

- **By phase and environment.** Filters for when (BEFORE / DURING / AFTER the task, or ONGOING habits) and where to paste it (any chat / same chat / new chat / agent with tools).
- **By search.** A word from a situation, the prompt text, or a number (`9.1`). Press `/` to jump to search.
- **Short on time.** 14 one-liners, most for the moment right after the AI answers.

Fields like `[MY HYPOTHESIS]` are yours to fill in before you send. That's the whole point. The Copy button copies the prompt and reminds you which fields are yours.

## Learn it with an AI coach

Reading the map isn't the same as practicing it. Give the map file to any AI chat and paste the prompt from [COACH.md](COACH.md). The coach asks one question about your work, builds an example from it, and walks you through all 69 prompts, one at a time.

## Feedback

Found a prompt that misfires, or a situation that's missing? [Open an issue](https://github.com/henryfonda12/AI-Prompt-Map/issues).

## For maintainers

| Path | What it is |
|---|---|
| `source/ai-prompt-map.md` | The source: every prompt, the situation table, the checklist, the glossary. This is the only file you edit. |
| `src/parse.py` | Parses the source into JSON word for word and validates its structure. |
| `src/template.html` | The interface: islands, routes, search, filters, copying. |
| `src/build.py` | Inserts the data into the template. |
| `build.sh` | Rebuilds everything with one command. |
| `index.html` | The finished page. |
| `dist/` | Intermediate build output. |

To update:

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
