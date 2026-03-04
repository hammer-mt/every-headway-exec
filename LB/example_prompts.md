# Example Prompts for Lorraine Buhannic, CPO at Headway

These prompts are ready to copy-paste into Claude. Each one references the actual data files in this folder and is designed to get high-value output quickly.

---

## Idea 1 — Candidate Sourcing

**What this does:** Cross-references your open roles against the employee directory to surface warm referral paths, then generates targeted sourcing strategies and personalized outreach templates for each role.

```
I'm the Chief People Officer at Headway, a mental health tech company. I'm going to share three CSV files with you:

- open_roles.csv — our current open requisitions with job titles, departments, levels, and hiring manager info
- employee_directory.csv — our full employee roster with names, roles, departments, tenure, and LinkedIn-style background fields
- candidate_pipeline.csv — candidates currently in process, including their source, stage, and role they're pursuing

Please do the following:

1. For each open role in open_roles.csv, scan employee_directory.csv to identify employees who are likely to have relevant professional networks for that role — based on their own background, previous companies, or domain expertise. List the top 2–3 employee referral targets per role and explain why each is a strong referral connector.

2. For roles with no strong internal referral path, recommend 3 specific sourcing channels or strategies (e.g., communities, niche job boards, LinkedIn search strings, competitive talent pools) tailored to the role's requirements.

3. For the top 5 hardest-to-fill open roles (use your judgment based on seniority, specialization, or current pipeline gaps visible in candidate_pipeline.csv), write a personalized outreach message I could send to a passive candidate on LinkedIn. The tone should reflect Headway's mission in mental health — warm, purposeful, and human. Each message should be 4–6 sentences.

Format the output as a role-by-role breakdown. I want this ready to action immediately.
```

---

## Idea 2 — Offer Analysis

**What this does:** Takes a specific role and candidate's compensation expectations, then models three distinct offer scenarios using your comp bands and market data — with a tradeoff analysis grounded in what has actually worked in your recent offers.

```
I'm the Chief People Officer at Headway and I'm preparing an offer for a candidate. I'll share three CSV files:

- comp_bands.csv — our internal compensation bands by level, role family, and geography
- market_data.csv — external market benchmarks (P25, P50, P75, P90) for comparable roles
- recent_offers.csv — a log of offers we've extended in the last 12 months, including structure, acceptance/decline outcome, and any notes on counter-offers or competing offers

Here is the specific situation:
- Role: Senior Product Manager, Growth
- Level: P5 (or equivalent in our band structure)
- Candidate location: New York, NY
- Candidate's stated expectations: $185,000 base, plus equity and bonus
- Competing offer in hand: $178,000 base from a Series C health tech company

Please do the following:

1. Model 3 distinct offer scenarios (conservative, competitive, and aggressive) using our comp_bands.csv and market_data.csv as anchors. For each scenario, specify: base salary, equity (% or dollar value if data supports it), bonus target, and any other notable comp elements. Show where each scenario falls relative to market percentiles.

2. For each scenario, provide a tradeoff analysis — what we gain and risk with each approach (e.g., budget impact, internal equity implications, candidate likelihood to accept).

3. Pull patterns from recent_offers.csv to inform the analysis: What has our acceptance rate looked like at different market positioning levels for similar roles? Have we lost candidates to competing offers in this range before? Are there any structural elements (e.g., signing bonus, accelerated vesting) that appear in accepted offers that we should consider here?

4. Give me a final recommendation with a one-paragraph rationale I could use to brief the hiring manager.
```

---

## Idea 3 — People Analytics Dashboard

**What this does:** Synthesizes headcount, recruiting funnel, and attrition data into a comprehensive people analytics report — surfacing trends, flight risks, and forward-looking predictive insights a CPO can take to the board or exec team.

```
I'm the Chief People Officer at Headway, a mental health tech company. I'm going to share three CSV files with you:

- headcount_data.csv — current and historical headcount by department, level, location, and employment type
- recruiting_funnel.csv — recruiting pipeline metrics over time, including req volume, applicants, interviews, offers, and hires by department and role type
- attrition_log.csv — records of every departure over the last 12–24 months, including voluntary vs. involuntary, tenure at departure, department, level, and any exit reason coding

Please build a comprehensive People Analytics Report structured as follows:

**Section 1 — Headcount Snapshot**
Summarize current headcount by department and level. Identify where we are growing, flat, or contracting. Flag any departments with headcount-to-revenue or headcount-to-output ratios that look unusual based on the data available.

**Section 2 — Recruiting Funnel Health**
Analyze the recruiting funnel from req open to hire. Identify: average time-to-fill by department, funnel conversion rates at each stage, and departments or role types where the funnel is most broken (high drop-off, low offer acceptance, etc.). Surface the top 3 recruiting bottlenecks.

**Section 3 — Attrition Analysis**
Break down attrition by voluntary vs. involuntary, by department, by tenure band (0–6 months, 6–18 months, 18+ months), and by level. Identify which segments have the highest attrition rates. Flag any patterns that suggest systemic issues (e.g., early tenure attrition in a specific team, senior-level voluntary departures clustering in a time period).

**Section 4 — Flight Risk Signals**
Based on the attrition patterns you've identified, define a flight risk profile — what tenure, level, and department combinations are statistically most likely to attrit next. Cross-reference with current headcount to estimate how many current employees fit that profile. Give me a number and a department-level breakdown.

**Section 5 — Predictive Insights and Recommendations**
Based on everything above, give me 3–5 forward-looking insights or recommendations I can bring to the exec team. These should be specific, prioritized, and actionable — not generic HR advice. Where the data supports it, include a projected impact (e.g., "reducing early attrition in Engineering by 20% would save approximately X recruiter hours and $Y in replacement costs based on current funnel metrics").

Format this as an executive-ready report. Use headers, bullet points where appropriate, and plain language. I want to be able to share this directly with my CEO and CFO.
```
