---
name: boring-to-brilliant
description: Turns dry, technical B2B products (inverters, batteries, SaaS, industrial equipment, compliance software, logistics, chemicals, anything with a spec sheet) into human stories, sharp campaign angles, hooks and headlines that a real buyer would stop for. Use this skill whenever someone shares a datasheet, feature list, product page or technical brief and wants marketing out of it, says their product is "boring", "too technical", "hard to market" or "all features no story", asks for campaign angles, a big idea, positioning, LinkedIn hooks or ad concepts for a B2B or technical product, or wants existing B2B copy made less generic, even if they never say "creative".
---

# Boring to Brilliant

Technical products are not boring. Their marketing is, because it stops at the spec.
A buyer doesn't want "98.5% max efficiency". They want to stop being the person who
explains to the CFO why the system underperformed. This skill climbs from the spec to
that human stake, then builds angles from there, and only keeps the ones that could
survive a skeptical engineer and a scrolling CFO.

Work in the user's language. If they write in Hebrew, answer in Hebrew (keep technical
units and product names as they are).

## The process

Run these five moves in order. Show your work in the final output, because the
translation table is often as useful to a marketing team as the ideas themselves.

### 1. Intake (ask only what you can't infer)

You need: the product, who buys it, what proof exists (numbers, certifications, case
studies, warranty), and any claims that are off-limits (regulated industries, parent
company approval, competitor naming rules). If the user gave a datasheet or link, read
it fully before asking anything. If something essential is missing, ask at most three
short questions in one message, then proceed. If the user seems to want speed, make
sensible assumptions and state them at the top.

B2B purchases have more than one buyer. Identify who matters, usually some of:
- **The economic buyer** (CFO, owner): cares about money, risk, payback, looking smart to the board.
- **The technical buyer** (engineer, IT, installer): cares about whether it actually works, and about not being blamed.
- **The user** (operator, site manager): cares about their daily hassle.
- **The blocker** (procurement, legal, safety): cares about compliance and the paperwork.

Angles usually land hardest when they're aimed at one of these people, not all of them.

### 2. The So-What Ladder

For the 4–6 most important specs or features, climb the ladder. Keep asking "so what?"
until you hit something a person feels.

| Rung | Question | Example (commercial battery) |
|---|---|---|
| Feature | What is it? | 2-hour liquid-cooled battery |
| Function | What does it do? | Stores midday solar, releases it in the evening |
| Benefit | Why is that good? | Shifts consumption out of peak tariff hours |
| Business outcome | What changes in the numbers? | Lower peak-demand charges, faster payback |
| Human stake | What does the buyer feel, fear or get to brag about? | The facility manager stops getting the 5pm call from finance |

The human stake is the raw material for everything that follows. If you can't reach
one, say which feature has no story yet. That's useful too.

### 3. Find the tension

Great angles come from tension, not from benefits. Look for:
- **The enemy**: what the status quo quietly costs (wasted energy, downtime, the
  spreadsheet nobody trusts, the installer's lost Saturday).
- **The belief to break**: what the market assumes that this product proves wrong.
- **The invisible**: what the product does that nobody sees until it fails.
- **The category cliché**: what every competitor says (blue skies, handshakes,
  "innovative solutions"). This is what to avoid and sometimes what to mock.

Write one sentence of insight in the form: *"[Buyer] wants [X], but [tension], so
[what they secretly need]."*

### 4. Generate angles through lenses

Read `references/lenses.md` and generate at least 8 angles using at least 6
different lenses. Each lens is a different way to break the "list the features"
reflex. Variety matters more than polish at this stage. The point is to give the
user ideas they wouldn't have reached on their own, so push past the first obvious
idea under each lens.

### 5. Score and kill

Score every angle 1–5 on:
- **Stop power**: would the target buyer stop scrolling?
- **Truth**: can it be proven with the proof that actually exists? (Invented stats get a 1.)
- **Ownability**: run the **logo-swap test**: put a competitor's logo on it. If it
  still works, it's not ownable.
- **Buyer fit**: does it speak to the specific buyer's stake?
- **Makeability**: could a small team produce it with a normal budget?

Kill anything with Truth ≤ 2 or Ownability ≤ 2, no matter how clever. A brilliant
claim you can't back up is a legal problem, not a campaign. Keep the top 3.

Before writing final copy, run every line through the cliché check (see below).

## Output format

Use this structure, and keep it scannable. Marketers skim.

```
# Boring → Brilliant: [Product]

**Assumptions** (only if you made any)

## The translation
[So-What Ladder table for the key features]

## The insight
[One sentence of tension]

## The cliché to avoid
[What every competitor in this category says, in one line]

## All angles (scored)
[Compact table: angle name | lens | one-line idea | stop | truth | own | fit | make | total]

## The top 3

### 1. [Angle name] — [lens]
**The idea:** 2–3 sentences.
**Who it's for:** which buyer.
**Headline:** ...
**LinkedIn hook (first 2 lines):** ...
**Ad line (≤ 8 words):** ...
**Visual:** what you'd see.
**Proof needed:** the exact fact or asset required to run this honestly.
**Boring version → Brilliant version:** the generic line vs. the new line, side by side.

(repeat for 2 and 3)

## Quick wins
3 small things they can do this week with existing assets (rewrite a product-page
headline, a post format, a sales-deck slide).
```

Mark any number you didn't get from the user or their materials as
**[needs verification]**. Never invent statistics, customer names or quotes, because
B2B buyers check, and one fake number poisons the whole campaign.

## The cliché check

Generic B2B language is the main reason technical marketing feels boring. Before
delivering, check all copy against `references/cliche-blacklist.md`. If a script
runtime is available, run:

```bash
python scripts/cliche_check.py "<your copy>"
# or: python scripts/cliche_check.py --file draft.md
```

It flags clichés and vague words and gives a score. Rewrite anything it flags unless
the user explicitly wants that phrase. If you can't run scripts, check against the
list by reading it.

## When the user brings existing copy

If they paste copy they already have and ask to make it better: run the cliché check
first, show the score, then run steps 2–5 on what the copy is trying to say. Show a
before/after for every line you change.

## Worked example

`references/example-inverter.md` shows the full process on a commercial solar
inverter. Read it if you're unsure what "good" looks like, particularly for how far
to climb the ladder and how hard to be when scoring.
