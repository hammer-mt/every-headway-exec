# Weekly Updates - Week of Feb 24, 2026

---

## Maria Chen - Provider Growth

**Week Summary:**

Great week. We closed 210 new provider signups, putting us at 13,200 active. Texas continues to be our strongest market -- the Houston metro partnership with UT Health is generating warm leads at ~3x our normal conversion rate. Florida softened a bit but still above plan.

Key activities:
- Finalized group practice partnership with Mindful Health Associates (projected 45 new providers by end of March)
- Launched referral bonus program for existing providers -- early uptake looks promising (38 referrals in first 4 days)
- Interviewed 2 candidates for the new Provider Recruiter role in Southeast region

**Blockers:** None major. Would love more marketing budget for the provider referral program -- ROI is looking very strong.

**Next week:** Focus on closing the pipeline in OR ahead of state launch. Targeting 50+ providers credentialed and ready to go.

---

## Derek Williams - Provider Success

things are okay but not great tbh. retention ticked down to 85% which is up from 82% at start of quarter but we lost momentum in feb. main issue is still the aetna reimbursement delays -- providers are waiting 45+ days for payment on some claims and a few have threatened to leave the platform.

talked to priya about it, she's aware and working on it from the insurance ops side.

we also launched the new provider satisfaction survey, got about 40% response rate so far. early results show providers love the patient matching but hate the scheduling interface. passing that feedback to product.

next week: 1:1 calls with top 20 highest-volume providers to make sure they're happy and not at risk of churning.

---

## Sarah Okafor - Market Expansion

### Colorado
- Fully operational since Jan 15. 312 active providers, 2,100+ patients served.
- Payer coverage: UHC, BCBS, Aetna live. Cigna integration pending (tied to national partnership).

### Nevada
- Launched Feb 10. 189 providers onboarded. Ramp is on plan.
- Las Vegas metro is 70% of volume, as expected. Reno picking up.

### Oregon
- Credentialing in progress. 78% of initial cohort (94 of 120 providers) approved by state board.
- Technical integration with Oregon Health Plan (Medicaid) on track for March 10 go-live.
- Remaining 26 providers have documentation gaps -- team is following up individually.

### Outlook
Confident we'll hit 3/3 states by end of Q1. Oregon is the tightest timeline but manageable. Starting to scope Q2 expansion candidates (looking at MN, WI, IA cluster).

---

## Lisa Fernandez - Growth Marketing

Hi all, quick update:

February was a record month. 14,200 new patient signups (vs. 11,800 in Jan). Key drivers:

1. **SEO:** Organic traffic up 18% MoM. New content hub for "therapy for anxiety" keywords is ranking on page 1 for 12 high-volume terms. This is our most efficient acquisition channel by far.

2. **Paid:** Meta campaigns performing well, CPA down to $23 (from $31 in Q4). Google Search campaigns steady. TikTok test is... mixed. Good impressions, low conversion. Might pause.

3. **Partnerships:** Employee wellness channel starting to contribute -- 1,400 signups from employer partnerships this month (Stripe, Shopify, and DoorDash are live).

4. **Referrals:** Patient referral program driving 8% of new signups, up from 5% last month.

Monthly active patients at 98K. Path to 110K depends on retention holding. Working closely with Andre's team.

Concern: CAC is creeping up in competitive markets (NYC, LA, SF). Need to differentiate on brand, not just spend.

---

## Andre Jackson - Patient Experience

### Retention
- 90-day retention at 64%, up from 60% start of quarter
- Drop-off analysis shows sessions 3-4 remain the critical churn point
- New re-engagement nudge sequence launched 2/20: personalized check-in from therapist + educational content about therapy journey expectations
- Too early for results but open rates on nudge emails are 3x our normal patient comms

### NPS
- Rolling NPS at 68, up from 63 in Q4
- Top promoter themes: quality of therapists, ease of booking, insurance coverage
- Top detractor themes: billing confusion (especially EOBs), limited availability for evening/weekend slots
- Action: Working with Priya on simplified billing communications. Kevin's team shipping evening slot expansion feature.

### Patient Safety
- 0 critical safety incidents in Feb
- Launched updated crisis resource integration -- patients now see 988 Suicide & Crisis Lifeline prominently during off-hours
- Provider compliance training completion at 97%

---

## Kevin Cho - Product

Sprint 14 shipped. Sprint 15 underway.

**Shipped:**
- Self-serve rescheduling: rolled out to 80% of patients (remaining 20% on legacy system, migration Sprint 16)
- Provider availability calendar v2: providers can now set recurring schedules with exception dates
- Insurance eligibility real-time check: reduced "surprise" coverage denials by 30%

