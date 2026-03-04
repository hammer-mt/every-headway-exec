# Example Prompts for OKR Automation with Claude

These prompts are ready to copy-paste into Claude. Each one references the actual files in this folder and builds toward a fully automated OKR review workflow.

---

## Prompt 1: Identify Stale and At-Risk OKRs

**What it does:** Scans the OKR tracker, flags items that are behind schedule or haven't been updated recently, and produces a prioritized list of where attention is needed.

```
I'm going to share two files with you. Please analyze them and identify which Key Results are at risk or stale.

[Attach: okr_tracker.csv]
[Attach: weekly_updates_raw.md]

In okr_tracker.csv, each row is a Key Result with columns for objective, current value, target value, owner, due date, and last updated date. In weekly_updates_raw.md, team leads submitted their updates in varied formats — some structured, some freeform.

Please do the following:
1. Calculate progress percentage for each Key Result (current / target).
2. Flag any KR as "At Risk" if progress is below 60% and the due date is within 6 weeks.
3. Flag any KR as "Stale" if the last_updated date is more than 14 days ago and it doesn't appear to be mentioned in the weekly updates.
4. For each flagged item, include: the KR name, owner, current progress %, and a one-sentence note on why it's flagged.

Output as a clean table sorted by severity (At Risk first, then Stale).
```

---

## Prompt 2: Draft Updated OKR Statuses from Weekly Updates

**What it does:** Reads the raw team lead updates, maps them to the right Key Results, and drafts updated status notes — ready to paste directly into the OKR tracker.

```
I have weekly updates from team leads and an OKR tracker. I need you to cross-reference them and draft updated status notes for each Key Result that was mentioned.

[Attach: weekly_updates_raw.md]
[Attach: okr_tracker.csv]

The weekly updates in weekly_updates_raw.md are from 10 different team leads and are written in inconsistent formats — some use bullet points, some paragraphs, some include metrics, some don't. The OKR tracker in okr_tracker.csv has 20 Key Results across 5 objectives.

For each Key Result in the tracker:
1. Search the weekly updates for any mentions of that KR, its owner, or related work (use reasonable inference — the team lead may not name the KR explicitly).
2. If you find relevant information, draft a 2-3 sentence status update in past tense, written as if the KR owner submitted it. Be specific — include any numbers or milestones mentioned.
3. If no relevant update was found, write "No update this week" and flag it.
4. If a team lead mentioned work that seems relevant to a KR but you're uncertain, include it with a note: "[Needs verification]".

Format the output as a table with columns: Objective, Key Result, Owner, Drafted Status Update.
```

---

## Prompt 3: Build a Comprehensive OKR Health Report

**What it does:** Pulls from all three data sources to produce a full OKR health report — progress metrics, Jira execution signal, team update coverage, and a summary of risks and wins. Designed to replace a manual weekly review.

```
I need a comprehensive OKR health report that synthesizes data from three sources. Please analyze all three files and produce the report described below.

[Attach: okr_tracker.csv]
[Attach: weekly_updates_raw.md]
[Attach: jira_export.csv]

Context:
- okr_tracker.csv: 20 Key Results across 5 objectives with progress metrics and ownership.
- weekly_updates_raw.md: 10 team lead updates submitted this week in varied formats.
- jira_export.csv: 32 Jira tickets, each mapped to an OKR via a field in the export.

Please produce a report with the following sections:

**1. Executive Summary (5-7 sentences)**
Overall OKR health this week. How many KRs are on track, at risk, or stalled? Any standout wins or concerns?

**2. Objective-by-Objective Breakdown**
For each of the 5 objectives:
- Average progress % across its Key Results
- How many KRs have active Jira tickets vs. none (from jira_export.csv)
- Whether team leads submitted updates covering this objective (from weekly_updates_raw.md)
- A 2-3 sentence assessment: trajectory, risks, and recommended action

**3. Execution Signal from Jira**
- Which KRs have the most active tickets (opened or updated this week)?
- Which KRs have zero Jira activity? Flag these if the KR is not yet complete.
- Are there any Jira tickets marked as blocked? If so, which KRs are affected?

**4. Top 3 Risks**
Based on the combined data, identify the three most concerning KRs. For each, explain what the tracker shows, what Jira shows, and what (if anything) the team lead said.

**5. Top 3 Wins**
Identify three KRs showing strong momentum this week and briefly explain why.

Format the report cleanly with headers. Keep the tone direct and factual — this is an internal executive document, not a presentation.
```

---

## Prompt 4: Generate a Weekly Executive Briefing (Ready to Send)

**What it does:** Produces a polished, send-ready executive briefing email that Rob can review and forward to leadership. Combines all three data sources into a narrative format suitable for a VP or C-suite audience.

```
I need you to draft a weekly OKR executive briefing that I can review and send to leadership. It should be concise, confident, and decision-oriented — not a data dump.

[Attach: okr_tracker.csv]
[Attach: weekly_updates_raw.md]
[Attach: jira_export.csv]

First, analyze all three files:
- okr_tracker.csv for current progress across 20 Key Results and 5 objectives
- weekly_updates_raw.md for what teams reported this week
- jira_export.csv for execution activity mapped to each OKR

Then draft a briefing email with the following structure:

**Subject line:** Weekly OKR Briefing — Week of [insert current week]

**Opening (2-3 sentences):** High-level health of the OKR portfolio. Are we largely on track? Any major shifts from last week implied by the data?

**This Week's Highlights (3-5 bullet points):** The most important things that happened. Pull from team updates and Jira activity. Be specific — include numbers where available.

**Areas Requiring Attention (2-4 bullet points):** KRs that are at risk, stalled, or have no recent activity. For each, name the KR, the owner, and a one-line suggested action (e.g., "Schedule sync with [owner] to unblock X").

**On Track and Progressing (1 short paragraph):** Briefly acknowledge the KRs in good shape so leadership has a complete picture.

**Recommended Discussion Topics for Leadership Review:** List 2-3 questions or decisions that leadership should weigh in on based on what the data shows.

**Closing (1 sentence):** Standard close noting the next update timing.

Tone: Professional but direct. Avoid jargon. Write as if I (Rob Sadow, VP Strategy & Operations) am the author. Flag any assumptions you made due to ambiguous data with a [NOTE: ...] inline so I can verify before sending.
```
