# Example Prompts for Olivia Millard Davis — CCO, Headway

These prompts are ready to copy-paste into Claude along with the relevant data files. For each prompt, attach the listed files before sending.

---

## Prompt 1: Monthly Payer Revenue Review

**Description:** Use this prompt at the start of each month to generate a comprehensive revenue review across your payer portfolio. It synthesizes monthly actuals, contract targets, forecast drivers, and quarterly metrics into an executive-ready briefing that surfaces at-risk payers and forward-looking themes.

**Files to attach:** `payer_revenue_monthly.csv`, `payer_contract_summary.csv`, `revenue_forecast_inputs.csv`, `quarterly_metrics_summary.csv`

```
I'm the Chief Commercial Officer at Headway, a mental health tech company that contracts with health insurance payers. I've attached four data files covering our payer revenue performance. Please produce a comprehensive monthly payer revenue review structured as follows:

**Files attached:**
- payer_revenue_monthly.csv — monthly revenue actuals by payer
- payer_contract_summary.csv — contracted rates, minimums, and terms by payer
- revenue_forecast_inputs.csv — forward-looking inputs including pipeline, rate changes, and volume assumptions
- quarterly_metrics_summary.csv — quarterly KPIs across the payer portfolio

**Please deliver the following sections:**

1. **Executive Summary (3–5 bullets):** Top-line revenue performance for the most recent month, variance to target, and one-sentence headline on portfolio health.

2. **Payer-by-Payer Revenue Breakdown:** A table showing each payer's actual revenue for the most recent month, their contracted target or minimum, the dollar and percent variance, and a trend indicator (up/down/flat) based on the prior 2–3 months in payer_revenue_monthly.csv.

3. **At-Risk Payer Identification:** Flag any payers that are (a) below contracted minimums, (b) trending down for 2+ consecutive months, or (c) have contract renewal dates within 90 days combined with underperformance. For each flagged payer, note the specific risk and its revenue exposure.

4. **Revenue Forecast:** Using revenue_forecast_inputs.csv, project expected revenue for the next 1–3 months. Call out any material assumptions (e.g., rate renegotiations, expected volume ramp, seasonal patterns) and provide a range if there is meaningful uncertainty.

5. **Quarterly Context:** Pull in the quarterly_metrics_summary.csv to contextualize monthly trends — are we on track for the quarter? What does the monthly run-rate imply for quarter-end?

6. **Key Themes and Recommended Actions:** Synthesize 3–5 cross-payer themes (e.g., concentrated revenue risk, contract structure issues, volume underperformance) and pair each with a specific recommended action for the commercial team.

Use plain language suitable for an executive audience. Flag any data gaps or inconsistencies you notice across the files. Where relevant, note which specific payers or contract terms are driving portfolio-level trends.
```

---

## Prompt 2: Voice of Customer Cross-Functional Briefing

**Description:** Use this prompt to transform raw qualitative and quantitative customer signal — from call transcripts, Slack summaries, and structured feedback — into a crisp cross-functional briefing. The output maps insights to payer health and routes recommended actions to the right internal teams.

**Files to attach:** `call_transcripts.md`, `slack_call_reports.csv`, `customer_feedback_themes.csv`, `payer_health_scorecard.csv`

```
I'm the Chief Commercial Officer at Headway, a mental health tech company. I've attached four files containing voice of customer (VoC) data from our payer relationships. Please synthesize this into a cross-functional briefing I can share with my leadership team.

**Files attached:**
- call_transcripts.md — transcripts or notes from calls with payer contacts
- slack_call_reports.csv — structured post-call reports logged in Slack by the commercial team
- customer_feedback_themes.csv — categorized feedback themes from payer interactions
- payer_health_scorecard.csv — current health scores and indicators by payer account

**Please deliver the following sections:**

1. **VoC Summary (3–5 bullets):** The most important things our payers are telling us right now — what they're happy with, what's frustrating them, and what they're asking for.

2. **Insight-to-Scorecard Mapping:** For each major theme in customer_feedback_themes.csv, identify which payers in payer_health_scorecard.csv are most affected. Are the payers raising the loudest concerns also the ones with the lowest health scores? Are any high-health-score payers surfacing early warning signals worth monitoring?

3. **Themes by Source:** Break down how themes appear across the three qualitative sources (call transcripts, Slack reports, structured feedback). Note where signals are consistent across sources versus where there is tension or contradiction.

4. **Sentiment by Payer:** Using the call transcripts and Slack reports, give a one-line sentiment read for each payer that appears in the data. Flag any payer where sentiment has shifted notably (e.g., a previously positive payer expressing frustration, or a recovering relationship).

5. **Recommended Actions by Department:** Organize specific, actionable recommendations into four buckets:
   - **Commercial / Account Management** (e.g., relationship escalations, QBR topics, contract conversations)
   - **Product** (e.g., feature requests, workflow friction points, integration asks)
   - **Operations / Network** (e.g., provider access complaints, credentialing delays, billing issues)
   - **Leadership / Executive** (e.g., strategic relationship issues requiring CCO or CEO engagement)

6. **Watch List:** Flag 2–3 payers that require proactive outreach or internal escalation in the next 30 days, with a one-sentence rationale for each.

Be specific — reference actual payer names, quotes, or examples from the source files where they strengthen a point. Flag any themes that appear in qualitative sources but are not yet reflected in the payer health scorecard, as these may indicate lagging indicators worth incorporating.
```
