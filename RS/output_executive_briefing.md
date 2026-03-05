# Weekly Executive Briefing

**Subject:** Weekly OKR Briefing — Week of March 2, 2026

---

Team,

We are entering the final four weeks of Q1 with 20 key results across 5 objectives. Nine KRs are On Track, four are At Risk, and four are Behind. The portfolio is making meaningful progress on provider growth, patient acquisition, and claims operations, but revenue pace, provider retention, and a few data/infrastructure targets need leadership focus before quarter-end.

---

## This Week's Highlights

- **Record patient acquisition month.** February closed with 14,200 new patient signups (vs. 11,800 in January), driven by a strong SEO content push and paid media efficiency gains (CPA down to $23 from $31 in Q4). Monthly active patients now at 98,000 against a 110,000 target.

- **Provider network at 13,200 — 88% to target.** 210 new providers signed last week. The UT Health partnership in Houston is converting at 3x normal rates, and a new group practice deal with Mindful Health Associates projects an additional 45 providers by end of March. Provider referral program launched with 38 referrals in its first four days.

- **Claim denial rate cut to 5.8%.** The pre-submission validation engine prevented 2,340 claim errors in February. The CPT code training module for providers launches March 3, which should drive the next meaningful reduction toward the 4% target.

- **Oregon launch on track for mid-March.** 78% of the initial provider cohort (94 of 120) is credentialed. Oregon Health Plan Medicaid integration is targeting March 10 go-live. Colorado and Nevada are fully operational (312 and 189 active providers, respectively).

- **Cohort analysis surfacing actionable insights.** Diana Reeves's February retention report shows employer wellness referrals retain at 78% (vs. 64% average), and first-choice therapist matches retain at 71% vs. 58% for alternatives. Patients who experience a claim denial in their first 60 days are 2.3x more likely to churn — a direct link between claims operations and patient retention.

---

## Areas Requiring Attention

- **Revenue run-rate is $24.5M against a $28M target (At Risk).** Owner: Nina Kowalski, Finance. The gap is driven by a slower Cigna ramp (go-live slipped from March 15 to April 1 per Priya's update) and lower January session volume. March needs to be a very strong collections month to close this gap. *Suggested action: Identify levers for accelerating session volume in March, and pressure-test the revised Cigna ramp timeline with the integration team.*

- **Provider onboarding time stuck at 17 days vs. 14-day target (Behind).** Owner: James Patel, Provider Ops. This KR has not been updated since February 7 and no update was submitted this week. *Suggested action: Request an immediate status update from James and determine whether the target is still achievable this quarter.* [NOTE: No weekly update was received from James Patel; the absence of activity is itself a flag.]

- **Executive OKR dashboard blocked and at risk of slipping to April (Behind).** Owner: Omar Hassan, Data Engineering. Jira ticket HW-1101 (metric definition alignment) is in Blocked status. A cross-functional alignment meeting is scheduled for March 3 with Finance and Ops. Frontend build (HW-1102) has not started. *Suggested action: Ensure the March 3 metric alignment session is decisive — assign a single decision-maker for contested definitions so the team can unblock immediately.*

- **Platform uptime at 99.91% vs. 99.95% target (At Risk).** Owner: Tom Nguyen, Engineering Infra. Two incidents in February (45-min booking outage on 2/12, 20-min payment delay on 2/22) pulled the number down. Circuit breakers and an Aurora database migration POC are in progress. *Suggested action: Confirm the circuit breaker rollout timeline and evaluate whether March can realistically recover the uptime number given the February deficit.*

---

## On Track and Progressing

Several KRs are in strong shape heading into the final month. Patient NPS is at 68 and trending toward the 72 target, buoyed by reduced first-appointment wait times (3.2 days average). Self-serve rescheduling is live for 80% of patients with the legacy migration scheduled for Sprint 16 (March 10). The P0/P1 bug backlog has been cut from 34 to 18, with a focused sprint on the remaining four P0s starting next week. Deployment frequency is up to 3x/week with CI/CD and feature flag improvements paying dividends. Claim processing time is down to 28 days average, with UHC and BCBS already under the 21-day target — Aetna remains the outlier at 38 days. The patient journey instrumentation effort has 7 of 10 events live, with the remaining three expected by end of next week.

---

## Recommended Discussion Topics for Leadership Review

1. **Kaiser partnership escalation.** Conversations with Kaiser have stalled and we are unlikely to close this quarter. Should we formally escalate to an exec-to-exec conversation, or redirect effort toward Centene as a replacement for the Molina slot? This decision affects whether we report 2 or 3 new partners for Q1.

2. **Aetna relationship management.** Aetna's 38-day claim processing time and 45+ day reimbursement delays are creating downstream problems across at least three KRs (provider retention, revenue, and claim processing time). A meeting with Aetna is set for March 5 to discuss accepting our clinical documentation format. Should we elevate this to a broader commercial conversation about the partnership terms?

3. **Patient retention drop-off at sessions 3-4.** With 90-day retention at 64% and the pace of improvement slowing, should we greenlight additional investment in the therapist matching algorithm v3 and evening/weekend slot expansion to accelerate progress before quarter-end? Diana's data showing the retention lift from first-choice therapist matches (71% vs. 58%) suggests the matching work could have outsized impact.

---

Next update will be distributed the week of March 9. Please flag any corrections or additional context by EOD Wednesday.

Rob Sadow
VP Strategy & Operations
