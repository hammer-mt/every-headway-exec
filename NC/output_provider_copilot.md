# Provider Copilot — Intervention Analysis

> **Generated:** 2026-03-04 | **Purpose:** Internal product evaluation (not for direct clinical use) | **Cohort:** 10 patients, 63 total sessions

---

## Prioritized Intervention List

| Patient ID | Trigger(s) Fired | Severity | Recommended Action | Days Since Last Session |
|:----------:|:-----------------|:--------:|:-------------------|:-----------------------:|
| PT-1004 | **TRG-002** Severe Depression Score, **TRG-001** No Symptom Improvement, **TRG-007** Treatment Plateau, **TRG-012** Risk Factor Cluster | **Critical** | Immediate clinical attention. PHQ-9 has remained at 20-22 across 7 sessions with essentially zero improvement (2-point change from baseline). Severe score + missed appointment triggers the risk factor cluster. IOP referral already submitted and bupropion augmentation added at last session, but no follow-up has occurred in 98 days. **Combination escalation:** The convergence of TRG-002 (severe score), TRG-001 (no improvement), and TRG-007 (plateau) with TRG-012 (risk cluster) warrants urgent outreach. This patient should be re-contacted immediately to confirm IOP intake occurred and to conduct a safety reassessment. Consider whether a higher level of care (PHP or inpatient evaluation) is now appropriate given the extended gap without contact. | 98 |
| PT-1009 | **TRG-009** Substance Use Escalation | **High** | Patient reports increased alcohol use on weekends as of session 4. Scores have worsened every session (15 to 18) with no improvement trajectory. Administer AUDIT-C screening at next session. Assess interaction with any future medications. Consider integrated treatment or referral to substance use specialist. Coordinate with psychiatrist (referral already noted). Note: Although only 4 sessions have elapsed (below the 6-session threshold for TRG-001), the unbroken worsening trend is clinically concerning and the 81-day gap since last contact warrants priority outreach. | 81 |
| PT-1006 | **TRG-005** Missed Appointments | **Moderate** | Two missed appointments documented within a 4-session window. Patient has expressed ambivalence about therapy and scores are trending slightly upward (worsening: 10 to 11). Engagement outreach is indicated. Contact patient to assess barriers, explore ambivalence, and consider scheduling flexibility or telehealth. The 75-day gap since last session suggests possible disengagement or dropout. | 75 |

### Patients with No Triggers Fired

| Patient ID | Diagnosis | Assessment | Baseline | Latest | Sessions | Days Since Last Session | Status |
|:----------:|:----------|:----------:|:--------:|:------:|:--------:|:-----------------------:|:-------|
| PT-1001 | MDD Recurrent Moderate | PHQ-9 | 18 | 6 | 8 | 75 | Steady improvement; transitioned to mild range. Relapse prevention phase. |
| PT-1002 | Generalized Anxiety Disorder | GAD-7 | 16 | 9 | 9 | 92 | Improved with combined CBT + buspirone. Now in mild range. |
| PT-1003 | PTSD | PCL-5 | 52 | 28 | 6 | 84 | Strong CPT response; nightmares and avoidance significantly reduced. |
| PT-1005 | Social Anxiety Disorder | GAD-7 | 14 | 7 | 7 | 105 | Good ACT response; moved from moderate to mild range. |
| PT-1007 | GAD (perinatal) | GAD-7 | 12 | 5 | 6 | 100 | Near remission; transitioned to maintenance. |
| PT-1008 | ADHD Inattentive | ASRS | 4.2 | 2.8 | 5 | 79 | Improving with medication + skills; strategies becoming habitual. |
| PT-1010 | GAD (test anxiety) | GAD-7 | 18 | 7 | 6 | 80 | Significant improvement; completed finals without panic. |

---

## Data Gaps

The following triggers could not be fully evaluated because the required data fields are missing or incomplete in `patient_session_data.csv`:

| Trigger | Required Data | What Is Available | Impact |
|:--------|:--------------|:------------------|:-------|
| **TRG-003** Suicidal Ideation Endorsed | PHQ-9 Item 9 score (individual item-level response) | Only the composite PHQ-9 total score is recorded | **Cannot evaluate at all.** This is the highest-impact gap: a Critical-severity trigger for active suicidal ideation is completely blind. Item-level PHQ-9 data should be a priority addition. |
| **TRG-005** Missed Appointments | Structured missed-appointment count or no-show flag per scheduled session | Missed appointments are only mentioned incidentally in free-text session notes | **Partially evaluable.** Sensitivity depends on whether the provider mentions the missed session in their notes. Sessions that were scheduled but never occurred (and never referenced in a subsequent note) are invisible. A dedicated attendance/no-show field is needed. |
| **TRG-006** Medication Non-Adherence Signal | Structured medication adherence field or standardized adherence screening | Only free-text session notes are available for keyword detection | **Partially evaluable.** Detection relies on providers documenting non-adherence in their notes using recognizable language. Under-reporting is likely. |
| **TRG-009** Substance Use Escalation | Structured substance use screening scores (e.g., AUDIT-C, DAST-10) | Only free-text session notes are available | **Partially evaluable.** Same free-text limitation as TRG-006. Standardized screening instrument scores would improve reliability. |
| **TRG-001, 002, 004, 007, 008, 010, 011** (all score-based triggers) | PHQ-9 or GAD-7 scores | PCL-5 (PT-1003) and ASRS (PT-1008) are used for 2 of 10 patients | **Not evaluable for 20% of cohort.** The trigger definitions only reference PHQ-9 and GAD-7. Patients assessed with PCL-5 (PTSD) or ASRS (ADHD) fall outside the trigger set entirely, creating a monitoring blind spot for those diagnoses. |

---

## Cohort Interpretation

This 10-patient cohort reveals a trigger set that is reasonably specific but has meaningful sensitivity gaps. Only 3 of 10 patients fired any triggers, and in each case the alert appears clinically warranted: PT-1004 is a genuinely treatment-resistant case with a dangerous gap in follow-up, PT-1009 shows an unbroken worsening trajectory compounded by emerging substance use, and PT-1006 is showing early signs of disengagement. The triggers correctly left alone the 7 patients who are improving or in remission, suggesting low false-positive rates for the conditions they cover. However, the trigger set is blind to two important dimensions: it cannot detect suicidal ideation (TRG-003) without item-level PHQ-9 data, and it has no coverage at all for patients assessed with PCL-5 or ASRS, meaning 20% of this cohort is entirely unmonitored. The reliance on free-text notes for missed appointments, medication adherence, and substance use creates a systemic under-detection risk that would grow with scale. Expanding the trigger definitions to include PCL-5 and ASRS thresholds, adding structured data fields for attendance and adherence, and capturing item-level assessment responses would substantially improve both the sensitivity and the clinical utility of the copilot system.
