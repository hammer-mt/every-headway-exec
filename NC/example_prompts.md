# Example Prompts for Neha Chaudhary, CMO at Headway

These prompts are ready to copy-paste into Claude. Each one references the synthetic data files in your folder and demonstrates how to use Claude as a real productivity tool for your work as Chief Medical Officer.

---

## Idea 1 - Clinical PRD Review

**What it does:** Runs your product requirements document through a structured clinical review, scores each dimension using your rubric, and surfaces qualitative feedback you can bring directly into a product conversation.

```
I'm the Chief Medical Officer at Headway, a mental health technology company. I need you to conduct a rigorous clinical review of a product requirements document.

I'm going to paste the contents of two files:
1. sample_prd.md — the PRD under review
2. clinical_review_rubric.csv — the rubric with dimensions and scoring criteria

[Paste contents of sample_prd.md here]

[Paste contents of clinical_review_rubric.csv here]

Please do the following:
- For each dimension in the rubric, assign a score according to the criteria defined
- Present scores in a summary table with columns: Dimension, Score, Max Score, % Score
- After the table, write 2–3 sentences of qualitative feedback for each dimension explaining the rationale behind the score and what would be needed to improve it
- Flag any dimensions where the PRD scores below 70% with a "NEEDS ATTENTION" label
- Close with an overall clinical readiness assessment: Ready / Conditionally Ready / Not Ready, and a 1-paragraph justification

Be direct. I need feedback I can bring into a product review meeting, not general observations.
```

---

## Idea 2 - AI Safety Planning

**What it does:** Combines your safety plan template with your crisis resource database to build a step-by-step interactive workflow that care coordinators or providers can walk a patient through in session.

```
I'm the Chief Medical Officer at Headway. I'm building a clinician-facing AI safety planning tool and need your help designing the interactive workflow logic.

I'm going to paste the contents of two files:
1. safety_plan_template.json — the structured safety plan schema we use
2. crisis_resources.csv — a database of crisis resources including hotlines, text lines, and local services by region

[Paste contents of safety_plan_template.json here]

[Paste contents of crisis_resources.csv here]

Using these two inputs, please:
1. Map each field in the safety plan template to a specific clinician prompt — the actual question or statement a provider would say to a patient to elicit that information
2. Flag any template fields that are ambiguous or missing guidance, and suggest how to clarify them
3. Build a decision tree for the crisis resources section: given a patient's state/region and their expressed preference (call vs. text vs. chat), which resource(s) should surface first?
4. Identify any gaps in the crisis_resources.csv — are there states or resource types that are missing?
5. Draft a one-page summary of this workflow written for a non-clinical care coordinator who needs to understand how to use it

Format the clinician prompts as a numbered list. Format the decision tree as a simple flowchart using text/indentation.
```

---

## Idea 3 - Provider Copilot

**What it does:** Analyzes your patient session data against defined clinical triggers to surface a prioritized list of patients who may need outreach, escalation, or clinical review — the kind of signal a copilot tool would surface for a provider.

```
I'm the Chief Medical Officer at Headway. I'm evaluating the feasibility of a provider copilot feature that flags patients who may need clinical intervention between sessions.

I'm going to paste the contents of two files:
1. patient_session_data.csv — de-identified session records including session notes fields, attendance, symptom scores, and other structured data
2. clinical_triggers.csv — the trigger definitions including criteria, severity levels, and recommended actions

[Paste contents of patient_session_data.csv here]

[Paste contents of clinical_triggers.csv here]

Please do the following:
1. For each patient in the session data, check whether any clinical triggers are met based on the trigger criteria
2. Produce a prioritized intervention list — a table with columns: Patient ID, Trigger(s) Fired, Severity, Recommended Action, Days Since Last Session
3. Sort by severity (highest first), then by days since last session (most days first)
4. For patients with multiple triggers fired, note whether the combination escalates the recommended action
5. Identify any triggers in clinical_triggers.csv that could not be evaluated because the required data field is missing from patient_session_data.csv — list these as data gaps
6. Write a brief (3–5 sentence) interpretation of the overall cohort: what patterns stand out, and what does this suggest about the sensitivity and specificity of the trigger set?

This analysis is for internal product evaluation, not direct clinical use.
```

---

## Idea 4 - Thought Leadership

**What it does:** Cross-references external mental health news with Headway's internal updates to identify where Headway's work is relevant to the current conversation, then drafts a thought leadership piece you could publish or post.

