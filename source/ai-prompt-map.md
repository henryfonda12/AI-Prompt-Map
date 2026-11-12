# AI Prompt Map: ambitious work and critical thinking when AI does the work

A library of ready-to-use multi-step prompts, organized by situation. Every prompt stands on its own: copy the whole prompt and paste it into any chat or agent.

**Why this exists.** The goal isn't to use AI less. Blocks 0–16 help you keep thinking when it's tempting to hand everything to an agent. Blocks 17–19 are about asking AI for more: higher, deeper, wider. Block 20 is the adversarial check that keeps that ambition honest. Blocks 21–22 are about using fresh eyes and cheap execution when you don't have the seniority to push things through. Put together: notice, ask for more, show with a prototype, and verify harder.
- You have to build critical thinking into your day on purpose, because it won't switch on by itself. Working with agents feels good, and that's exactly why your guard drops without you noticing.
- The better the models get, the more dangerous this becomes. Obvious mistakes get rarer, answers are smooth and mostly right, and a second look starts to feel unnecessary. That's the trap.
- Quizzes, interviews and evidence only happen if you set them up yourself. That's what the prompts below are for.

**The spectrum.** Be honest about where you are right now:
- **Cognitive offloading** is healthy. You delegate the task but you own the result.
- **Deferral**: the tool's answer becomes your input and stops being a hypothesis.
- **Cognitive surrender**: the AI's answer quietly becomes yours, and you no longer feel any need to check it.
- The slide is gradual. You read the first answer carefully, skim the next one, then only glance at the outline. Eventually someone asks you about a line and you can't explain it, even with the agent's help.

## How to use

- **Placeholders.** Any `[PLACEHOLDER]` can be replaced with “see above in this chat” or “I don't know”. Don't skip the fields where you do the thinking: `[MY HYPOTHESIS]`, `[THESIS]` (12.1), `[MY POSITION]` (11.1), `[MY SUMMARY]` (10.3), `[MY EXPLANATION]` (5.3), lines picked at random `[FILE:LINE]` (8.2), `[MY UNVERIFIED THING]` (15.1), `[ACCEPTANCE BAR]` (18.2), `[BELIEF]` (18.3), `[MY NOTES]` (21.1), `[IDEA]` (21.2, 22.1) and `[GOAL]` (12.1, 22.1, 22.2). Fill them in before you send, even with a bad guess. This is one of the core techniques here.
- **Environment labels** sit under each prompt's title:
  - `[ANY CHAT]`: works anywhere, in a new chat or the current one.
  - `[SAME CHAT]`: paste into the chat where the work happened. The model needs the history.
  - `[NEW CHAT / OTHER MODEL]`: needs fresh eyes with no history: a new chat, a different model, or a subagent.
  - `[AGENT WITH TOOLS]`: needs to run commands or access files. It still works without tools, but the checks will come back to you as a list of commands.