**In progress:**
- Legacy booking migration (Sprint 16, targeting March 10)
- Therapist matching algorithm v3: incorporating patient preference weighting and availability optimization
- Evening/weekend slot expansion (tied to Andre's retention work)

**Upcoming:**
- Cigna integration (Sprint 17, dependent on their API timeline)
- Provider mobile app v2 planning starting next week

No major technical risks. Team velocity is good at 42 pts/sprint (up from 36 in Q4).

---

## Priya Mehta - Insurance Ops

Claim denial rate: 5.8% (down from 8% start of quarter)

Highlights:
- Pre-submission validation engine caught 2,340 errors in February before claims went out
- Most common prevented errors: wrong CPT codes (41%), missing prior auth references (28%), incorrect member IDs (19%)
- CPT code training module for providers goes live March 3 -- expecting meaningful impact on remaining denial rate

Claim processing time: 28 days average
- UHC: 18 days (great)
- BCBS: 20 days (good)
- Aetna: 38 days (problematic -- they require manual clinical review on 30% of mental health claims)
- Working on getting Aetna to accept our clinical documentation format to skip manual review. Meeting scheduled March 5.

New payer integration:
- Cigna technical integration 40% complete. Their API documentation is... not great. Lots of back and forth.
- Estimated go-live: April 1 (was March 15, slipped due to Cigna responsiveness)

---

## Tom Nguyen - Engineering Infrastructure

uptime: 99.91% in february

incidents:
- 2/12: 45 min outage on booking service. root cause was DB failover that didn't promote the replica correctly. fixed the failover script and added automated testing for failover scenarios.
- 2/22: 20 min payment processing delay. third party gateway (Stripe) had a partial outage. we didn't detect it fast enough because our health check was only pinging the endpoint, not doing transactional checks. fixed.

MTTR: 32 min average (down from 45 min start of quarter). the 2/12 incident brought the average up. without it we'd be at 22 min.

working on:
- circuit breakers for all external service dependencies (stripe, payer APIs, twilio)
- chaos engineering framework -- want to start running game days monthly
- evaluating move from RDS to Aurora for the booking database. could improve failover time to <30 seconds.

---

## Omar Hassan - Data Engineering

Not a great update this week honestly.

The OKR dashboard is behind schedule. We have the data model ~70% done but we're stuck on metric definitions. Finance and ops teams have different definitions for "active patient," "revenue recognized," and "provider retention." I've scheduled a metric alignment meeting for March 3 with Nina, Derek, and Lisa to get consensus. Until that's resolved I can't finalize the dashboard.

On the pipeline latency work -- we migrated claims processing, session booking, and patient signup pipelines to streaming. Those are now under 2 hours. But the remaining 5 pipelines all depend on batch data feeds from insurance partners (they send us files overnight, not real-time data). Getting them to provide real-time APIs is a business negotiation, not a technical problem. Rob -- would appreciate your help pushing on this with the payer partners.

Patient journey instrumentation: 7 of 10 events done. The last 3 are harder because they span multiple services. Should be done by end of next week.

---

## Diana Reeves - Analytics

February cohort retention report delivered to leadership on 2/28. Key findings:

- Patients referred through employer wellness programs retain at 78% (90-day), significantly above the 64% average
- Patients matched with their first-choice therapist retain at 71% vs. 58% for those who got second/third choice
- Insurance type matters: commercially insured patients retain better (69%) than Medicaid (54%)
- Evening appointment slots have 22% lower no-show rates

Recommendations shared with Andre (patient experience) and Lisa (growth marketing) to inform targeting and matching.

March report will add therapist-matching quality as a new dimension. Working with Kevin's team to get matching algorithm v3 data instrumented.

Also started ad hoc analysis on claim denial impact on retention -- preliminary data suggests patients who experience a claim denial in their first 60 days are 2.3x more likely to churn. Sharing with Priya and Rob.

---

## Rachel Kim - Engineering Platform

Bug backlog update: down to 18 P0/P1s from 34 at start of quarter. February bug bash cleared 8 issues.

Remaining P0s (4):
1. Insurance eligibility check timeout on high-latency payer connections (intermittent)
2. Duplicate appointment creation race condition (rare but high impact)
3. Provider payment calculation rounding error for split-session billing
4. Patient record merge failing for accounts created before 2024 migration

Remaining P1s (14): mix of UI inconsistencies, edge cases in scheduling logic, and some analytics tracking gaps.

Deployment frequency: averaging 3x/week. CI/CD improvements from Jan are paying off. Feature flags working well -- 12 flags active right now. Main bottleneck to going daily is QA review time for HIPAA-sensitive changes. Exploring automated compliance checking to unblock this.

Next week: focused sprint on the 4 remaining P0s. Goal is to close at least 2.
