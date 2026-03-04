# Claude Code Skill: Weekly Summary

## What is a Skill?

A skill is a saved set of instructions that tells Claude exactly how to handle a specific task. Think of it like a saved recipe — instead of explaining from scratch every time how you want your weekly report written, you save those instructions once, and Claude follows them automatically whenever you ask. You invoke a skill by typing a short command, like `/weekly-summary`.

---

## What Does This Skill Do?

This skill looks at any spreadsheet data (CSV files) in your current folder and produces a clean, well-structured executive summary — the kind of briefing you would hand to a board member or department head. It surfaces key metrics, calls out what is going well and what needs attention, and gives you a short list of recommended actions. All of that from a single command.

This is especially useful if your team exports weekly reports from your EMR, EHR, or financial system as CSV files. Instead of manually reviewing rows of numbers, you drop the file in a folder, type one command, and get a leadership-ready narrative in seconds.

---

## How to Install It

You only need to do this once per project or folder you want to use it in.

1. Open your terminal (on a Mac: press Command + Space, type "Terminal", hit Enter).
2. Navigate to your project folder. For example:
   ```
   cd ~/Documents/weekly-reports
   ```
3. Create the skills folder that Claude Code looks for:
   ```
   mkdir -p .claude/skills
   ```
4. Copy the `SKILL.md` file from this example into that folder:
   ```
   cp /path/to/this/SKILL.md .claude/skills/weekly-summary.md
   ```
   (Replace `/path/to/this/` with wherever you saved this file.)
5. Open Claude Code in that same folder.
6. Type `/weekly-summary` and press Enter.

That is it. Claude will read any CSV files in the folder and generate your report.

---

## How to Customize It

Open the `SKILL.md` file in any text editor (Notepad, TextEdit, or VS Code all work). Everything under the `## Instructions` section is plain English — just edit it the way you would revise a memo. For example:

- Want the report to always include a staffing section? Add a line that says so.
- Want Claude to flag anything above a certain readmission threshold? Write that in.
- Want the output in a specific format your team uses? Paste in your template.

There is no code to change. You are just editing the instructions Claude reads before it starts working.

---

## Why This Matters

Most AI interactions are one-off — you explain what you want, get an answer, and start over next time. Skills let you lock in your best thinking once and reuse it indefinitely. Your team gets consistent, high-quality outputs every week without anyone having to remember exactly how to phrase the request. It is the difference between a custom report and a standardized, repeatable workflow.