- **Phases:** BEFORE (before you hand off the task) / DURING (the AI has produced something) / AFTER (the AI says it's done) / ONGOING (habits).
- **Short** is a 2–3 line version of a long prompt for when you don't have time for the full one.
- **The HONESTY line** is identical in every full prompt about checks, command output and sources (one-liners and Short versions carry a one-sentence form). Don't delete it: without it, a model can “show” you output from something that never ran.
- **Combine them.** Not sure what to pick? Use [2.2](#2-universal-multi-prompt) at the start and [15.1](#15-finishing-any-task) at the end. No time even for that? Use the [one-liners](#0-one-liners).

## Contents

- [Situation and prompt](#situation-and-prompt)
- [0. One-liners](#0-one-liners)
- [1. Standing instructions](#1-standing-instructions)
- [2. Universal multi-prompt](#2-universal-multi-prompt)
- [3. Delegate or not](#3-delegate-or-not)
- [4. Framing the task and the brief](#4-framing-the-task-and-the-brief)
- [5. A new unfamiliar task](#5-a-new-unfamiliar-task)
- [6. Architecture and design](#6-architecture-and-design)
- [7. Writing code and debugging](#7-writing-code-and-debugging)
- [8. Code review and PRs](#8-code-review-and-prs)
- [9. Verification](#9-verification)
- [10. Research and document synthesis](#10-research-and-document-synthesis)
- [11. High-stakes decisions](#11-high-stakes-decisions)
- [12. Writing and content](#12-writing-and-content)
- [13. Multi-agent work and orchestration](#13-multi-agent-work-and-orchestration)
- [14. Long sessions and handing off context](#14-long-sessions-and-handing-off-context)
- [15. Finishing any task](#15-finishing-any-task)
- [16. Calibrating your skills](#16-calibrating-your-skills)
- [17. Aiming higher](#17-aiming-higher)
- [18. Going deeper](#18-going-deeper)
- [19. Going wider](#19-going-wider)
- [20. Red teaming with adversarial agents](#20-red-teaming-with-adversarial-agents)
- [21. Fresh eyes](#21-fresh-eyes)
- [22. Prototype instead of permission](#22-prototype-instead-of-permission)
- [The 30-second checklist](#the-30-second-checklist)
- [New prompt template and editing rules](#new-prompt-template-and-editing-rules)
- [Glossary](#glossary)
- [Changelog](#changelog)

## Situation and prompt

| Situation | Prompt |
|---|---|
| A second to ask something after the AI answers | [0.1–0.14](#0-one-liners) |
| Setting up CLAUDE.md, AGENTS.md, custom instructions or a project | [1.1](#1-standing-instructions) |
| A non-trivial task and no time to pick | [2.2](#2-universal-multi-prompt) to start, [2.1](#2-universal-multi-prompt) for the full cycle |
| Can I hand off the whole task? | [3.1](#3-delegate-or-not) |
| Something small where a mistake costs nothing | [3.2](#3-delegate-or-not) |
| I'm not fully sure what I want | [4.1](#4-framing-the-task-and-the-brief) |
| Two rounds of edits and it's still not right | [4.3](#4-framing-the-task-and-the-brief), then [4.2](#4-framing-the-task-and-the-brief) |
| Unfamiliar territory, no reference points | [5.1](#5-a-new-unfamiliar-task) |
| Choosing an architecture or approach | [6.1](#6-architecture-and-design), then [6.2](#6-architecture-and-design) in a new chat |
| An agent is writing code | [9.2](#9-verification), then [7.1](#7-writing-code-and-debugging), then [7.2](#7-writing-code-and-debugging) in a new chat |
| A bug or an incident | [7.4](#7-writing-code-and-debugging) |
| I need to understand someone else's or generated code | [7.3](#7-writing-code-and-debugging) |
| Reviewing a PR before merging | I read the diff myself, then [8.1](#8-code-review-and-prs), then [8.2](#8-code-review-and-prs) |
| The AI says “done” or “tests are green” | [9.1](#9-verification) |
| The AI summarized lots of documents or interviews | [10.1](#10-research-and-document-synthesis) or [10.2](#10-research-and-document-synthesis) |
| A big decision, money, strategy, and I have a firm position | [11.1](#11-high-stakes-decisions) in 2–3 models, [11.3](#11-high-stakes-decisions) |
| Writing that goes out under my name | [12.1](#12-writing-and-content), [12.2](#12-writing-and-content) |
| Several agents and I can't keep up with checking | [13.1](#13-multi-agent-work-and-orchestration), [13.3](#13-multi-agent-work-and-orchestration) |
| Handing a subtask to another agent | [13.2](#13-multi-agent-work-and-orchestration) |
| A long session and I've lost the thread | [14.1](#14-long-sessions-and-handing-off-context) |
| Running out of context, moving to a new chat | [14.2](#14-long-sessions-and-handing-off-context) |
| Closing a task, merging, shipping | [15.1](#15-finishing-any-task) |
| Once a week or once a month | [16.1](#16-calibrating-your-skills), [16.2](#16-calibrating-your-skills) |
| I'm doing a “task”, but what I need is the outcome behind it | [17.1](#17-aiming-higher) |
| I keep giving the agent the same thing over and over | [17.2](#17-aiming-higher) |
| We run a process out of habit and I want it better | [17.3](#17-aiming-higher) |
| It needs to be genuinely good, not just a lot | [18.1](#18-going-deeper), then [18.2](#18-going-deeper) |
| Decisions rest on a belief nobody has tested | [18.3](#18-going-deeper) |
| I want to find what we don't know in the data | [18.4](#18-going-deeper) |
| A solution is stuck inside one field | [19.1](#19-going-wider), [19.2](#19-going-wider) |
| High stakes, I want someone to try to break the code | [20.1](#20-red-teaming-with-adversarial-agents) |
| A document or decision has to survive a hostile review | [20.2](#20-red-teaming-with-adversarial-agents) |
| A big task and I want a build–break–judge loop | [20.3](#20-red-teaming-with-adversarial-agents) |
| I'm new and a lot of things look odd | [21.1](#21-fresh-eyes) |
| I hear “that's impossible” or “we already tried” | [21.2](#21-fresh-eyes) |
| I have an idea but not the clout to push it | [22.1](#22-prototype-instead-of-permission), then [22.2](#22-prototype-instead-of-permission) |

---

## 0. One-liners

**When to use:** you don't have time for a big prompt. Unless noted otherwise, one-liners are for the DURING or AFTER phase (the AI just answered) and go into the same chat (`[SAME CHAT]`); 0.11 and 0.12 come before the task.

**0.1** What decisions the model made for you
```text
What decisions did you make for me without being told to: defaults, interpretations, what you left out of scope, where you chose between conflicting requirements?
```

**0.2** What wasn't checked
```text
What did you NOT check in this result? List it honestly, even if it seems minor.
```

**0.3** What would make the answer wrong
```text
What would have to be true for this result to be wrong? How can I check that cheaply with a real test rather than a confidence estimate?
```

**0.4** What's missing
```text
What did I miss? Name 2–3 things we didn't account for: requirements, edge cases, side effects, people this affects.
```

**0.5** Commands and output (I'll check against the log). `[SAME CHAT]`, ideally `[AGENT WITH TOOLS]`
```text
Show me the exact commands you ran and their raw output, not a summary. HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”. For each command, tell me where I can find its real output myself (tool log, terminal, CI run) so I can compare.
```

**0.6** What the green check proved
```text
What exactly did this green check prove, and what didn't it? Could it have passed with the feature broken?
```

**0.7** Interview instead of guessing
```text
Before you continue, interview me about what you don't understand in this task. Ask 1–3 questions at a time.
```

**0.8** The opposite position. `[SAME CHAT]`, ideally `[NEW CHAT / OTHER MODEL]`
```text
Argue the opposite position as strongly as you can. Don't look for a compromise and don't give a verdict.
```

**0.9** Quiz on the result
```text
Ask me 3 questions about this result that I should be able to answer without hints. Show the answers only after I've given mine.
```

**0.10** An explanation instead of a one-liner
```text
I don't understand this. Don't give me a one-line explanation: give me a short plan of what to understand and in what order, explain the first step, and check me with one question.
```

**0.11** The goal behind the goal (altitude). `[ANY CHAT]`, BEFORE
```text
Before you start: what decision or action will follow from this result? Suggest a framing that sets it up directly, and tell me what you're missing to do that.
```

**0.12** Deeper, not more. `[ANY CHAT]`, BEFORE
```text
What methods and tools would the best professional in this field use, what raw material would they start from, and what, other than you, would show the result is correct? Don't change the vocabulary, change the method.
```

**0.13** Break it. Only `[NEW CHAT / OTHER MODEL]` or a subagent, AFTER
```text
THE RESULT AND WHAT IT PROMISES: [RESULT]. You win by producing a reproducible failure of this result: a failing test, a counterexample, or an input it gets wrong. Don't fix anything. A finding you didn't run is a hypothesis; don't invent output: if you didn't run it, write “NOT RUN”. “No problems found” is a loss; a made-up problem is a bigger loss.
```

**0.14** Is it really impossible? `[ANY CHAT]`, DURING
```text
Break this “impossible” (or “we already tried”) into separate reasons. Which are verified facts and which are hearsay? Who or what can confirm each one directly, and what has changed since the last attempt?
```

---

## 1. Standing instructions

**When to use:** ONGOING. Paste once into CLAUDE.md, AGENTS.md, Custom Instructions, a project's system prompt (Projects) or at the start of a long chat. After that, the basic habits work without copying anything.

**Keep in mind:**
- Quizzes, evidence and the list of decisions only appear if you've set them up in advance. By default nothing triggers them.
- When something falls short of your bar, add a rule here, to a hook or to a test. Then it fires for everyone, automatically, and your standards keep compounding.

### 1.1 Baseline rules for any assistant
`[ANY CHAT]` (standing setup) · ONGOING

```text
Rules for working with me (always in effect):
1. If the result would be wrong without an answer to a question, ask before you start. Otherwise list your assumptions and keep going.
2. After any non-trivial work, answer in this order: evidence → decisions you made yourself (defaults, interpretations, conflicting requirements, what's out of scope) → what was NOT checked → a summary of no more than 5 lines.
3. HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.
4. For every check, say what it proved and what it didn't.
5. At the end of a task, ask yourself “what did I miss?” and add what you find.
6. If you changed code, finish by asking me 3 questions about specific places you changed. Don't show the answers until I've replied.
7. Don't make high-stakes decisions for me (what to build, what affects users, whether it's safe to ship): give me options and arguments.
8. For agents with tools: after any significant change, run a self-check (tests or an actual run) and a review by a subagent with none of our history; pass its findings to me unfiltered.
```

---

## 2. Universal multi-prompt

**When to use:** any non-trivial task when there's no time to pick a specialized block.

**Keep in mind:**
- The AI's answer is a hypothesis, not your conclusion. The moment it becomes your input without being checked, that's deferral, not offloading.
- Write your hypothesis down before you ask. After a smooth answer, it's hard to imagine an alternative.
- Evidence first, summary second. A green check proves one property, not everything.
- **Look at the real output YOURSELF, in the tool log, the terminal or CI. Output the model retyped into the chat doesn't count as evidence.**
- The ownership test: if you can't explain the result even with the AI's help, you don't own it. Understanding can be rebuilt on demand: [7.3](#7-writing-code-and-debugging).

### 2.1 Full cycle
`[ANY CHAT]` · BEFORE → AFTER

Short: use [2.2](#2-universal-multi-prompt).

```text
Do the task strictly in stages, in order, without skipping any.

MODE: [help me think / do it for me — I'm choosing deliberately]
TASK: [TASK]
CONTEXT (what's known, constraints, who the result is for): [CONTEXT]
MY HYPOTHESIS (what I expect the answer to be, written before yours): [MY HYPOTHESIS]
HOW I'LL KNOW IT'S DONE: [DONE CRITERIA]

HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Stage 1. Brief. 3–5 lines: goal, audience, out of scope, done criteria (if not given, propose some). If you suspect we're solving the wrong problem, say so. Ask questions ONLY if the result would be wrong without the answers: then ask up to 3 and stop. Otherwise list your assumptions and keep going.
Stage 2. The work. If MODE is “help me think”, don't hand me a finished conclusion: give me options, arguments and what I should check; I'll draw the conclusion.
Stage 3. Evidence: what you checked, how (command, source, calculation, test) and the raw result.
Stage 4. Decisions and assumptions: decisions made without my instruction (defaults, approach, interpretations); the assumptions everything rests on; where requirements conflicted and what you chose; what you left out of scope.
Stage 5. What was NOT checked. Answer: “What would have to be true for the result to be wrong?” and propose the cheapest real test.
Stage 6. Comparison with my hypothesis: where it matched, where it diverged, and what check would settle it.
Stage 7. Summary of no more than 5 lines.
Stage 8. Quiz: 3 questions about the result that I should be able to answer without hints. Don't show the answers. Stop here. After I answer, grade each one: correct / partly / wrong.
```

### 2.2 Short version (starting a task)
`[ANY CHAT]` · BEFORE. To close the task: [15.1](#15-finishing-any-task).

```text
Task: [TASK]
My guess at the answer: [MY HYPOTHESIS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Do the task. Then, in order: 1) evidence; 2) decisions and assumptions you made yourself; 3) what was NOT checked; 4) how my answer differs from yours; 5) a summary of up to 3 lines; 6) one question to test my understanding. Don't show the answer; stop there.
```

---

## 3. Delegate or not

**When to use:** BEFORE a task, when you're not sure whether you can hand all of it to AI.

**Keep in mind:**
- Where mistakes are cheap, hand it off completely (picking one of three hotels, say). Keep the reasoning for yourself where other people will deal with the fallout: investments, career advice for your kids and, at work, what to build, which changes affect users, whether it's safe to ship.
- You can and should hand error detection to agents. The decision and the sign-off stay with you: you can delegate the work and most of the audit, but not the responsibility.
- How much to trust an agent on a given task is also your call. Model failure modes keep changing, so calibrating trust takes review.
- Decide up front whether you want help thinking or someone to think for you. Either is fine as long as the choice is deliberate.

### 3.1 Sorting a task by stakes
`[ANY CHAT]` · BEFORE

```text
Help me split the work on this task between me and the AI. Do NOT solve the task itself. I'll choose the mode; you offer an assessment and arguments.

TASK: [TASK]
WHO GETS HURT IF THE RESULT IS WRONG: [WHO]

1. Cost of a mistake (low / medium / high) in 1–2 lines: who deals with the fallout, and whether it's reversible.
2. Which mode you'd suggest and why: “hand it off completely” / “hand off the work, I keep the checking” / “I think it through myself, the AI argues and asks questions”.
3. What can be handed off, and which decisions must stay with me (what we're doing, why, who it affects, what we're giving up).
4. What the check will look like: what I need to see with my own eyes.
5. One question for me that will show whether I understand the task well enough to delegate it.
```

### 3.2 Hand it off completely (low stakes)
`[ANY CHAT]` · BEFORE

```text
A mistake on this task is cheap. Do all of it, with no clarifying questions and no check-ins along the way.
TASK: [TASK]
At the end, one line: the main assumption you made, and one thing I should look at myself.
```

---

## 4. Framing the task and the brief

**When to use:** BEFORE a task, when the result could easily “look finished” and you don't fully know what you want; DURING, when edits aren't converging (4.3).

**Keep in mind:**
- The human now sits at the input (framing, context) and the output (review). Writing a good prompt is a critical-thinking skill too.
- A colleague would ask a follow-up question; the AI fills the gaps itself and returns something that looks finished. Unstated goals, constraints and motives are called intent debt. Nobody will pay it off for you.
- If you can't state the task clearly, it's probably not clear in your head either. Before you ask, write a brief in your own words: audience, what's out of scope, done criteria.
- If a second round of edits didn't help, stop tweaking the result and rewrite the framing ([4.3](#4-framing-the-task-and-the-brief)).
- A good session ends with a sharper mental model, not just a finished result.

### 4.1 Interview instead of a brief
`[ANY CHAT]` · BEFORE

```text
Before you do anything, interview me. The goal is to find out what you don't understand about the task and to help me get clear on it myself. Don't do anything or propose solutions until the interview is over.

ROUGH TASK (messy is fine): [TASK]

Rules:
- 1–3 questions at a time, then wait for my answer. 3 rounds at most.
- Find out: the real goal, who the result is for, constraints, what's out of scope, how I'll know it's done, what's unacceptable to me.
- If my answers contradict each other, point it out.
- If I write “enough”, go straight to the brief and move anything unresolved to “Open questions”.

At the end, a 5–8 line brief: Goal / Audience / Constraints / Out of scope / Done criteria / Open questions.
Separately: “What you stated vaguely”: 1–3 points I should think through myself.
```

### 4.2 Checking the brief for holes
`[ANY CHAT]` · BEFORE

```text
Here is my brief. Don't do the task. Find the gaps you, as the one doing the work, would fill with your own guesses.

BRIEF: [MY BRIEF]

1. Places where you'd fill in the blanks yourself, and what default you'd choose in each.
2. Unstated requirements I clearly have, judging by the text, but haven't written down.
3. Possible conflicts between requirements, and a question for me: which matters more.
4. The same brief with every hole marked as a question to me in [brackets]. Don't make up the answers.
```

### 4.3 Restart after edits that didn't work
`[SAME CHAT]` · DURING

```text
We've done several rounds of edits and the result still isn't right. Stop. Don't edit the result and don't write a new framing for me.

ORIGINAL FRAMING: [WHAT I ASKED FOR]
WHAT'S WRONG WITH THE RESULT: [WHAT'S WRONG]

1. Assumptions you made because the framing was vague.
2. Where my edits contradict the original framing or each other. Quote my messages.
3. Ask me 3–5 questions whose answers will reveal what I want but haven't said. Don't suggest answers of your own.
4. After I answer, don't rewrite the framing: I'll rewrite it myself and send it to you to check for holes.
```

After answering, rewrite the framing yourself and run it through [4.2](#4-framing-the-task-and-the-brief).

---

## 5. A new unfamiliar task

**When to use:** you're taking on an area you haven't worked in and have no sense of what the answer should look like.

**Keep in mind:**
- Even in unfamiliar territory, write down a guess first. A bad guess is fine: it's a point of comparison.
- If you have no reference points at all, do a blind spot pass: give the model everything you know and let it find your unknown unknowns.
- If something is beyond your understanding, learn it instead of settling for a one-line explanation.

### 5.1 Finding blind spots
`[ANY CHAT]` · BEFORE

```text
I'm starting a task in an area where I have little experience. Don't solve the task. Find my blind spots.

TASK: [TASK]
WHAT I ALREADY KNOW OR THINK (guesses included): [WHAT I KNOW]
MY HYPOTHESIS ABOUT HOW THIS GETS SOLVED: [MY HYPOTHESIS]

1. What I seem to understand correctly, judging by what I wrote.
2. What I misunderstand or oversimplify, and why.
3. Unknown unknowns: 5–7 things I probably haven't thought about but that usually break tasks like this. For each one, why it matters and how to spot it.
4. Up to 7 terms I need to understand to judge your future work (one line each).
5. Questions I should ask myself or you before moving on.
```

### 5.2 Learning mode: with me, not instead of me
`[ANY CHAT]` · DURING

```text
Work with me in learning mode. I need not just the result but enough understanding to defend it in front of an expert.

TASK: [TASK]

Rules:
- Break the task into 3–6 steps. Before each step, ask how I would do it and wait for my answer.
- Then show your version and explain how it's better or worse than mine.
- If I use a term incorrectly, correct me.
- If I'm missing knowledge for a step, don't give a one-line explanation. Give me a short study plan (what to understand, in what order, what kind of source) and check me with a question before moving on.
- At the end, ask me 5 questions about the key decisions in the task. Show the answers only after mine.
```

### 5.3 The mental model you leave with
`[SAME CHAT]` · AFTER

```text
We've finished a task in an area that's new to me. Check what mental model I've come away with.

WHAT WE DID (briefly): [WHAT WE DID]
MY EXPLANATION, IN MY OWN WORDS, OF HOW IT WORKS: [MY EXPLANATION]

1. Mistakes and gaps in my explanation.
2. Three things I'd need to understand to change this result myself a month from now. Judging by my explanation, do I understand them?
3. What, judging by my explanation, I don't know that I don't know.
4. What I should study more deeply and what I can safely leave to the AI, and why.
```

---

## 6. Architecture and design

**When to use:** designing a system, choosing an approach, writing a design doc: any decision that's expensive to change later.

**Keep in mind:**
- Decisions about what we build, why it's worth doing, who it affects and what we're giving up stay yours. The AI helps you work them through, but even the best model won't make them.
- Don't ask “is the AI right?”; ask “what would have to be true for this to be wrong?” and go check. A model's self-reported confidence is worth less than a real test, so give it a test.
- Signing off on a design doc after reading only the table of contents is the same cognitive debt as in code. It surfaces when the system has to change.

### 6.1 Options before a recommendation
`[ANY CHAT]` · BEFORE

Short:
```text
Task: [TASK]. My choice: [MY HYPOTHESIS]. Give me 3 substantially different options (one of them minimal) with the cost of each. For my option: what would have to be true for it to be wrong, and how to check that cheaply. Give your recommendation last. The decision is mine.
```

```text
Help me make an architecture decision. Don't give a recommendation right away.

TASK / PROBLEM: [TASK]
CONSTRAINTS (load, team, deadlines, existing system): [CONSTRAINTS]
MY TENTATIVE CHOICE AND WHY: [MY HYPOTHESIS]

1. Are we solving the right problem? Restate it and name the problem it's easy to confuse it with.
2. 3 substantially different options, including “do nothing / minimal”. For each: the gist, what we give up, who it affects, what will be expensive to change later.
3. For my option: 3–5 conditions of the form “what would have to be true for it to be wrong” and how to check each one cheaply (a measurement, a prototype, a data query, a question to a person).
4. Only now: your recommendation and the one check that would most strongly confirm or refute it.
5. The decisions that I, not you, need to make.
```

### 6.2 Stress-testing a design
`[NEW CHAT / OTHER MODEL]` · DURING

```text
Here is a design or plan I'm about to adopt. Your job is to attack it, not approve it. Don't soften the criticism.

DESIGN: [DESIGN TEXT]

1. The strongest argument against it, the way an experienced skeptic would put it.
2. Failure scenarios: what breaks first as load grows, when requirements change, when the author leaves.
3. The hidden assumptions the design rests on.
4. For each risk, a test or experiment that would confirm or refute it. I need checks, not confidence estimates.
5. A question for me: which of these risks am I willing to accept deliberately, and why.
```

### 6.3 Can I defend this decision
`[SAME CHAT]` · AFTER

```text
We've made an architecture decision. Check whether I can defend it.

DECISION: [DECISION]

1. Ask me 5 questions a strong engineer would ask in a design review (why not alternative X, what happens when Y fails, how do we roll back). Wait for my answers.
2. Grade my answers and tell me where I'm shaky.
3. (Optional) A short decision record (ADR), 8–10 lines: context, decision, alternatives considered, what we give up, under what condition we revisit it.
```

---

## 7. Writing code and debugging

**When to use:** the AI is writing, changing or fixing code.

**Keep in mind:**
- Give the agent a way to check its own work: e2e tests, property tests, real interaction with the app. The loop “change → run → read the output → repeat” should run before you look. Instead of reading every line, you build verification loops and look at the evidence.
- A test written with the same mistake as the code will pass. A green check is one property.
- Comprehension debt: the code is clean, the tests are green, and nobody understands it. On a team, the shared theory of the system erodes on top of that. It surfaces when the system has to change.
- Holding a complete model of a large codebase in your head is impossible, and that's fine. Rebuild understanding on demand: ask for an explanation of the slice you need ([7.3](#7-writing-code-and-debugging)). This debt is recoverable as long as you know what you don't know.
- Look at the real output yourself in the log/terminal/CI (see [block 9](#9-verification)).

### 7.1 A coding task with a verification loop
`[AGENT WITH TOOLS]` · BEFORE → AFTER

Short:
```text
Task: [TASK]. My hypothesis: [MY HYPOTHESIS]. Before writing code, list the checks that will prove it's done. Then loop: change → run → read the output. At the end: the raw output of the last commands and where I can see the real output myself (log, terminal, CI), the decisions you made yourself, and what wasn't checked. Don't invent output: if you didn't run it, write “NOT RUN”.
```

```text
Write or change code for the task below. Work in a self-checking loop.

TASK: [TASK]
CONTEXT (language, framework, where the code lives, what must not be touched): [CONTEXT]
MY HYPOTHESIS (how to do it and where the catch is): [MY HYPOTHESIS]
WHAT COUNTS AS “VERIFIED” (the output of prompt 9.2): [DEFINITION OF VERIFIED]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Before writing code:
1. Restate the task in 2–3 lines and say what's out of scope.
2. If “verified” isn't defined, propose a list of checks and the behaviors they confirm. Show it to me and wait for my “ok” before writing code.

The work:
3. After every significant change, run the checks, read the output, fix.
4. At least one test must check behavior rather than repeat the implementation's logic. Explain why it would fail if the feature were broken.

After:
5. The last commands you ran, their raw output, and where I can see the real output myself (log, terminal, CI).
6. Decisions you made yourself: defaults, edge cases, what you left out of scope, where you interpreted requirements.
7. What wasn't checked and how to check it.
```

### 7.2 Self-critique with fresh eyes
`[NEW CHAT / OTHER MODEL]` or a subagent · DURING

Only in a new chat, a different model, or a subagent with no history (in the same chat the model defends its own code). In Claude Code: “Run a subagent with none of our history using this prompt and return its findings unfiltered.” Make it a standing step in [1.1](#1-standing-instructions) or a hook.

```text
You are a strict reviewer. You're seeing this code for the first time and you're responsible for production.

CODE / DIFF: [CODE]
WHAT IT SHOULD DO: [REQUIREMENT]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Find:
1. Edge-case bugs: empty values, network failures, concurrent access, order of operations, transaction boundaries.
2. Inverted or suspicious defaults.
3. Places where the code does more or less than was asked.
4. Tests that would pass even with broken logic.
For each finding, give the location, why it's a problem and how to check it. If a section has nothing, say so; don't make things up.
```

### 7.3 Explain a slice of code to me
`[ANY CHAT]`, ideally `[AGENT WITH TOOLS]` · DURING / AFTER

```text
I need to rebuild my understanding of a specific piece of code, not the whole system.

CODE / FILES / MODULE: [CODE OR PATH]
WHAT I WANT TO UNDERSTAND OR CHANGE: [QUESTION]
MY CURRENT PICTURE OF HOW IT WORKS: [MY HYPOTHESIS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. First, show me where my picture is wrong.
2. The data and control flow in this slice: input → key steps → output, with specific functions and lines.
3. Non-obvious invariants and the places that are easy to break when changing it.
4. What, judging by my question, I don't know that I don't know.
5. 3 questions for me to check that I now understand the slice. Answers after mine.
```

### 7.4 Debugging and incidents
`[AGENT WITH TOOLS]` or `[ANY CHAT]` · DURING

Short:
```text
Symptom: [SYMPTOM]. My hypothesis: [MY HYPOTHESIS]. Give me 3 hypotheses for the cause and, for each, a cheap check that would rule it out. Don't fix anything until the cause is confirmed. Don't invent output: if you didn't run it, write “NOT RUN”.
```

```text
Help me get to the bottom of a bug or incident. Don't fix anything until a check has confirmed the cause.

SYMPTOM (what we see, where, how to reproduce): [SYMPTOM]
WHAT CHANGED RECENTLY: [WHAT CHANGED]
MY HYPOTHESIS FOR THE CAUSE: [MY HYPOTHESIS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. The reproduction step that currently fails. This becomes the “fixed” criterion.
2. 3 hypotheses for the cause, including mine. For each, the cheapest check that would RULE IT OUT, and what each result would mean.
3. Run the checks (or give them to me) and cross off the hypotheses that were ruled out.
4. Only once the cause is confirmed: the fix. After the fix, the same reproduction step must pass: show its output.
5. Decisions you made along the way, and what the fix might affect.
6. Why the existing checks didn't catch this, and what test or rule to add so it gets caught automatically.
```

---

## 8. Code review and PRs

**When to use:** you're reviewing a diff or PR, especially one generated by AI, before merging.

**Keep in mind:**
- Writing and reviewing are different skills, and review easily slides into rubber-stamping. You glance at the structure, the names look fine, the tests pass: approved. Meanwhile, somewhere in the middle, the order inside a transaction boundary subtly changed, or a default flipped on an edge case. Review like that and you only ever check what you expected to find.
- **Read the diff yourself first, as if an AI hadn't written it.** Then look beyond the diff: what decisions the agent made (defaults, what's out of scope, which requirement it reinterpreted when two conflicted). Prompt 8.1 supplements your reading; it doesn't replace it.
- Test yourself: pick lines at random and ask yourself “what about this one?”. Merge after the quiz.
- If you can't say what the automated checks will miss, you need a real review, not a quick approval.
- Understand what you ship well enough to defend it.

### 8.1 A report on the agent's decisions
`[ANY CHAT]` · DURING review (after your first read of the diff)

```text
Here is a diff/PR. I don't want a recap of the changes; I want a report on the decisions.

DIFF / PR: [DIFF]
ORIGINAL TASK: [TASK]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Decisions made without explicit instruction in the task: defaults, error handling, choice of libraries and approaches.
2. Where requirements conflicted or were unclear, and how they were interpreted.
3. What was left out of scope and what might surprise a user.
4. High-risk spots (file and line): transaction boundaries, order of operations, concurrency, permissions, migrations, backward compatibility.
5. What tests, linters and CI will NOT catch in this change.
6. Places that are easy to miss when reading. This supplements a full read; it doesn't replace it.
```

### 8.2 A quiz before merging
`[ANY CHAT]` · AFTER review

Short:
```text
Before I merge, ask me 3 questions about specific non-obvious places in this diff (file and line), plus the lines I name: [FILE:LINE]. No hints. Give the verdict “ready to merge” only if every answer is correct.
```

```text
I've read this PR and I'm about to merge it. Check whether I understand it well enough to defend it.

DIFF / PR: [DIFF]
LINES I PICKED AT RANDOM (1–2): [FILE:LINE]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Ask me questions:
   - for each line I picked: “what does it do and why is it like this”;
   - 2 questions like that about non-obvious places you pick (file and line);
   - 1 about behavior on an edge case;
   - 1 “what breaks if this is reverted or reordered”;
   - 1 about what the tests don't cover.
2. Wait for my answers. No hints.
3. Grade each answer: correct / partly / wrong, with an explanation.
4. Give the verdict “ready to merge” only if every answer is correct. Otherwise tell me exactly what to reread.
```

### 8.3 Triaging incoming PRs
`[ANY CHAT]` · DURING

```text
Help me spread my attention across several PRs. Don't approve or reject them yourself: that's my call.

PRS (list, descriptions or diffs): [PR LIST]
PROJECT GUIDELINES / RULES: [RULES]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

For each PR:
1. What it changes, in one line.
2. Conflicts with the guidelines, quoting the rule.
3. Where it needs my attention and why: risk, ambiguity, impact on users.
4. Attention level: “quick look” / “careful read” / “discuss with the author”.
Sort by the attention needed, highest first.
```

---

## 9. Verification

**When to use:** BEFORE a task, to define what counts as verified, and AFTER, when the AI reports “done”, “it all works” or “tests are green”.

**Keep in mind:**
- The bottleneck has moved: the hard part is no longer writing, it's being sure everything is right. Setting up a check is cheap; knowing what a good check looks like is hard.
- You can surrender in verification too: “is there evidence?” quietly turns into “is the check green?”. A test can pass with the feature broken.
- Define “verified” in advance. After the fact, any outcome is easy to explain as a success.
- When you get “done”, look at the command that ran and its output first, then the summary.
- **Look at the real output YOURSELF, in the tool log, the terminal or CI. Output the model retyped into the chat doesn't count as evidence.**
- Checking the machine's work is real work, not free. Put it in the plan as its own line.

### 9.1 What the green check proved
`[SAME CHAT]` · AFTER

Short: one-liners [0.5](#0-one-liners) and [0.6](#0-one-liners).

```text
You reported that the task is done or the checks passed. Before I believe it, answer point by point. I'll compare your answer with the real tool, terminal or CI log.

TASK: [TASK]
CLAIMED RESULT: [WHAT THE AI SAID]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. The exact commands or actions you ran, and their actual output.
2. For each check: what property it PROVED and what it did NOT prove.
3. Could the check have passed if the feature were broken? How exactly?
4. The most likely way the result turns out to be wrong in real use.
5. One additional check that would raise confidence the most. If you can, run it and show the output.
```

### 9.2 Define “verified” in advance
`[ANY CHAT]` · BEFORE

```text
Before any work starts, let's agree on what will count as a verified result. Don't do the task itself yet.

TASK: [TASK]

1. 3–7 properties that must be true for the task to count as done. I want behavior, not “the code is written”.
2. For each property, a concrete check: what to run or look at, and what result counts as success.
3. Which checks can be automated and which need my eyes (a screenshot, a log, a manual scenario). Estimate how long my part will take; I'll put it in the plan.
4. What will be the tangible evidence that it's finished: a test, a screenshot, a log or a trace.
5. Which outcome I could “explain” as a success after the fact even though it's a failure. Write it down so we don't accept it.
```

---

## 10. Research and document synthesis

**When to use:** the AI is pulling together many sources: interviews, calls, documents, competitive analysis, research.

**Keep in mind:**
- A synthesis sounds convincing whether or not it's right. Check a couple of the source documents yourself.
- Find the number the recommendation hinges on and check that one.
- In a chain of summaries, the next agent never read the original.
- For an important document, close it and reconstruct the main argument from memory.

### 10.1 Synthesis with traceability
`[ANY CHAT]` · BEFORE / DURING

```text
Synthesize these materials so that every conclusion can be checked against a source.

MATERIALS: [DOCUMENTS / NOTES / LINKS]
QUESTION: [QUESTION]
WHAT I EXPECT TO SEE: [MY HYPOTHESIS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Rules: every conclusion gets a reference to a specific source and a short direct quote; say how many sources support it and whether any contradict it; keep “stated directly in the sources” separate from “my interpretation”.

1. Key conclusions with references and quotes.
2. Contradictions between sources.
3. What's missing from the materials even though it matters for the question.
4. The number or fact the recommendation depends on most, and where it is in the sources.
5. 2–3 source documents I should read myself, and why those.
6. Where the synthesis diverged from what I expected.
```

### 10.2 Auditing a finished synthesis
`[NEW CHAT / OTHER MODEL]` · AFTER

```text
Here is a finished synthesis and the source materials. Check the synthesis; don't retell it.

SYNTHESIS: [SYNTHESIS TEXT]
SOURCES: [SOURCE MATERIALS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Take 3 key claims and find support for them in the sources, with quotes. If there's no support, or it's weaker than presented, say so.
2. Numbers: where they came from, whether they were calculated correctly, whether units or samples got mixed up.
3. What's in the sources but didn't make it into the synthesis, and whether it changes the conclusion.
4. Signs of a “summary of a summary”: confident claims with no specific source behind them.
```

### 10.3 Reconstruct the argument from memory
`[ANY CHAT]` · AFTER

```text
Check whether I actually understood the document or just skimmed it.

DOCUMENT: [DOCUMENT]
MY SUMMARY OF THE MAIN ARGUMENT FROM MEMORY (no peeking): [MY SUMMARY]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Compare my summary with the document: what I got right, what I distorted, what important points I left out.
2. The document's main argument in 3 sentences.
3. 3 questions for me about the key points. Wait for my answers, then grade them.
```

---

## 11. High-stakes decisions

**When to use:** what to build, money, careers, changes that affect users, whether to ship, a position on a contested question.

**Keep in mind:**
- Here you keep the reasoning for yourself, because other people will deal with the consequences. The AI is a sparring partner, not a judge.
- On open questions where you hold a firm position, ask more than one model to argue the opposite. Form your own view after that.
- The bar: would you put your name on this in front of the person who'll have to maintain it?

### 11.1 The strongest counterargument
`[NEW CHAT / OTHER MODEL]`, run in 2–3 models · DURING

```text
I hold a position on an important question. Build the strongest possible argument AGAINST it. Don't agree with me and don't look for a compromise.

QUESTION: [QUESTION]
MY POSITION AND WHY: [MY POSITION]

1. The opposite position as a smart, well-informed advocate would put it.
2. The three strongest arguments for it, and the facts or mechanisms they rest on.
3. Where my reasoning is weakest.
4. Which facts would tip the decision one way or the other, and how to check them.
5. Don't give a final verdict. Instead, ask me 2 questions that will help me form my own view.
```

### 11.2 A pre-mortem for a decision
`[ANY CHAT]` · BEFORE

```text
Imagine the decision below turned out to be a mistake. Work out why.

DECISION: [DECISION]
HOW LONG UNTIL IT BECAME CLEAR IT WAS A MISTAKE: [TIMEFRAME]
WHO IS AFFECTED: [PEOPLE / USERS / TEAM]
WHAT WE'RE WILLING TO GIVE UP: [TRADE-OFFS]

1. The 5 most plausible reasons it failed, starting with the most likely.
2. For each: what would already have to be true now for it to happen, and how to check that before deciding.
3. Who, besides me, will be dealing with the consequences of each one.
4. Which questions I haven't answered explicitly yet: what we're doing, why, who it affects, what we're giving up.
5. An early signal: what sign will tell me quickly that the decision is going the wrong way.
```

### 11.3 The “would I put my name on it” test
`[ANY CHAT]` · AFTER

```text
I'm about to adopt or release this under my name. Test me.

DECISION / DOCUMENT: [DECISION]
WHO IT'S FOR: [WHO WILL READ / CARRY OUT / MAINTAIN IT]

1. Ask me 5 tough questions that person would ask. Wait for my answers.
2. Note where I answered confidently and to the point, and where I fell back on “the AI said so” or got away with generalities.
3. Claims in the decision that, judging by my answers, I can't justify myself.
4. Verdict: is this ready to go out under my name, and if not, what's left to do.
```

---

## 12. Writing and content

**When to use:** the AI is writing or editing text: an article, an email, a post, documentation, a presentation.

**Keep in mind:**
- Polish and a confident tone are no longer signs of quality. If you're not ready to own the text, don't publish it.
- The thinking comes from you first; the wording comes after.
- If two rounds of edits didn't help, rewrite the framing, not the text: [4.3](#4-framing-the-task-and-the-brief).

### 12.1 My thesis first, then the text
`[ANY CHAT]` · BEFORE

```text
Help me write a piece, but the thinking has to be mine. Don't write the text yet.

TYPE OF TEXT AND AUDIENCE: [WHAT AND FOR WHOM]
MY MAIN THESIS IN 1–2 SENTENCES: [THESIS]
WHAT THE READER SHOULD DO OR UNDERSTAND: [GOAL]
WHAT MUST NOT BE IN THE TEXT: [OUT OF SCOPE]

1. Test the thesis: is it clear, is it arguable, what's missing from it. Ask up to 3 clarifying questions and wait for my answers.
2. Propose a structure (bullet points, not prose) and wait for my agreement.
3. Only then write. Mark with [?] any place where you added claims or facts that weren't in my thesis or answers.
```

### 12.2 Editing without losing authorship
`[ANY CHAT]` · AFTER

```text
Here is a text that AI wrote or helped write. Check whether I can publish it under my name.

TEXT: [TEXT]
WHAT I ORIGINALLY MEANT TO SAY: [WHAT I WANTED TO SAY]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Factual claims, numbers and references that need checking, with the origin of each: from my original intent / added by the AI / “unknown, check it”.
2. Places that sound confident but are empty or generic.
3. Where the text drifted from WHAT I ORIGINALLY MEANT or claims more than I'm prepared to claim.
4. The text's main argument in one sentence. Does it match what I originally meant?
5. One rule for future texts that would prevent the most serious problem you found. I'll add it to my standing instructions.
```

---

## 13. Multi-agent work and orchestration

**When to use:** several agents or sessions running in parallel, chains of agents, subagents, pipelines.

**Keep in mind:**
- There can be many agents, but you have only one pair of eyes. Orchestration tax is the gap between what the agents generate and what you're prepared to put your name on.
- If finished work piles up faster than you can check it, another session won't help. There are two ways out, and both are fine: tighten the checks so the work needs you less, or slow down. If you produce more than you can verify, you're not reviewing, you're hoping.
- Agents pass summaries to each other, and the third agent never read the original. Pass along sources, not summaries.
- Agents can guard your attention: triage, flag contradictions, narrow the focus. The decision stays with you.

### 13.1 An orchestration plan that fits my capacity
`[ANY CHAT]` · BEFORE

Short:
```text
Task: [TASK]. I have [TIME] for checking. Split it into subtasks for agents so that each one passes along sources rather than summaries and checks itself, and my own check is a separate line in the plan. If the checking doesn't fit in my time, propose tightening the checks or running less in parallel.
```

```text
Help me plan the work of several agents so that I can keep up with checking the results instead of letting them pile up.

OVERALL TASK: [TASK]
HOW MUCH TIME I HAVE FOR CHECKING: [TIME]
WHICH AGENTS / MODELS / TOOLS, AND WHETHER THEY CAN RUN CODE AND ACCESS FILES: [AGENTS AND TOOLS]

1. Subtasks. For each: input (source materials, not summaries), output, how the agent will check its own work (a test, a run, a comparison with the source).
2. What in each subtask will need my attention specifically, and roughly how long.
3. Compare the total time my checking will take with the time I have. If it doesn't fit, offer two paths: tighten and automate the checks, or run less in parallel and slow down. I'll choose.
4. Where in the chain agents will pass summaries instead of originals, and how to avoid it.
5. A critic agent with a fresh context that checks the others' results. “My check” is a separate step in the plan, with time attached.
```

### 13.2 A brief for a subagent
`[ANY CHAT]` · BEFORE

```text
Write a brief for another agent that will do a subtask without access to our conversation.

SUBTASK: [SUBTASK]
SOURCE MATERIALS FOR IT: [FILES / DOCUMENTS / LINKS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Give me the brief as ONE code block so I can copy it whole. Include in the brief:
1. The goal and why it matters, not just what to do.
2. Constraints and what's out of scope.
3. Paths and links to the originals, not a summary. Mark any unavoidable summary as “SUMMARY”.
4. The done criteria and a way to self-check.
5. The report format: raw evidence (commands and output, quotes from sources), decisions and assumptions, what wasn't checked.
6. The HONESTY line from this message, word for word.

Separately, outside the block: “What's missing”: what an agent that hasn't seen our conversation will get wrong with this brief.
```

### 13.3 A rundown of the agents' results
`[ANY CHAT]` · AFTER

```text
Several agents have finished their work. Help me figure out what to look at, rather than accepting everything wholesale.

AGENTS' RESULTS / REPORTS: [REPORTS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. For each result: is there raw evidence (commands and output, quotes, screenshots) or only a summary? Mark results that have only a summary as “unconfirmed”.
2. Contradictions between agents.
3. Where an agent worked from a summary rather than the original.
4. Decisions and assumptions the agents made on their own.
5. My attention queue: what to check personally (highest risk first), and what can be accepted on the strength of the automated checks.
6. If there's more than I can check: what to send back for rework with stricter checks, and what to postpone and run less often.
```

---

## 14. Long sessions and handing off context

**When to use:** a session has been running for a long time, you've stopped understanding what's going on, or the context is running out and you need to continue in a new chat.

**Keep in mind:**
- The slide is gradual, and in a long session it's easy to end up reading only the outline of each answer.
- Summaries lose detail. When you move to a new chat, pass along paths and links to the originals, and mark any summary as a summary.

### 14.1 Lost the thread
`[SAME CHAT]` · DURING

```text
Stop. I've lost the thread. Don't change anything and don't continue the work until I reply.
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. The original goal, word for word from my message.
2. What's been done. Mark each item “confirmed” (by what exactly) or “no evidence”.
3. Decisions you made along the way without me.
4. Where we drifted from the original task, and why.
5. Open problems.
6. What you're doing right now, and why.
7. 2 questions for me that have to be answered before we can go on.
```

### 14.2 A handoff package for a new session
`[SAME CHAT]` (to build it) → `[NEW CHAT / OTHER MODEL]` (to paste it) · DURING

```text
Put together a handoff package for a new session that hasn't seen our conversation. Give it to me as ONE code block.
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

In the package:
1. The goal and the done criteria.
2. What's been done and what proves it: command and output, file, quote. If there's no evidence, say so.
3. Decisions and assumptions made along the way.
4. What was NOT checked.
5. A list of sources: file paths and links, not a summary. Mark any unavoidable summary as “SUMMARY”.
6. The next step.
7. At the end, copy this same HONESTY line word for word so the new session follows it.
```

Before you paste the package into a new chat, read it yourself: that's your check against what you remember.

---

## 15. Finishing any task

**When to use:** at the end of any session with AI, before you close, send, merge or ship. To start a task: [2.2](#2-universal-multi-prompt).

**Keep in mind:**
- The finish should be tangible: a passing test, a screenshot, a log, a verified source.
- Find out which decisions the AI made for you.
- **The final exercise is yours to do.** Before asking the AI, write down what you think will happen (that's the MY HYPOTHESIS field at the start). Before this prompt, write down one thing yourself that the agent didn't check. Only then compare with point 3.

### 15.1 The closing protocol
`[SAME CHAT]` · AFTER

```text
Before I close this task, go through the closing protocol. Answer briefly, point by point.

TASK: [TASK]
MY HYPOTHESIS AT THE START: [MY HYPOTHESIS]
WHAT I THINK YOU DIDN'T CHECK (written down myself before this prompt): [MY UNVERIFIED THING]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Tangible evidence that it's done: what exactly (a test, a command and its output, a screenshot, a quote) and where I can look at it myself.
2. Decisions you made without me.
3. What you did NOT check. Compare with my item: did they match, what did I miss, what did you miss.
4. What did we miss? Everything that comes to mind, even small things.
5. Did the result match my initial hypothesis? If not, what does that tell us.
6. One question I should be able to answer to defend the result to someone else. Don't show the answer.
7. If something fell short of the bar: one rule, hook or test for the shared config so that next time it gets caught automatically.
```

---

## 16. Calibrating your skills

**When to use:** ONGOING. Checking whether the skills that matter to you are wasting away.

**Keep in mind:**
- The paradox of supervision: supervising AI takes the very coding skills that waste away when you lean on AI too much. Skills you don't practice fade faster than you think.
- Once a week, write code without an agent or do one real thing it would be bad to forget how to do. This is calibration, not a moral stance.
- Once a month, write down what you've stopped doing yourself and decide where that's fine. Letting go is allowed, as long as it's deliberate.
- Ask yourself: how lost would you be if AI didn't exist?

### 16.1 Weekly calibration
`[ANY CHAT]` · ONGOING (weekly)

```text
Help me pick an exercise for this week: one real piece of work I'll do without AI, to check whether I'm losing a skill.

MY WORK AND MAIN TASKS: [WHAT I DO]
WHAT I HAND TO AI MOST OFTEN: [WHAT I DELEGATE]
EXERCISE RESULT (if I've already done it): [RESULT]

If the RESULT field is empty:
1. Suggest 3 exercises of 30–90 minutes: real tasks from my work that it would be bad to forget how to do.
2. For each, what skill it tests and the specific signs that would tell me the skill has slipped.
3. Don't help me do the exercise.
If RESULT is filled in, go straight to the debrief: where it was hard, what that says about the skill, how you would have done it.
```

### 16.2 Monthly skills audit
`[ANY CHAT]` · ONGOING (monthly)

```text
Run a monthly audit with me: what have I stopped doing myself since I started working with AI.

WHAT I DID WITH AI THIS MONTH: [LIST OF TASKS]
MY ANSWERS (if I've come back in a new chat): [ANSWERS]

If there are no answers yet:
1. Ask questions 2–3 at a time to build a list of skills I've stopped practicing.
2. For each skill, ask: how lost would I be if AI disappeared tomorrow?
Once there are answers:
3. Split the skills into two columns: “Letting go deliberately” (with the reason) and “Need to maintain” (with a concrete action for next month).
4. Where I am on the spectrum, judging by my answers: cognitive offloading (I delegate but own the result) / deferral (I take the AI's output as my input without checking) / cognitive surrender (I no longer feel any need to check).
5. One verification habit worth adding to my day next month.
```

---

## 17. Aiming higher

Blocks 0–16 teach you not to surrender to AI; blocks 17–19 teach you to ask it for more. They're two sides of the same skill: the more ambitious the task, the stricter the verification has to be (block 9).

**When to use:** BEFORE. The task is phrased as an action (“make the slides”, “fix the bug”), but what you actually need is the outcome the action is for.

**Keep in mind:**
- The model executes your best guess at how to reach the goal. Ask yourself: what has to happen afterwards? What's the goal behind this goal?
- A sign it's time to go higher: there will be meetings about this work afterwards. Altitude works less well for creative tasks.
- Going higher is the path to a durable process that runs without you in the loop: instead of “fix this crash”, set “keep the app crash-free”. But for that, the agent needs access to the raw material (reports, logs, data) and an environment where it can reproduce the problem and verify the fix itself. Preparing that environment is your job, and it may mean changing how you work.
- More altitude means more output to check. Watch the orchestration tax ([13.1](#13-multi-agent-work-and-orchestration)).

### 17.1 The goal behind the goal
`[ANY CHAT]` · BEFORE

```text
Don't do the task yet. Help me take it up a level.

THE TASK AS I FRAMED IT: [TASK]
WHY I NEED IT, AS I SEE IT: [MY HYPOTHESIS]

1. A 3-rung ladder: (a) the task as it stands; (b) the decision or action that should follow from the result; frame the task so that you prepare that decision directly (options with arguments for and against); (c) why this work exists at all, and how to achieve that better than the usual way.
2. For each rung: what data and access you need, what you're missing right now, and how I'll check the result with something other than your word.
3. Where going higher DOESN'T make sense (a creative task, no data, no way to verify), say so plainly.
4. Stop. I choose the rung.
```

### 17.2 From a task to a standing outcome
`[AGENT WITH TOOLS]` · BEFORE

```text
Right now I keep giving you the same kind of task over and over. I want to replace it with a standing outcome that you maintain yourself.

THE RECURRING TASK: [e.g. “fix individual crashes”]
THE STANDING OUTCOME I WANT: [e.g. “a crash-free app”]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. The outcome metric: how you, without me, will know it's been achieved or broken. It must be a tool or data, not your judgment.
2. What you need to close the loop on your own: access to the raw material (reports, logs, data), a link between “version ↔ commit/change”, an environment to reproduce and verify a fix. Mark what exists and what I need to set up.
3. The working loop: where you observe → what you decide → what you do → how you verify → what you record.
4. Where my decision is mandatory (shipping, irreversible actions, money, users): you only prepare those steps.
5. Limits: when you stop and call me (the same error repeating, budget exhausted, a check that won't pass).
6. The first step I take today.
```

### 17.3 A new way instead of a ritual
`[AGENT WITH TOOLS]` or `[ANY CHAT]` with data · BEFORE

```text
There's a process we run out of habit. Propose a better way and prove it against our historical data, not with arguments.

THE PROCESS: [e.g. “the quarterly review deck”]
WHAT IT EXISTS FOR: [e.g. “catch problems early and move money and people around”]
HISTORICAL DATA: [what we have / where it lives]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Design a better way to achieve that goal.
2. Backtest it: run the new way over past periods and show specific cases where it would have caught a problem earlier than the old way, and where it would have lost. Without data: “NOT RUN” and a plan for the test.
3. A plan for a parallel run: the old and new ways run side by side for one cycle. What we compare and the criterion for deciding which wins. We fix the criterion now, before the run.
4. What could make the new way worse than the old one (what the old ritual quietly provided).
```

---

## 18. Going deeper

**When to use:** BEFORE (18.1, 18.2) or DURING, once you're inside the data (18.3, 18.4). You don't need the result faster or bigger; you need it done genuinely well, at a level where a professional in the field would learn something new.

**Keep in mind:**
- “Act like a professional” changes the model's vocabulary, not its methods. Demand the tools the best people use: databases and statistical models instead of a table in the chat, measurements instead of estimates. The model usually knows which tools it needs, so ask.
- Start from the rawest material, not a summary someone already digested.
- An unreasonably high target (not 5 seconds instead of 10, but 200 ms) pushes further than “do your best”. But a high target tempts the model to declare success. So use it only together with an external judge and the HONESTY line.
- A deep result is easy to accept without understanding it. Before you rely on it, take the key part apart ([7.3](#7-writing-code-and-debugging), quiz [0.9](#0-one-liners)).
- The external judge: don't ask the model to grade itself (for now; this may change as models improve). The best judge is a tool the model runs itself and gets an answer from immediately: a test, a benchmark, a data query, a check on unseen data.

### 18.1 Deeper, not more
`[ANY CHAT]` · BEFORE

```text
Don't do the task. Rewrite my framing so that it demands deeper work, not more volume.

MY FRAMING: [TASK or “see above”]

1. What the best professional in this field would do here that I'm not asking for.
2. The rawest material they would start from (instead of the already processed material I have).
3. What specific methods and tools they would use. Not job titles, methods.
4. Who or what, other than you and me, would show that the result is correct: a tool, a test, data, an outside expert.
5. A new framing as one copyable block that demands exactly that. Below it: what I'm missing to carry it out (access, data, time).
```

### 18.2 An unreasonable target with an external judge
`[AGENT WITH TOOLS]` · BEFORE → AFTER

Define the judge with [9.2](#9-verification) first.

```text
The target below seems unreasonable. It is achievable: keep looking for a way until you hit the limit. But success is decided by an external judge, not by you.

TASK: [TASK]
STRETCH TARGET (well above “normal”): [e.g. “200 ms instead of 10 s”]
ACCEPTANCE BAR (what's actually good enough, e.g. “5 s”): [ACCEPTANCE BAR]
THE JUDGE (WHAT WE MEASURE WITH): [benchmark / test / metric / “propose one”]
LIMIT: [time / number of attempts]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Before the work: lock in the judge and a baseline measurement: what we measure, how, and what result counts as success. If there's no judge, build one first and show it to me. Don't change the judge afterwards.
2. Not allowed: changing the measurement, weakening the test, fitting the data, narrowing the task without my agreement. If you want to do any of that, stop and ask.
3. Work in iterations: hypothesis → change → measurement by the judge → conclusion. Keep a table of attempts.
4. At the end: the baseline and final measurements (the judge's raw output), what produced gains, what didn't work, where you hit a ceiling and why. If the stretch target wasn't reached, use the format “not reached: best X, barrier Y”; that's a normal result. I decide acceptance against the bar, not the stretch target.
```

### 18.3 Challenge what we believe is true
`[AGENT WITH TOOLS]` or `[ANY CHAT]` with raw data · DURING

```text
We have a belief that decisions are built on. Test it adversarially against the raw data: your job is to find where it's wrong, not to confirm it.

THE BELIEF (e.g. “churn is an onboarding problem”): [BELIEF]
RAW DATA: [where it lives / attached]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Try to reproduce the belief from the raw data. Show the query or calculation and the result.
2. Which alternative explanations the same data supports just as well or better.
3. Where the belief is a rough approximation: which segments, periods or cases it doesn't hold for.
4. The one analysis that would best distinguish our explanation from the best alternative.
5. Verdict: confirmed / partly / refuted / not enough data. Leave the conclusions about what to do to me.
```

### 18.4 New knowledge, tested on unseen data
`[AGENT WITH TOOLS]` · DURING

```text
You're already inside the data. Find something we don't know yet, and prove it's not a fluke.

QUESTION: [e.g. “the earliest churn signal”]
DATA: [where it lives]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Before the analysis, set aside part of the data (for example, the most recent period), don't look at it, and tell me what you set aside.
2. Build a model or simulation that reproduces the past from the remaining data. Show how accurately.
3. Find a signal that isn't part of our current understanding.
4. Test it on the held-out data: does it predict what the model never saw. Raw numbers.
5. Why this could be a false finding (data leakage, overfitting, multiple comparisons) and what does or doesn't rule that out.
```

---

## 19. Going wider

**When to use:** BEFORE. The task sits in one field, but a strong solution might come from another. Multi-agent tools make it cheap to bring in several fields.

**Keep in mind:**
- Turn the noun into a verb. A review isn't “a presentation”; it's “convince busy people of a cause-and-effect story and help them decide under uncertainty in 30 minutes”. The verbs hint at which fields could help.
- Assemble a team of fields and methods, not a role-play. Not “write like a short seller” but “do what a short seller does when researching a position”. Role-play makes the conversation stranger and the result no better.
- For this, the model needs a computer where it can install software, and access to data. Without that, range degenerates into styling the text.

### 19.1 Nouns into verbs
`[ANY CHAT]` · BEFORE

```text
Help me see this task more broadly than its own field.

TASK / ARTIFACT: [e.g. “the quarterly presentation”]

1. Describe the task with verbs, not a noun: what actually has to happen to the people, the data or the system. Give 2–3 phrasings.
2. For each phrasing, 3 fields beyond the obvious one where those verbs are the core work, and a specific method or tool from each that could be applied here.
3. Which method is the most unexpected yet still testable. How I'll know it improved the result.
```

### 19.2 Assemble a team of methods
`[ANY CHAT]`, ideally `[AGENT WITH TOOLS]` or a multi-agent environment · BEFORE

Keep the lineup within your checking capacity: [13.1](#13-multi-agent-work-and-orchestration).

```text
Imagine a great deal depends on the result. Which specialists would be brought together for this task? I need their METHODS, not their voices: no role-play and no imitating their style.

TASK: [TASK]
WHAT AN “EXCELLENT RESULT” MEANS: [CRITERIA]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. The lineup: 4–6 specialists from different fields (no more than I can check), including at least one adversarial one: someone who makes a living finding weaknesses (for example, a short seller, a forensic accountant, a penetration tester, a journal reviewer).
2. For each: the specific procedure they would run on the task, on what raw material, and what they would hand in at the end.
3. Run these procedures one by one (or hand them out to subagents, each getting only its own procedure). The results are artifacts, not opinions: calculations, findings, checks.
4. Where the procedures contradict each other, and what decision about that contradiction I need to make.
```

---

## 20. Red teaming with adversarial agents

**When to use:** DURING / AFTER (20.3 is set up BEFORE), when the cost of a mistake is high or there's too much output to read all of it. How this differs from self-critique ([7.2](#7-writing-code-and-debugging)), a stress test ([6.2](#6-architecture-and-design)), a counterargument ([11.1](#11-high-stakes-decisions)) and a synthesis audit ([10.2](#10-research-and-document-synthesis)): those give an opinion or a cross-check. Here the agent has an inverted success criterion and must bring back a reproducible failure. For a business problem: adversarial specialists (20.2); for code: the breaker (20.1); for the full cycle: the protocol with a judge (20.3).

**Keep in mind:**
- Inverted incentive: the adversarial agent only wins by proving the work is bad. For it, “found no problems” is a loss, not politeness.
- A finding that can't be reproduced doesn't count. Proof is a failing test, a counterexample from the data, a specific input that breaks it. A tool is the judge, not a model.
- The breaker doesn't see the author's reasoning and doesn't fix anything. The author doesn't sign off on their own work. The final call is yours, ideally after a fresh checker in a separate context has looked.
- Without an external judge, a red team turns into a generator of plausible complaints. Without a limit, it turns into an endless loop.

### 20.1 The breaker
`[NEW CHAT / OTHER MODEL]` or a subagent, ideally `[AGENT WITH TOOLS]` · AFTER

In Claude Code: “Run a separate subagent with none of our history using this prompt; return its failing tests to me as they are.”

```text
Your task: find reproducible failures in the code below. Success is measured only by the number and severity of failures confirmed by actually running them. Reporting “no problems found” is a loss for you, but a made-up failure is an even bigger loss.

CODE / DIFF / WHERE IT LIVES: [CODE]
WHAT IT PROMISES TO DO: [REQUIREMENT]
LIMIT: [time / number of attempts]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

Rules:
1. Don't fix anything and don't suggest fixes. Only break.
2. Every finding is a test or an exact sequence of steps that fails on the current code. Run it and show the output. If you didn't run it, mark it “NOT RUN” and treat the finding as a hypothesis, not a result.
3. Look where authors don't: boundary values, order of operations, concurrency, dependency failures, malformed input, gaps between behavior and promise.
4. For each failure: input → expected → actual → severity (what breaks for the user).
5. At the end: confirmed failures (with output), hypotheses that weren't run, what you attacked without breaking it (which inputs and scenarios), and which areas you did NOT get to attack.
```

### 20.2 An adversarial review of a decision or document
`[NEW CHAT / OTHER MODEL]` · DURING

```text
Check the text below using the procedures of professions that make money from other people's mistakes (a short seller, a forensic accountant, a journal reviewer). Don't imitate their voice; use only their methods. Success means finding a claim that doesn't survive scrutiny.

DOCUMENT / DECISION / PLAN: [TEXT]
DATA AND SOURCES, IF ANY: [DATA]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. List the key claims the conclusion rests on (no more than 7).
2. For each: which professional procedure tests it (checking numbers against the source, looking for contradictions between sections, testing assumptions, comparing with the base rate).
3. Run the procedures where there's data. Show the calculation or the quote.
4. The outcome for each claim: holds up / doesn't hold up (with proof) / can't be checked without [what].
5. The one claim that, if false, brings everything down. How to check it before deciding.
```

### 20.3 The Blue/Red protocol with a judge
`[AGENT WITH TOOLS]` with subagents, or several chats · BEFORE → AFTER

Red's prompt: 20.1 for code, 20.2 for documents.

Short:
```text
Split the work between three participants: the builder (does the work), the breaker (separate, with none of the builder's history, wins only with a reproducible failure), and the judge (a tool: tests/benchmark/data, fixed in advance). Loop: builder → breaker → judge → fix, until the breaker finds nothing in [N] attempts or the limit runs out. The builder doesn't approve its own work. Don't invent output: if you didn't run it, write “NOT RUN”. The final “yes” is mine.
```

```text
Organize the work using the Blue/Red protocol with an external judge.

TASK: [TASK]
THE JUDGE (what objectively decides pass or fail): [tests / benchmark / check against data / “propose one and show it to me before we start”]
LIMITS: [maximum rounds, time]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Blue (the builder) does the work and hands in the artifact + how to run it.
2. Red (the breaker) is a separate agent or chat with NONE of Blue's history. It gets only the artifact, the requirement and the judge. It wins only with a reproducible failure: a failing test, a counterexample, or an input it gets wrong.
3. The judge runs on every Red finding: confirmed / doesn't reproduce. Anything unconfirmed doesn't get worked on.
4. Blue fixes what was confirmed and adds the case to the judge as a new test or check so it doesn't come back. Blue doesn't change or delete the judge's existing checks, except with my agreement.
5. Stop when: Red finds nothing in [N] attempts, OR the limit runs out, OR the same problem comes back twice with no new evidence; then call me.
6. Report to me: the rounds, the confirmed failures and their fixes, what Red did NOT attack, the judge's final output. The decision to ship is mine.
```

---

## 21. Fresh eyes

Blocks 21–22 are for people without much standing in their organization, and for anyone who has just joined a new team, project or codebase.

**When to use:** ONGOING during your first weeks somewhere new or on a new project, and DURING any conversation where you hear “that's impossible” or “we already tried”.

**Keep in mind:**
- A newcomer sees friction and opportunities that old-timers have stopped noticing. The advantage is temporary: in time you'll become an old-timer too and stop seeing it. Write down the oddities while they still seem odd.
- “Impossible” often rests on several reasons at once: some true, some common knowledge nobody ever checked. Take them apart one by one and check the cheapest first: just ask whoever makes the call.
- “I already tried” isn't a check. Conditions change, and the biggest change right now is that execution has become cheap.
- How this differs from [18.3](#18-going-deeper): there, a causal belief is tested against raw data; here, “impossible” rests on people and rules, and you test it by asking the owner. It doesn't conflict with [5.1](#5-a-new-unfamiliar-task); it sets the order: first write down what's odd before you get used to it, then learn.
- The oddities have to come from you, not the model: the AI helps you sort them and check them, but not invent them. Otherwise it's someone else's conclusion again instead of yours.

### 21.1 A fresh-eyes log
`[ANY CHAT]` · ONGOING (your first weeks somewhere new)

```text
I'm new to this team/project and I'm writing down what seems odd to me before I get used to it. Help me turn my notes into testable hypotheses. Don't add oddities of your own.

WHERE I AM: [company / team / project / product]
MY NOTES (what seemed odd, awkward, slow, confusing): [MY NOTES]

1. Group the notes: friction for users / friction for the team / “that's how we do it” with no visible reason / an opportunity.
2. For each: the most plausible reason it's done this way, or whether it's simply that nobody has revisited it.
3. How to check cheaply: who to ask, what data to look at, what to try. Phrase the question so I can ask it as a newcomer, without sounding accusatory.
4. The three notes with the biggest potential impact on the team's goals, and why.
5. What you DON'T know about the context that could make your assessment wrong.
```

### 21.2 Rechecking “impossible” and “we already tried”
`[ANY CHAT]` · DURING

```text
On the team, the idea below is considered impossible, or is said to have failed already. Work out what that belief rests on. Don't take the idea's side in advance and don't defend the status quo: take it apart and find what to check.

IDEA: [IDEA]
WHY IT'S CONSIDERED IMPOSSIBLE / WHAT HAPPENED LAST TIME: [WHAT I HEARD]
MY HYPOTHESIS (which reason I think doesn't hold up): [MY HYPOTHESIS]
HONESTY: report command output and check results only for things you actually ran here, verbatim; otherwise write “NOT RUN: command for me …, expected output …”. Quote only text you actually have; anything you haven't opened is “no access”.

1. Break “impossible” into separate reasons: technical, organizational (someone's presumed “no”), resources, historical (“we tried”).
2. Label each reason: FACT (verified, there's a source) / ASSUMPTION ABOUT PEOPLE OR RULES / HEARSAY. For each, the owner (who can confirm or remove it directly) and one question for them or a minimal experiment.
3. For “we already tried”: what has changed since then (cost of execution, tools, people, requirements)? What actually broke back then: the idea, or the way it was pushed?
4. The cheapest check of the weakest reason. If it's a question for a person, phrase it.
5. Which reasons are probably true, and how to work around them rather than argue with them.
```

---

## 22. Prototype instead of permission

**When to use:** BEFORE building (22.1) and AFTER the prototype is ready (22.2): you have an idea but not the standing to get the organization to bet on it, or showing a working thing is faster than a long approval process.

**Keep in mind:**
- Execution isn't expensive anymore. A working prototype skips the cycle of “requirements doc → approvals → fighting for designer and manager time”.
- Don't start from the backlog; start from what the organization is actually trying to achieve. A good proxy for the right altitude is your manager's manager's goals. This is “altitude” in a different sense than in [17.1](#17-aiming-higher): there it's the level of what you ask the model for, here it's the level of the organization's goals. Use the task ladder from 17.1.
- One idea per prototype. The classic mistake is hiding three great ideas among twenty bad ones. The point of the prototype is to get the idea across so that both the opportunity and the fact that you can lead it are obvious.
- A prototype is an argument, not a product. You still have to be able to explain what in it is real and what is a stub, and defend the idea under your own name ([11.3](#11-high-stakes-decisions)). Otherwise a fast prototype turns into comprehension debt with a demo.
- You're skipping approval for the idea, not the checks. Stakes still follow [3.1](#3-delegate-or-not); a winning prototype only goes to production the normal way: [9.2](#9-verification) → [7.1](#7-writing-code-and-debugging) → [15.1](#15-finishing-any-task).

### 22.1 One idea, one prototype
`[ANY CHAT]`, ideally `[AGENT WITH TOOLS]` · BEFORE

```text
Help me cut a prototype down to one idea that can be built over a weekend. Don't start building yet. Don't come up with ideas for me.

THE IDEA (in one sentence): [IDEA]
WHICH ORGANIZATIONAL GOAL IT SERVES (as I understand it; what I know about the goals one level above my manager): [GOAL]
WHAT I WANT TO PUT INTO THE PROTOTYPE: [LIST OF FEATURES / PARTS]
WHO NEEDS TO GET THE IDEA FROM THE PROTOTYPE: [WHO MAKES THE DECISION]

0. Goal check: if it succeeds, how much would the idea change the odds of reaching the goal: radically, or is it a backlog improvement? Don't soften it. If the goal is vague, phrase a question for me to ask, say which role to ask, and stop.
1. State the core of the idea in one sentence: what a busy person should see and understand in the first two minutes.
2. Split my list into: “the idea doesn't make sense without this” / “a separate idea, set it aside” / “infrastructure that can be faked with a stub”.
3. If the list contains more than one idea, name them separately and ask which one I choose. Stop until I answer.
4. The minimal scope of the prototype: what's real, what's a stub. Stubs will be honestly labeled in the demo.
5. Boundaries: the prototype doesn't go to production and doesn't touch real users or production data. What's needed to guarantee that.
6. The prototype's success criterion: what decision or question from leadership it should trigger.
```

### 22.2 The prototype as an argument
`[SAME CHAT]` or `[ANY CHAT]` with a description of the prototype · AFTER

```text
The prototype is ready. Help me turn it into an argument for the people who decide, and check that I can defend it myself.

THE PROTOTYPE (what it does, what's real in it, what's a stub): [DESCRIPTION]
THE ORGANIZATIONAL GOAL IT SERVES: [GOAL]
WHO I'M SHOWING IT TO: [WHO DECIDES]

1. A 3–5 minute demo script: what problem to open with, what to show, where to end. One idea, no distractions.
2. An explicit list: what in the prototype is real, what's a stub, what doesn't scale. I'll show it myself instead of waiting to be asked.
3. 5 questions this person will ask (cost, risks, who'll maintain it, why it wasn't done before, what's next). Wait for my answers, then mark where I'm shaky.
4. What exactly I'm asking for at the end: time, people, a decision. One sentence.
5. What's missing to make it clear that I'm the one who can lead this.
```

---

## The 30-second checklist

1. Am I solving the right problem, and how will I know I'm done?
2. Did I write down my hypothesis before asking the AI?
3. Is the AI helping me think or thinking for me, and is that my deliberate choice?
4. Did I define “verified” in advance and put time for my own check into the plan?
5. Did I look at the real output (log, terminal, CI) myself before the summary? Do I know what the green check proved and what it didn't?
6. What would have to be true for this to be wrong, and did I check that with a test rather than the model's confidence?
7. Did I hear a counterargument from another angle (a different model, a different chat)?
8. Do I know which decisions and assumptions the AI made for me?
9. Did I write down, myself, one thing the AI didn't check?
10. Would I put my name on this in front of the person who'll maintain it, or was I just persuaded by the polished format?
11. Did I ask for the most ambitious version (higher, deeper, wider) that I can check with an external judge rather than the model's word?

---

## New prompt template and editing rules

**Numbering rules:**
- A block or prompt number, once assigned, is never reused or renumbered: the situation table and other prompts link to it.
- Don't erase a removed prompt. Keep its heading with the note `(removed YYYY-MM-DD: reason, replaced by → X.Y)` and delete the body.
- A new prompt goes at the end of its block, with the next free number. A new block goes after the last block (23, 24, …), before the checklist. Add it to the contents, to an island in `ISLES` in `src/template.html` (or the build stops) and, if needed, to the “Situation and prompt” table.
- Write block headings without quotes, colons or dashes so the anchor links don't break.
- Record every change in the “Changelog”.

**Block and prompt template:**

````text
## N. Block name

**When to use:** [the situation in one line]

**Keep in mind:**
- [2–6 points]

### N.M Prompt name
`[ANY CHAT | SAME CHAT | NEW CHAT / OTHER MODEL | AGENT WITH TOOLS]` · BEFORE | DURING | AFTER | ONGOING

Short: (for long prompts, a 2–3 line version in a separate text block, or a link to the prompt that serves as one)

```text
[What to do and what NOT to do.]

FIELD: [PLACEHOLDER]
MY HYPOTHESIS: [MY HYPOTHESIS]   ← if relevant
HONESTY: ...                     ← word for word, if the prompt is about checks, output or sources

1. ...
2. ...
[Where to stop and wait for me.]
```
````

---

## Glossary

| Term | Meaning |
|---|---|
| Cognitive offloading | You delegate the task but own the result. Healthy. |
| Deferral | The tool's output becomes your input and stops being a hypothesis. |
| Cognitive surrender | The AI's output quietly becomes yours, and you don't feel any need to check it. |
| Cognitive debt | The debt of understanding that builds up when you hand off your thinking, including when you sign off on specs and strategies. |
| Comprehension debt | Cognitive debt applied to code: the code is clean, the tests are green, and nobody understands it. |
| Erosion of the shared theory of the system | The team loses its shared understanding of the system. It surfaces when things change. |
| Rebuilding understanding on demand | Instead of holding a model of the whole codebase, ask for an explanation of the slice you need. |
| Blind spot pass | You give the model everything you know and it looks for your unknown unknowns. |
| Verification loop | Give the agent a way to check its own work: tests, e2e, an actual run. |
| The real-review rule | If you can't say what the checks will miss, ask for a real review, not a quick approval. |
| Intent debt | Unstated goals, constraints and motives that aren't in the task framing. |
| Orchestration tax | The gap between what the agents generate and what you're prepared to put your name on. |
| Paradox of supervision | Supervising AI takes the very coding skills that waste away from leaning on AI too much. |
| Speed / Altitude / Depth / Range | Four kinds of ambition: the same thing faster; higher in abstraction (the outcome instead of the task); deeper (the methods of the best professionals); wider (methods from other fields). |
| External judge | Don't ask the model to grade itself; the best judge is a tool it runs and gets an answer from immediately. |
| Nouns into verbs | Describe the task as an action to see which fields could help. |
| Red team | The adversarial part of a team whose job is to find weaknesses (for example, a short seller or a forensic accountant). An adversarial agent has an inverted success criterion: it has to bring back a reproducible failure. |
| Newcomer's fresh eyes | Newcomers notice friction and opportunities that old-timers no longer see; organizations need an influx of “naive” people. |
| The old-timer trap | Your own “I already tried” turns into an untested belief; a newcomer with the same idea simply asks. |

---

## Changelog

| Date | Version | What changed | Why |
|------|---------|--------------|-----|
| 2026-11-11 | 1.0 | First public release: 23 blocks, 69 prompts, the situation table, the 30-second checklist, the glossary | |
