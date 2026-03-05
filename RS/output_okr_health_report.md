# OKR Health Report — Q1 2026

**Prepared:** March 4, 2026
**Data Sources:** OKR Tracker (last updated Feb 28), Jira Export (34 tickets), Weekly Team Updates (week of Feb 24)

---

## 1. Executive Summary

Headway is tracking 20 Key Results across 5 Objectives for Q1 2026. Of these, 11 KRs (55%) are On Track, 4 (20%) are At Risk, and 5 (25%) are Behind. Provider network growth, claim denial reduction, and deployment velocity are standout areas of momentum. The most concerning gaps are in insurance partner acquisition (1 of 4 partners signed with Kaiser stalled and Molina deprioritized), the executive OKR dashboard (blocked on metric alignment), and data pipeline latency (dependent on payer negotiations outside our control). Revenue is At Risk at $24.5M against a $28M target, driven by slow Cigna ramp and a soft January. March is a make-or-break month for several KRs, and any slippage on the Oregon launch, Humana LOI, or legacy booking migration could push additional KRs off track.

---

## 2. Objective-by-Objective Breakdown

### Objective 1: Expand Provider Network to 15K Active Therapists
**Key Results:** 4 | **Average Progress:** 72%

| Key Result | Current | Target | Status | Jira Tickets |
|---|---|---|---|---|
| Grow active provider base to 15K | 13,200 | 15,000 | On Track | 0 |
| Increase provider retention to 90% | 85% | 90% | At Risk | 0 |
| Launch in 3 new states (CO, NV, OR) | 2/3 | 3 | On Track | 2 (both In Progress) |
| Reduce onboarding time to 14 days | 17 days | 14 days | Behind | 0 |

**Assessment:** Provider growth is the strongest performer in this objective -- Maria Chen's team added 840 providers in February and has healthy pipeline through partnerships and referral programs. The state expansion is on track with CO and NV live; Oregon is tight but the team is managing credentialing gaps actively (2 Jira tickets tracking Oregon-specific work). Two KRs are weak: provider retention stalled at 85% due to Aetna reimbursement delays, and onboarding time has not been updated since Feb 7 and remains 3 days over target with no Jira activity, suggesting it lacks dedicated execution focus.

---

### Objective 2: Increase Patient Engagement and Retention
**Key Results:** 4 | **Average Progress:** 73%

| Key Result | Current | Target | Status | Jira Tickets |
|---|---|---|---|---|
| Increase monthly active patients to 110K | 98,000 | 110,000 | On Track | 0 |
| Improve 90-day retention to 72% | 64% | 72% | At Risk | 2 (1 In Progress, 1 To Do) |
| Achieve patient NPS of 72+ | 68 | 72 | On Track | 0 |
| Launch self-serve rescheduling (100%) | 80% | 100% | On Track | 2 (1 In Progress, 1 To Do) |

**Assessment:** Patient acquisition is strong with February delivering a record 14,200 signups, but the path to 110K monthly actives depends on retention holding. The 90-day retention KR improved 4 points since Q4 but the pace is slowing, and the remaining gap (64% to 72%) is steep for one month. Two Jira tickets (therapist matching v3, evening slot expansion) are directly targeting the retention problem. NPS is trending well at 68 with billing confusion as the top detractor. Self-serve rescheduling has clear execution path via the legacy migration in Sprint 16.

---

### Objective 3: Deepen Insurance Partnerships and Revenue
**Key Results:** 4 | **Average Progress:** 53%

| Key Result | Current | Target | Status | Jira Tickets |
|---|---|---|---|---|
| Add 4 new insurance partners | 1/4 | 4 | Behind | 3 (1 In Progress, 2 To Do) |
| Increase gross revenue to $28M run-rate | $24.5M | $28M | At Risk | 0 |
| Reduce claim denial rate to 4% | 5.8% | 4% | On Track | 3 (2 In Progress, 1 Done) |
| Reduce claim processing time to 21 days | 28 days | 21 days | On Track | 0 |

**Assessment:** This is the weakest objective overall. The insurance partner KR is significantly behind -- only Cigna is signed (with integration slipping to April 1 from March 15), Kaiser conversations have stalled requiring executive escalation, Molina was deprioritized, and Humana LOI is not expected until mid-March. Revenue is tracking $3.5M below the $28M target with one month remaining. The bright spot is claim operations: denial rate dropped from 8% to 5.8% with a CPT training module launching March 3 that could drive further reduction, and processing time is improving with UHC and BCBS already under the 21-day target. Aetna remains a significant outlier at 38 days.

