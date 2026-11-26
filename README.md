# Boring → Brilliant

**A Claude skill that turns dry, technical B2B products into marketing people actually stop for.**

Inverters. Cold-chain loggers. Compliance software. Industrial valves. If your product
comes with a datasheet, its marketing probably sounds like this:

> *"Innovative, state-of-the-art solutions that empower your team with seamless, reliable performance."*

That sentence scores **0/100** on this skill's cliché check. Here's what the skill
turned it into for a pharma temperature logger:

> **Every shipment needs an alibi.**
> *14:02 – 6.8°C. 14:03 – 6.9°C. 14:04 – 8.1°C. Where was your shipment at 14:04?*

Same product. Same specs. Nothing invented.

---

## What it does

You give Claude a spec sheet, a product page or a two-line description. The skill
runs a five-step creative process:

| Step | What happens |
|---|---|
| **1. Intake** | Works out *who* actually buys: the CFO, the engineer, the operator, or procurement. They want different things. |
| **2. The So-What Ladder** | Climbs every feature from *spec → function → benefit → business outcome → human stake*. "98.5% efficiency" becomes "the CFO sees the number match the proposal." |
| **3. Find the tension** | The enemy, the belief to break, the invisible value, and the category cliché to avoid. |
| **4. 12 creative lenses** | Generates 8+ angles through lenses like *Name the villain*, *Borrowed world*, *Honest confession* and *The tiny moment*. |
| **5. Score & kill** | Scores every angle on stop power, truth, ownability, buyer fit and makeability. Runs the **logo-swap test** (if a competitor's logo works on it, it's dead). Kills anything it can't prove. |

You get a scored table of all angles, then the top 3, each with a headline, a LinkedIn
hook, an ad line, a visual, the proof you'll need, and a **boring vs. brilliant**
side-by-side. Plus three quick wins you can ship this week.

### Built-in honesty
B2B buyers check everything. The skill never invents statistics, customers or quotes;
any number not from your materials is marked **[needs verification]**.

### The cliché checker
A small script that grades any copy for B2B clichés and gives a specificity score:

```bash
python boring-to-brilliant/scripts/cliche_check.py "Our innovative solutions empower your team"
# Specificity score: 0/100  (Boring: reads like every other B2B site)
#   [hollow promise] innovative
#   [vague verb] empower
#   [filler noun] solutions
```

The skill answers in whatever language you write in (the cliché list itself is English for now).

---

## Examples

- [Commercial solar inverter](boring-to-brilliant/references/example-inverter.md): "10 MPPTs for flexible system design" → **"Bring us your worst roof."**
- [Pharma cold-chain logger](examples/cold-chain-logger.md): "Real-time alerts for proactive monitoring" → **"Know at 2am. Not at 9."**

---

## Install

**Claude.ai / Claude app:** download this repo (green **Code** button → **Download ZIP**),
zip the inner `boring-to-brilliant/` folder, then upload it in the Skills section of
Claude's settings.

**Claude Code:** copy the folder into your skills directory:

```bash
git clone https://github.com/adameoded-commits/boring-to-brilliant.git
cp -r boring-to-brilliant/boring-to-brilliant ~/.claude/skills/
```

Then just ask something like:
> "Here's our datasheet for a commercial battery. Every competitor sounds the same. Give me campaign angles."

---

## What's inside

```
boring-to-brilliant/
├── SKILL.md                      # the process
├── references/
│   ├── lenses.md                 # the 12 creative lenses, with examples
│   ├── cliche-blacklist.md       # B2B clichés and how to fix them
│   └── example-inverter.md       # a full worked example
└── scripts/
    └── cliche_check.py           # the cliché checker
```

---

## Why I built this

I'm a marketing coordinator at an energy-tech company, not a developer. My job is
making inverters and batteries interesting, and I kept doing the same mental steps
on every campaign. So I wrote them down and turned them into a tool anyone can use.

Ideas, issues and pull requests are welcome, especially new lenses and cliché lists in
other languages.

## License
MIT
