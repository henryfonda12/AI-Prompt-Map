"""Parse the cheat sheet into JSON without altering any wording.

Any structural problem (lost line, prompt without text, duplicate id, broken
link, unparsed block heading) is an error: the script exits non-zero before
writing the JSON, so build.sh never overwrites index.html with a broken page.
"""
import json, re, sys
from collections import Counter

with open(sys.argv[1], encoding="utf-8") as f:
    src = f.read()
lines = src.split("\n")
errors = []

# ---- split into level-2 sections (respect 4-backtick fences) ----
sections, cur, fence4 = [], None, False
head = []
for ln in lines:
    if ln.startswith("````"):
        fence4 = not fence4
    if not fence4 and ln.startswith("## "):
        cur = {"title": ln[3:].strip(), "lines": []}
        sections.append(cur)
        continue
    (cur["lines"] if cur else head).append(ln)


def chunks(body, where):
    """Return list of ('text', str) / ('code', str) keeping order."""
    out, buf, code, in_code = [], [], [], False
    for ln in body:
        if not in_code and ln.startswith("```text"):
            if buf:
                out.append(("text", "\n".join(buf).strip("\n")))
                buf = []
            in_code, code = True, []
        elif in_code and ln.rstrip() == "```":
            out.append(("code", "\n".join(code)))
            in_code = False
        elif in_code:
            code.append(ln)
        else:
            if ln.startswith("```"):
                errors.append(f"{where}: code blocks must open with ```text, found: {ln.strip()}")
            buf.append(ln)
    if in_code:
        errors.append(f"{where}: unclosed ```text block (no closing ``` line)")
    if buf:
        out.append(("text", "\n".join(buf).strip("\n")))
    return [c for c in out if c[1].strip() or c[0] == "code"]


def strip_rule(t):
    return re.sub(r"\n*---\s*$", "", t).strip("\n")


def parse_prompt_body(pid, title, body):
    p = {"id": pid, "title": title, "meta": "", "notes": [], "after": [], "short": None, "full": None}
    ch = chunks(body, f"prompt {pid}")
    pending_short = False
    for kind, val in ch:
        if kind == "text":
            val = strip_rule(val)
            if not val:
                continue
            for para in re.split(r"\n\s*\n", val):
                para = para.strip()
                if not para:
                    continue
                if para.startswith("`[") and not p["meta"]:
                    p["meta"] = para
                elif para == "Short:":
                    pending_short = True
                else:
                    p["after" if p["full"] is not None else "notes"].append(para)
        else:
            if pending_short:
                p["short"] = val
                pending_short = False
            elif p["full"] is None:
                p["full"] = val
            else:
                errors.append(f"prompt {pid}: extra code block. The next prompt's heading probably doesn't "
                              f"follow the “### N.M Name” template (no period after the number)")
    return p