---

### Objective 4: Improve Platform Reliability and Developer Velocity
**Key Results:** 4 | **Average Progress:** 72%

| Key Result | Current | Target | Status | Jira Tickets |
|---|---|---|---|---|
| Achieve 99.95% uptime | 99.91% | 99.95% | At Risk | 3 (1 In Progress, 1 To Do, 1 Done) |
| Reduce MTTR to 20 min | 32 min | 20 min | On Track | 2 (1 In Progress, 1 Done) |
| Increase deploys to daily | 3x/week | 5x/week | On Track | 2 (1 In Progress, 1 Done) |
| Reduce P0/P1 bug backlog to <10 | 18 | 10 | On Track | 4 (2 In Progress, 2 To Do) |

**Assessment:** This objective has solid execution momentum. The bug backlog is down from 34 to 18 with all 4 remaining P0s tracked in Jira for Sprint 16. Deployment frequency improved from 2x to 3x/week with CI/CD and feature flag improvements; automated HIPAA compliance checking (in progress) could unblock the push to daily. Uptime is the concern -- two incidents in February (booking outage, payment delay) dropped it to 99.91%, and closing a 0.04% gap in March requires zero significant outages. Circuit breaker work is in progress to mitigate third-party risks.

---

### Objective 5: Scale Data and Analytics Capabilities
**Key Results:** 4 | **Average Progress:** 52%

| Key Result | Current | Target | Status | Jira Tickets |
|---|---|---|---|---|
| Launch executive OKR dashboard | Not launched | 1 | Behind | 3 (1 In Progress, 1 Blocked, 1 To Do) |
| Instrument top 10 patient journey events | 7/10 | 10 | On Track | 3 (1 In Progress, 2 To Do) |
| Deliver monthly cohort retention analysis | 2/3 | 3 | On Track | 0 |
| Reduce pipeline latency to <4hr | 12 hrs | 4 hrs | Behind | 4 (1 In Progress, 3 Done) |

**Assessment:** This objective has the lowest average progress. The OKR dashboard is the most visibly stalled KR across the entire OKR set -- it has a blocked Jira ticket (HW-1101, metric definition alignment), the frontend build has not started, and Omar Hassan flagged in his weekly update that it may slip to April. Pipeline latency work completed the technically feasible migrations (3 of 8 pipelines now streaming), but the remaining 5 depend on payer partners providing real-time API access, making this a business negotiation problem. Diana Reeves' cohort analysis work is a quiet win -- delivering on time with increasingly valuable segmentation.

---

## 3. Execution Signal from Jira

### Most Active KRs (by ticket count)
| Key Result | Total Tickets | In Progress | Done | To Do | Blocked |
|---|---|---|---|---|---|
| Reduce P0/P1 bug backlog to <10 | 4 | 2 | 0 | 2 | 0 |
| Reduce data pipeline latency to <4hr | 4 | 1 | 3 | 0 | 0 |
| Reduce claim denial rate to 4% | 3 | 2 | 1 | 0 | 0 |
| Launch executive OKR dashboard | 3 | 1 | 0 | 1 | 1 |
| Add 4 new insurance partners | 3 | 1 | 0 | 2 | 0 |
| Achieve 99.95% uptime | 3 | 1 | 1 | 1 | 0 |
| Instrument top 10 patient journey events | 3 | 1 | 0 | 2 | 0 |

### KRs with Zero Jira Activity
The following KRs have **no Jira tickets** and may lack structured execution plans:

1. **Grow active provider base to 15K** -- Strong progress (13,200/15,000) driven by Maria Chen's team, but no tickets tracking the work. Execution appears to happen outside Jira (recruitment campaigns, partnerships).
2. **Increase provider retention to 90%** -- At Risk and no tickets. Derek Williams' update focuses on reactive measures (1:1 calls with top providers) rather than systematic initiatives.
3. **Reduce provider onboarding time to 14 days** -- Behind and no tickets. Last updated Feb 7. This KR appears orphaned.
4. **Increase monthly active patients to 110K** -- On Track via marketing channels, which likely operate outside Jira.
5. **Achieve patient NPS of 72+** -- On Track. Driven by cross-functional improvements rather than dedicated tickets.
6. **Increase gross revenue to $28M run-rate** -- At Risk. Revenue is an outcome metric without direct Jira-trackable work.
7. **Reduce claim processing time to 21 days** -- On Track. Improvements driven by automation and payer-side work, not tracked in Jira.
8. **Deliver monthly cohort retention analysis** -- On Track. Analytics work may be tracked in a different system.

