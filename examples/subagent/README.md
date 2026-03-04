# Subagent Example: Data Quality Checker

This folder contains a working example of a **subagent** — one of the most powerful concepts in AI-assisted work. Before we explain how to install it, let's answer the most important question first.

---

## What Is a Subagent?

Think about how a good executive operates. You don't do everything yourself. You delegate. When you need a financial audit, you don't personally comb through spreadsheets — you assign that to someone who specializes in it. They do the work, then report back to you with a summary.

Claude works the same way with subagents.

When you ask Claude to handle a complex task, Claude can recognize that part of the job requires specialized focus. Instead of doing everything itself in one big pass, Claude can **delegate** that piece to a subagent — a separate AI worker with a specific job description. The subagent does its work, then hands the results back to Claude, who synthesizes everything into an answer for you.

You don't manage this handoff. Claude handles it automatically.

---

## What Does This Subagent Do?

This particular subagent is called **data-checker**. Its one job is to look at data files (specifically CSV files — the kind you might export from Excel, an EHR system, or a database) and produce a plain-English report of anything that looks wrong.

It checks for:

- **Missing information** — cells that are blank or filled with placeholders like "N/A" or "unknown"
- **Formatting inconsistencies** — dates written three different ways, phone numbers with and without dashes
- **Suspicious values** — a patient age of 847, a negative cost, a duplicate record
- **Structural problems** — rows with the wrong number of columns, missing headers

The data-checker works quietly in the background. Claude assigns it the task, it scans your files, and it returns a structured report that Claude then presents to you in plain English.

---

## How Is a Subagent Different from a Skill?

This is a question worth pausing on, because the distinction matters.

| | Skill | Subagent |
|---|---|---|
| **Who triggers it?** | You do, by typing a slash command like `/summarize` | Claude does, on its own, when it decides it needs help |
| **When is it useful?** | When you have a repeatable task you want to run on demand | When a bigger task has a specialized piece that should be handled separately |
| **Analogy** | A button you press to run a specific process | A specialist you've hired who Claude can call when the work requires it |

A skill is a tool you use. A subagent is a team member Claude uses.

---

## Why Does This Matter?

Three reasons, in plain English:

**1. Delegation**
You wouldn't ask your CMO to personally audit every spreadsheet. You'd have the right person do it. Subagents apply that same logic to AI. Claude stays at the strategic level while specialized workers handle the detailed, tedious tasks.

**2. Parallelism**
If you have ten data files to check, Claude could potentially assign the data-checker subagent to work on multiple files at the same time, rather than processing them one by one. That's faster.

**3. Specialization**
A subagent has a focused job description. It knows exactly what to look for and how to report it. That focus makes it more reliable at its specific task than a generalist trying to do everything at once.

In healthcare, this starts to matter a lot. Imagine subagents that specialize in checking clinical data, billing codes, scheduling records, or compliance documentation — all working in parallel while you simply ask Claude, "Is our data ready for the audit?"

---

## How to Install This Example

You can drop this subagent into any project where you want Claude to be able to check data quality automatically.

**Step 1: Open your terminal**

On a Mac, press Command + Space, type "Terminal", and press Enter.

**Step 2: Navigate to your project folder**

Type `cd` followed by a space, then drag your project folder into the terminal window. Press Enter.

**Step 3: Create the skills folder**

Copy and paste this command, then press Enter:

```
mkdir -p .claude/skills
```

This creates a hidden folder where Claude looks for subagents and skills.

**Step 4: Copy the skill file**

Copy the `SKILL.md` file from this example folder into the `.claude/skills/` folder you just created. You can do this in Finder or with the terminal.

**Step 5: Open Claude Code in your project**

Launch Claude Code and point it at your project folder.

**Step 6: Ask Claude to check your data**

You don't need a special command. Just ask naturally:

> "Can you check the data quality of my CSV files?"

> "Something looks off in our patient data exports — can you take a look?"

> "We're about to run a report. Can you validate the source data first?"

Claude will recognize that the data-checker subagent is available and will invoke it automatically. A few moments later, you'll get a plain-English summary of what it found.

---

## A Note for Non-Technical Leaders

You don't need to understand how this works under the hood to benefit from it. What matters is the pattern: you describe what you need, Claude decides how to get it done, and specialized workers handle the details.

The same pattern that makes a well-run organization efficient applies here. You're not learning to code. You're learning to delegate — to AI.