blocks, extra = [], {}
for s in sections:
    m = re.match(r"^(\d+)\. (.+)$", s["title"])
    if not m:
        if re.match(r"^\d", s["title"]):
            errors.append(f"heading “## {s['title']}” looks like a block but doesn't follow the “## N. Name” template")
        extra[s["title"]] = strip_rule("\n".join(s["lines"]).strip("\n"))
        continue
    num, name = m.group(1), m.group(2)
    blk = {"n": int(num), "title": name, "when": "", "keep": "", "intro": [], "prompts": []}
    body = s["lines"]
    if num == "0":
        # one-liners: **0.x** title meta  + code
        ch = chunks(body, "block 0")
        last = None
        for kind, val in ch:
            if kind == "text":
                for para in re.split(r"\n\s*\n", strip_rule(val)):
                    para = para.strip()
                    if not para:
                        continue
                    mm = re.match(r"^\*\*(0\.\d+)\*\* (.+)$", para)
                    if mm:
                        last = {"id": mm.group(1), "title": mm.group(2), "meta": "", "notes": [], "short": None, "full": None}
                        blk["prompts"].append(last)
                    elif para.startswith("**When to use:**"):
                        blk["when"] = para
                    else:
                        if re.match(r"^\*\*0\D?\d", para):
                            errors.append(f"block 0: one-liner doesn't follow the “**0.N** Name” template: {para[:60]}")
                        blk["intro"].append(para)
            elif last is None:
                errors.append("block 0: a code block comes before the first **0.N** one-liner")
            elif last["full"] is not None:
                errors.append(f"one-liner {last['id']}: second code block. The next one-liner's heading probably "
                              f"doesn't follow the “**0.N** Name” template")
            else:
                last["full"] = val
    else:
        # split on ### headings
        pre, parts, curp = [], [], None
        for ln in body:
            mm = re.match(r"^### (\d+\.\d+) (.+)$", ln)
            if mm:
                curp = [mm.group(1), mm.group(2), []]
                parts.append(curp)
            elif curp:
                curp[2].append(ln)
            else:
                pre.append(ln)
        for para in re.split(r"\n\s*\n", "\n".join(pre).strip()):
            para = para.strip()
            if para.startswith("**When to use:**"):
                blk["when"] = para
            elif para.startswith("**Keep in mind:**"):
                blk["keep"] = para
            elif para:
                blk["intro"].append(para)
        for pid, title, b in parts:
            blk["prompts"].append(parse_prompt_body(pid, title, b))
    blocks.append(blk)

# split title / lead from head
data = {"head": "\n".join(head).strip("\n"), "blocks": blocks, "extra": extra}

# ---- fidelity: every non-empty source line must appear verbatim, as many times as in the source ----
blob = []
def walk(o):
    if isinstance(o, str):
        blob.append(o)
    elif isinstance(o, dict):
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(data)
# one-liners are stored without their "**0.x** " prefix: restore it for the check
blob += [f"**{p['id']}** {p['title']}" for b in blocks if b["n"] == 0 for p in b["prompts"]]
have = Counter(t.strip() for s in blob for t in s.split("\n"))
need = Counter()
for i, ln in enumerate(lines, 1):
    t = ln.strip()
    if not t or t in ("---", "```text", "```", "Short:") or t.startswith("## ") or t.startswith("### "):
        continue
    need[t] += 1
    if need[t] > have[t]:
        errors.append(f"line {i} is missing from the data: {t[:80]}")

# ---- prompts: text present, ids unique ----
ids = Counter()
for b in blocks:
    for p in b["prompts"]:
        ids[p["id"]] += 1
        if not p["full"]:
            errors.append(f"prompt {p['id']}: no text (no ```text block)")
        if not p["id"].startswith(f"{b['n']}."):
            errors.append(f"prompt {p['id']} sits in block {b['n']}")
errors += [f"prompt number {i} appears {n} times" for i, n in ids.items() if n > 1]

# ---- links [2.2](#2-...): prompt must exist and live in the anchored block ----
nums = {b["n"] for b in blocks}
link_re = re.compile(r"\[([^\]]+)\]\((#[^)]+)\)")
for s in blob:
    for text, href in link_re.findall(s):
        am = re.match(r"^#(\d+)-", href)
        if re.fullmatch(r"\d+\.\d+", text) and text not in ids:
            errors.append(f"link [{text}]({href}): no such prompt")
        elif am and int(am.group(1)) not in nums:
            errors.append(f"link [{text}]({href}): no such block")
        elif am and text in ids and not text.startswith(am.group(1) + "."):
            errors.append(f"link [{text}]({href}): the prompt is in a different block")
for ln in extra.get("Situation and prompt", "").split("\n"):
    for text, href in link_re.findall(ln):
        if text not in ids and not re.match(r"^#\d+-", href):
            errors.append(f"“Situation and prompt”: step [{text}]({href}) points to neither a prompt nor a block")

print("prompts:", sum(len(b["prompts"]) for b in blocks), "blocks:", len(blocks), file=sys.stderr)
if errors:
    print(f"ERRORS ({len(errors)}), data not written:", *errors, sep="\n  ", file=sys.stderr)
    sys.exit(1)
with open(sys.argv[2], "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