```
I'm the Chief Medical Officer at Headway, a mental health technology company. I want to draft a thought leadership piece that positions Headway at the intersection of what's happening in the industry and what we're actually doing internally.

I'm going to paste the contents of two files:
1. news_feed_sample.csv — recent external news stories and developments in mental health, healthcare policy, and health tech
2. internal_updates.csv — recent Headway product launches, clinical program updates, and company milestones

[Paste contents of news_feed_sample.csv here]

[Paste contents of internal_updates.csv here]

Please do the following:
1. Identify the top 3 external themes or narratives from the news feed that are most relevant to mental health access, provider experience, or clinical quality
2. For each theme, match it to one or more internal updates from Headway that speak directly to that theme
3. Identify any internal updates that have no obvious external news match — these may represent areas where Headway is ahead of the public conversation
4. Draft a 600–800 word thought leadership piece written in my voice as CMO. The piece should: open with a provocative observation about the current state of mental health care, weave in 2–3 of the strongest theme/internal-update pairings as evidence of what's working, and close with a forward-looking statement about what the field needs to do next
5. Suggest 3 possible titles for the piece and 2 possible publication venues (e.g., STAT News, LinkedIn, Health Affairs)

Write the draft at a level appropriate for a sophisticated healthcare audience — not a general consumer piece.
```

---

## Idea 5 - Risk Register

**What it does:** Scans incoming regulatory news against your existing risk register to flag whether any new items should be added, any existing risks should be re-rated, or any items can be closed — keeping your risk register current without a manual review process.

```
I'm the Chief Medical Officer at Headway. I maintain a clinical and regulatory risk register and need to keep it current as the regulatory environment evolves.

I'm going to paste the contents of two files:
1. risk_register.csv — our current risk register with existing risk items, likelihood scores, impact scores, owners, and status
2. regulatory_news_feed.csv — recent regulatory news, guidance documents, enforcement actions, and policy updates relevant to mental health and telehealth

[Paste contents of risk_register.csv here]

[Paste contents of regulatory_news_feed.csv here]

Please do the following:
1. For each item in the regulatory news feed, assess whether it is relevant to Headway's risk profile
2. For relevant news items, determine whether they:
   a. Map to an existing risk register entry and suggest an updated likelihood or impact score with rationale
   b. Represent a net-new risk not currently in the register and should be added as a new entry
   c. Indicate that an existing risk has materially decreased and could be downgraded or closed
3. Produce a change summary table with columns: News Item, Action (Update / Add / Downgrade / No Action), Risk ID (if applicable), Rationale
4. Draft the full text of any new risk register entries you recommend adding, using the same schema and field structure as the existing register
5. Flag any news items where you have low confidence in the relevance assessment and explain why

Be conservative — when in doubt about relevance, flag it for human review rather than dismissing it.
```

---

## Idea 6 - Patient Outcomes Dashboard

**What it does:** Compares Headway's patient outcomes data against external benchmarks to generate a structured insights summary — the kind of narrative that would accompany a board-level or clinical leadership dashboard.

```
I'm the Chief Medical Officer at Headway. I'm preparing a clinical outcomes summary for leadership and need help interpreting our outcomes data relative to external benchmarks.

I'm going to paste the contents of two files:
1. patient_outcomes.csv — de-identified patient outcomes data including measures like PHQ-9 change scores, session completion rates, time to symptom improvement, and retention
2. benchmark_data.csv — external benchmark values for the same or comparable measures, sourced from published research or industry comparisons

[Paste contents of patient_outcomes.csv here]

[Paste contents of benchmark_data.csv here]

Please do the following:
1. For each outcome measure that appears in both files, calculate Headway's performance relative to the benchmark — show the absolute difference and whether Headway is above, at, or below benchmark
2. Present this in a summary table with columns: Measure, Headway Value, Benchmark Value, Difference, Direction (Above / At / Below)
3. Identify the 2–3 measures where Headway's performance is strongest relative to benchmark, and the 2–3 where there is the most room for improvement
4. Write a 400–500 word executive narrative summarizing the outcomes picture. It should: open with the headline finding, walk through the key strengths and gaps, note any data limitations or caveats in comparability, and close with 2–3 recommended areas of focus for the next quarter
5. Flag any measures in patient_outcomes.csv that have no benchmark match and note whether finding a benchmark for these should be a priority

Write the narrative in a tone appropriate for a board deck or clinical leadership review — clear, direct, and evidence-grounded.
```