### Blocked Tickets
- **HW-1101** (OKR dashboard metric definition alignment): Blocked on cross-functional agreement between Finance, Ops, and Growth on definitions for "active patient," "revenue recognized," and "provider retention." Meeting scheduled March 3. This is the only formally blocked ticket and it is gating the entire OKR dashboard KR.

---

## 4. Top 3 Risks

### Risk 1: Add 4 New National Insurance Partners — 1 of 4 signed, closing Q1 at best 2
- **Tracker:** Status is Behind. Only Cigna is signed. Kaiser stalled, Molina deprioritized, Humana LOI not expected until mid-March.
- **Jira:** 3 tickets, all Cigna-related. No tickets for Humana, Kaiser, or alternative pipeline. Cigna integration slipped from March 15 to April 1.
- **Team Leads:** Rob Sadow's update notes Kaiser needs executive escalation. Priya Mehta confirms Cigna's API documentation is causing delays. Even if Humana signs an LOI in March, integration would extend well into Q2.
- **Impact:** This KR will almost certainly miss target. Realistic Q1 outcome is 1 signed (Cigna) with Humana as a possible LOI. This directly impacts the revenue KR.

### Risk 2: Increase Gross Revenue to $28M Quarterly Run-Rate — $3.5M gap with 1 month remaining
- **Tracker:** At Risk at $24.5M. Gap attributed to slow Cigna ramp and low January session volume.
- **Jira:** No dedicated tickets. Revenue is a lagging indicator dependent on multiple other KRs (insurance partners, patient volume, claim processing).
- **Team Leads:** Nina Kowalski notes March pipeline "looks strong" but acknowledges the size of the gap. Lisa Fernandez's record acquisition month helps, but revenue recognition lags patient signups.
- **Impact:** Closing a $3.5M gap in one month requires roughly a 43% increase over the February run rate. This is extremely unlikely. The Cigna delay (now April 1 go-live) removes a potential revenue driver from Q1 entirely.

### Risk 3: Launch Executive OKR Dashboard — Blocked, may slip to April
- **Tracker:** Behind. Data model 70% complete. Last updated Jan 31.
- **Jira:** 1 ticket blocked (metric definitions), 1 in progress (data model), 1 not started (frontend). Three sequential dependencies with the first one blocked.
- **Team Leads:** Omar Hassan explicitly called this out as at risk of slipping to April. The blocker is organizational (metric definitions across Finance, Ops, and Growth teams disagree on fundamental terms) rather than technical.
- **Impact:** This KR will almost certainly miss Q1. A metric alignment meeting is set for March 3, but even if it resolves quickly, the frontend build (8 story points, Sprint 17) cannot start until the data model is finalized, making a March delivery unrealistic.

---

## 5. Top 3 Wins

### Win 1: Provider Network Growth — 13,200 of 15,000 (88% to target)
Maria Chen's team is executing at a high level. February added 840 providers with recruitment campaigns running 12% above target CPA. The UT Health partnership in Houston is delivering 3x normal conversion rates. A new referral bonus program generated 38 referrals in its first 4 days. The Mindful Health Associates group practice partnership projects 45 additional providers by end of March. At the current trajectory, this KR should close at or above 15,000.

### Win 2: Claim Denial Rate Reduction — 5.8% down from 8% (69% of the way to 4% target)
Priya Mehta's pre-submission validation engine caught 2,340 errors in February alone, preventing the three most common denial causes (wrong CPT codes, missing prior auth, incorrect member IDs). A provider CPT code training module launches March 3, targeting the largest remaining error category (41% of prevented errors were CPT-related). This KR has strong Jira execution (3 tickets, 1 completed, 2 in progress) and clear line of sight to further improvement.

### Win 3: P0/P1 Bug Backlog Reduction — 18 down from 34 (67% of the way to <10)
Rachel Kim's team cut the backlog nearly in half through dedicated bug bash sprints in January and February. All 4 remaining P0 bugs are individually identified and tracked in Jira for Sprint 16, with a focused sprint planned to close at least 2 next week. The 14 remaining P1s are lower-severity edge cases. This KR has the clearest execution plan of any in the set and strong probability of hitting or approaching the target.

---

*End of report.*
