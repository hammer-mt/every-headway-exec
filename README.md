# Headway x Every — Executive AI Offsite

Materials for the March 4, 2026 hands-on AI building day. Each executive has a folder with synthetic data and ready-to-use prompts for the projects they brainstormed.

## Quick Start

1. Open [Claude](https://claude.ai) or [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
2. Go to your folder below
3. Open `example_prompts.md` — pick a prompt, paste it into Claude along with the referenced data files
4. Build something

---

## Your Folders

### RS — Rob Sadow (VP Strategy / Ops)

**Project: OKR Tracking & Review Automation**

Automate the weekly process of collecting team updates, drafting OKR status changes, and surfacing risks for leadership.

| File | What it is |
|------|-----------|
| `okr_tracker.csv` | Central OKR spreadsheet — 20 key results across 5 objectives |
| `weekly_updates_raw.md` | Raw weekly updates from 10 team leads (varied formats, just like real life) |
| `jira_export.csv` | 32 Jira tickets mapped to specific OKRs |
| `example_prompts.md` | 4 ready-to-use prompts, from basic analysis to full executive briefing |

---

### NC — Neha Chaudhary (Chief Medical Officer)

**6 projects** spanning clinical operations, safety, and thought leadership.

| File | Project | What it is |
|------|---------|-----------|
| `sample_prd.md` | Clinical PRD Review | A product requirements doc with deliberate clinical review flags |
| `clinical_review_rubric.csv` | Clinical PRD Review | 8-dimension scoring rubric (safety, evidence base, risk, etc.) |
| `safety_plan_template.json` | AI Safety Planning | Complete patient safety plan template with example data |
| `crisis_resources.csv` | AI Safety Planning | 16 crisis hotlines and resources |
| `patient_session_data.csv` | Provider Copilot | 63 session records across 10 patients with varied trajectories |
| `clinical_triggers.csv` | Provider Copilot | 12 clinical trigger rules (e.g., "no improvement after 6 sessions") |
| `news_feed_sample.csv` | Thought Leadership | 25 mental health industry news items |
| `internal_updates.csv` | Thought Leadership | 15 internal Headway launches and milestones |
| `risk_register.csv` | Risk Register | 15 clinical/compliance/regulatory risks |
| `regulatory_news_feed.csv` | Risk Register | 20 recent regulatory and legal news items |
| `patient_outcomes.csv` | Outcomes Dashboard | 81 rows of outcomes data sliced by plan, state, demographics |
| `benchmark_data.csv` | Outcomes Dashboard | 15 published industry benchmarks for comparison |
| `example_prompts.md` | All | 6 prompts — one per project |

---

### LB — Lorraine Buhannic (Chief People Officer)

**3 projects** covering recruiting, compensation, and people analytics.

| File | Project | What it is |
|------|---------|-----------|
| `open_roles.csv` | Candidate Sourcing | 12 open roles across departments |
| `employee_directory.csv` | Candidate Sourcing | 40 employees with backgrounds for referral matching |
| `candidate_pipeline.csv` | Candidate Sourcing | 25 candidates at various pipeline stages |
| `comp_bands.csv` | Offer Analysis | Internal compensation bands (IC1-IC6, M1-M3) |
| `market_data.csv` | Offer Analysis | Radford-style market comp data for 20 roles |
| `recent_offers.csv` | Offer Analysis | 15 recent offers — acceptance/decline patterns |
| `headcount_data.csv` | People Analytics | 59 employees with performance, engagement, flight risk |
| `recruiting_funnel.csv` | People Analytics | 6 months of recruiting funnel data |
| `attrition_log.csv` | People Analytics | 10 recent departures with exit reasons |
| `example_prompts.md` | All | 3 prompts — one per project |

---

### OMD — Olivia Millard Davis (Chief Commercial Officer)

**2 projects** focused on payer relationships and revenue.

| File | Project | What it is |
|------|---------|-----------|
| `payer_revenue_monthly.csv` | Revenue Review | 6 months of revenue data across 10 payers |
| `payer_contract_summary.csv` | Revenue Review | Contract terms and targets for each payer |
| `revenue_forecast_inputs.csv` | Revenue Review | 3-month forward projections for top 5 payers |
| `quarterly_metrics_summary.csv` | Revenue Review | 4 quarters of company-wide KPIs |
| `call_transcripts.md` | Voice of Customer | 6 payer call summaries (expansion, escalation, review) |
| `slack_call_reports.csv` | Voice of Customer | 19 structured call reports from Slack |
| `customer_feedback_themes.csv` | Voice of Customer | 12 aggregated feedback themes across payers |
| `payer_health_scorecard.csv` | Voice of Customer | Relationship health scores for 10 payers |
| `example_prompts.md` | All | 2 prompts — one per project |

---

### MT — Mike Taylor (Facilitator / Demo)

**5 demo projects** showing what's possible — used during the guided build session.

| File | Project | What it is |
|------|---------|-----------|
| `nps_and_descriptions_only.csv` | NPS Dashboard | NPS survey data with scores and open-ended subscriber descriptions |
| `every-landing.html` | Landing Page | Landing page for "Learn Claude Code in One Day" |
| `hoboken-hidden-gems.html` | Hidden Gems Guide | Interactive local guide to Hoboken with map, filters, and recommendations |
| `therapists-db.js` | Therapist Directory | JavaScript database of 132 therapist records (specialties, insurance, bios, etc.) |
| `therapists-index.html` | Therapist Directory | Search/browse page for finding family counselors in New York |
| `therapists-provider.html` | Therapist Directory | Individual therapist detail page |
| `example_prompts.md` | All | 5 prompts — NPS dashboard, landing page mod, vacation guide, directory feature, workforce analysis |

---

## Examples — Extending Claude

The `examples/` folder has three beginner-friendly templates for going beyond basic prompting. Each one has its own README with plain-English explanations and step-by-step install instructions.

### [`examples/claude-code-skill/`](examples/claude-code-skill/)

**What it is:** A reusable prompt you invoke with a slash command (like `/weekly-summary`). Think of it as a saved recipe — Claude follows the same steps every time.

**When to use it:** You find yourself pasting the same kind of prompt over and over. Save it as a skill instead.

### [`examples/subagent/`](examples/subagent/)

**What it is:** A specialized AI worker that Claude can delegate tasks to automatically. Like a manager assigning a subtask to a team member who works independently and reports back.

**When to use it:** Your task has multiple independent parts that could be worked on in parallel (e.g., "check data quality on all my files while I work on the analysis").

### [`examples/mcp-server/`](examples/mcp-server/)

**What it is:** A plugin that connects Claude to external tools and data. Just like your phone has apps that give it new abilities, MCP servers give Claude new abilities (search databases, call APIs, read spreadsheets).

**When to use it:** You want Claude to pull live data from your systems instead of copy-pasting files into the chat.

---

## Important Notes

- All data in this repo is **synthetic** — realistic but entirely made up. No real patient, employee, or financial data.
- The `exec_ideas/` folder (containing the original brainstorming docs) is gitignored and not included in this repo.
- Each folder's `example_prompts.md` has copy-paste-ready prompts. Start there.
