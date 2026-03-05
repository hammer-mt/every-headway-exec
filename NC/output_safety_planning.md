# AI Safety Planning Workflow

## Section 1: Clinician Prompts — Mapping Template Fields to Provider Questions

Each numbered item below maps a field (or group of fields) from the `safety_plan_template.json` to the exact language a provider would use to elicit that information from a patient. Prompts follow the Stanley-Brown collaborative model: open-ended first, then specific.

### Patient Info

1. **preferred_name** — "What name would you like me to use with you during our sessions?"
2. **primary_diagnosis / secondary_diagnosis** — *(Populated by provider from clinical assessment; not elicited via prompt.)*
3. **current_medications** — "Can you walk me through the medications you are currently taking — the name, how much you take, and how often?"

### Step 1 — Warning Signs

4. **warning_signs (thought)** — "When things start to get really hard, what kinds of thoughts tend to show up? For example, thoughts about yourself, your worth, or your place in other people's lives."
5. **warning_signs (behavior)** — "Are there things you start doing, or stop doing, that would tell someone close to you that you're heading into a rough patch? Things like pulling away from people, changes in sleep, eating, or substance use?"
6. **warning_signs (image)** — "Sometimes people experience intrusive mental pictures or daydreams when they are struggling. Does anything like that happen for you? Can you describe what you see?"
7. **warning_signs (mood)** — "Are there shifts in how you feel emotionally that signal things are getting worse? For instance, a sudden numbness, a wave of hopelessness, or an unexpected calm after a long stretch of pain?"
8. **warning_signs (category assignment)** — "For each sign we just listed, let's label it: is it a thought, a feeling, a behavior, or an image? That will help us both recognize patterns faster."

### Step 2 — Coping Strategies (Internal)

9. **strategies (activity)** — "Let's think about things you can do completely on your own, without needing to reach anyone else, that help you feel even a little bit better or take your mind off the pain. What has worked before, even once?"
10. **strategies (effectiveness_rating)** — "On a scale of 1 to 5, where 5 means 'this reliably helps,' how effective is each of these strategies for you?"
11. **strategies (notes / conditions)** — "Are there any conditions that make this strategy work better or worse? For example, time of day, location, or something you need to have on hand?"
12. **strategies (category)** — *(Populated by provider based on the patient's description: physical, breathing, cognitive, engagement, sensory, distraction.)*

### Step 3 — Social Contacts for Distraction

13. **contacts (name, phone, relationship)** — "Who are the people, or what are the social settings, you could reach out to or show up at when you need to be around others — even if you don't tell them anything is wrong? Let's get names and numbers."
14. **contacts (best_way_to_reach)** — "For each person, what is the easiest way to get in touch — call, text, just showing up?"
15. **contacts (notes)** — "Is there anything we should note about when they're usually available, or what you might do together?"

### Step 4 — People to Ask for Help

16. **trusted_contacts (name, phone, relationship)** — "Now let's list the people you could actually tell, 'I'm in crisis and I need help.' These are the people who know about your mental health. Who comes to mind?"
17. **trusted_contacts (knows_about_safety_plan)** — "Does this person know that you have a safety plan? Would you be comfortable sharing it with them so they know how to help?"
18. **trusted_contacts (notes)** — "What should we write down about how this person can help — for example, can they come to your home, drive you somewhere, or hold onto something for you?"

### Step 5 — Professional and Crisis Resources

19. **crisis_resources (populated by provider)** — "I'm going to add the key crisis numbers to your plan now — the 988 Lifeline, Crisis Text Line, 911, and your nearest emergency department. Let's go through each one so you know what to expect when you call or text."
20. **crisis_resources (nearest ED details)** — "Which emergency room is closest to where you live, and how would you get there? Can someone drive you, or would you take a rideshare or subway?"

### Step 6 — Environmental Safety (Means Restriction)

21. **safety_steps (action)** — "Let's talk about making your environment safer. Are there things in your home that you worry could be dangerous during a crisis — medications, alcohol, sharp objects, firearms, anything else?"
22. **safety_steps (responsible_person)** — "For each item we just identified, who could hold onto it or help you secure it? Is there someone you trust to take that step with you?"
23. **safety_steps (status / date_completed)** — "Have you already taken any of these steps? If so, when did you do it, and is it still in place?"
24. **safety_steps (notes)** — "Is there anything else we should write down about how this step works day-to-day — for example, how you access your medication if it's locked up?"

### Reasons for Living

25. **reasons** — "I'd like us to write down the things that matter most to you — the people, goals, experiences, or even small daily things that give you a reason to keep going. There's no wrong answer. What comes to mind?"

### Provider Notes

26. **clinical_observations** — *(Documented by provider after session, not elicited from patient.)*
27. **risk_level_at_creation** — *(Assessed by provider using validated instruments, e.g., C-SSRS.)*
28. **review_frequency_days / next_review_date** — "I'd like us to review and update this plan regularly. How often feels right to you — every session, every other week, once a month?"

---

## Section 2: Ambiguous or Missing Template Fields

The following fields in `safety_plan_template.json` lack sufficient guidance or could cause confusion during clinical use.

| # | Field / Area | Issue | Suggested Clarification |
|---|---|---|---|
| 1 | `patient_info.primary_diagnosis` / `secondary_diagnosis` | Template holds free-text strings. No guidance on who populates this or how it stays current if diagnosis changes. | Add a `diagnosis_source` field (e.g., "provider-entered") and a `last_confirmed` date. Note in instructions that diagnosis fields are provider-only. |
| 2 | `step_2_coping_strategies.effectiveness_rating` | Scale is 1-5 but the anchors are not defined anywhere in the template. A "3" is ambiguous. | Add an `effectiveness_scale` object to the metadata: `{ 1: "Rarely helps", 2: "Sometimes helps", 3: "Helps about half the time", 4: "Usually helps", 5: "Almost always helps" }`. |
| 3 | `step_2_coping_strategies.category` | The enum of valid categories (physical, breathing, cognitive, engagement, sensory, distraction) is not listed in the template. Values are only discoverable by reading the sample data. | Add a `valid_categories` array to the `step_2_coping_strategies` instructions block. |
| 4 | `step_3_social_contacts_for_distraction.contacts.relationship` | Mixes personal roles ("sibling," "friend") with a structural label ("social_setting") in the same field. The yoga studio entry is structurally different from person entries. | Split into two sub-arrays: `people` and `social_settings`, each with appropriate fields (social settings need address and schedule, not phone). |
| 5 | `step_6_environmental_safety.safety_steps.status` | Only values observed are "completed" and "ongoing." No defined enum. Missing a value for steps that are planned but not yet taken. | Define an enum: `["not_started", "in_progress", "completed", "ongoing", "no_longer_needed"]`. |
| 6 | `reasons_for_living.reasons` | Stored as plain strings with no structure. Difficult to track which reasons remain salient over time or to flag when a patient can no longer identify any. | Convert each reason to an object with `description`, `date_added`, and `still_salient` (boolean) fields. Add a clinical alert if the array is empty or all items are marked not salient. |
| 7 | `safety_plan_metadata.status` | Only value shown is "active." No documentation of other valid states or what triggers a status change. | Define enum: `["draft", "active", "under_review", "inactive", "expired"]`. Add `status_changed_date` and `status_changed_by` fields. |
| 8 | `safety_plan_metadata.created_date` / `last_updated` | These are null in the template. No guidance on format (ISO 8601?) or whether they auto-populate. | Specify ISO 8601 format in a comment or instructions block. Require these to be non-null when `status` is "active." |
| 9 | `step_5_professional_and_crisis_resources` | The nearest ED entry has `facility_name` and `address` fields that do not appear on the other crisis resource entries, creating an inconsistent schema. | Define two sub-schemas: `hotline_resource` (with phone/text/chat_url) and `facility_resource` (with facility_name/address/phone). |
| 10 | `provider_notes.plan_modifications_log` | Each entry has only `date` and `modification` (free text). No field for who made the modification or what triggered the review. | Add `modified_by`, `review_trigger` (e.g., "scheduled review," "patient request," "clinical escalation"), and `risk_level_at_review`. |

---

## Section 3: Crisis Resource Decision Tree

Given a patient's geographic location and their preferred contact modality (call, text, or chat), the following decision tree determines which resources from `crisis_resources.csv` to surface first.

```
START: Is the patient in immediate danger or at imminent risk of harming themselves or others?
|
+-- YES --> Surface first: 911 / Local Emergency Services
|           Then surface: Nearest Emergency Department (from safety plan)
|           Then surface: 988 Suicide & Crisis Lifeline (call 988)
|           STOP — do not filter further; all channels active.
|
+-- NO --> Continue to Step A.

STEP A: Identify the patient's state/region.
|
+-- New York City
|   |
|   +-- Preferred modality?
|       +-- CALL --> 1. NYC Well (1-888-692-9355)
|       |           2. 988 Suicide & Crisis Lifeline (988)
|       +-- TEXT --> 1. NYC Well (Text WELL to 65173)
|       |           2. 988 Lifeline (Text 988)
|       |           3. Crisis Text Line (Text HOME to 741741)
|       +-- CHAT --> 1. 988 Lifeline Chat (988lifeline.org/chat)
|                    2. Crisis Text Line (crisistextline.org)
|
+-- San Francisco / Bay Area
|   |
|   +-- Preferred modality?
|       +-- CALL --> 1. Bay Area Crisis Stabilization (1-415-970-3800)
|       |           2. 988 Suicide & Crisis Lifeline (988)
|       +-- TEXT --> 1. 988 Lifeline (Text 988)
|       |           2. Crisis Text Line (Text HOME to 741741)
|       +-- CHAT --> 1. 988 Lifeline Chat (988lifeline.org/chat)
|                    2. Crisis Text Line (crisistextline.org)
|
+-- Illinois
|   |
|   +-- Preferred modality?
|       +-- CALL --> 1. Illinois Call4Calm (1-833-225-2326)
|       |           2. 988 Suicide & Crisis Lifeline (988)
|       +-- TEXT --> 1. Illinois Call4Calm (Text TALK to 552020)
|       |           2. 988 Lifeline (Text 988)
|       |           3. Crisis Text Line (Text HOME to 741741)
|       +-- CHAT --> 1. 988 Lifeline Chat (988lifeline.org/chat)
|                    2. Crisis Text Line (crisistextline.org)
|
+-- Georgia
|   |
|   +-- Preferred modality?
|       +-- CALL --> 1. Georgia Crisis & Access Line (1-800-715-4225)
|       |           2. 988 Suicide & Crisis Lifeline (988)
|       +-- TEXT --> 1. 988 Lifeline (Text 988)
|       |           2. Crisis Text Line (Text HOME to 741741)
|       +-- CHAT --> 1. 988 Lifeline Chat (988lifeline.org/chat)
|                    2. Crisis Text Line (crisistextline.org)
|
+-- ALL OTHER STATES / REGIONS (no local resource in CSV)
    |
    +-- Preferred modality?
        +-- CALL --> 1. 988 Suicide & Crisis Lifeline (988)
        |           2. SAMHSA National Helpline (1-800-662-4357)
        +-- TEXT --> 1. 988 Lifeline (Text 988)
        |           2. Crisis Text Line (Text HOME to 741741)
        +-- CHAT --> 1. 988 Lifeline Chat (988lifeline.org/chat)
                    2. Crisis Text Line (crisistextline.org)

OVERLAY: Specialty Populations (surface IN ADDITION to above)
|
+-- Patient is LGBTQ+ and under 25?
|   --> Add: Trevor Project (1-866-488-7386 / Text START to 678-678)
|
+-- Patient is transgender?
|   --> Add: Trans Lifeline (1-877-565-8860)
|
+-- Patient is a veteran or military family?
|   --> Add: Veterans Crisis Line (988 press 1 / Text 838255)
|
+-- Patient is perinatal or postpartum?
|   --> Add: Postpartum Support International (1-800-944-4773 / Text 503-894-9453)
|
+-- Patient is experiencing domestic violence?
|   --> Add: National DV Hotline (1-800-799-7233 / Text START to 88788)
|
+-- Patient is affected by a disaster?
|   --> Add: Disaster Distress Helpline (1-800-985-5990 / Text TalkWithUs to 66746)
|
+-- Patient is dealing with an eating disorder?
|   --> Add: National Alliance on Eating Disorders (1-866-662-1235)
|       NOTE: M-F 11am-9pm ET only — not 24/7
|
+-- Concern involves child abuse or neglect?
|   --> Add: Childhelp Hotline (1-800-422-4453)
|
+-- Patient needs general mental health referrals (non-crisis)?
    --> Add: NAMI Helpline (1-800-950-6264 / Text NAMI to 741741)
        NOTE: M-F 10am-10pm ET only — not a crisis line
```

---

## Section 4: Gaps in crisis_resources.csv

### 4A — Geographic Coverage Gaps

The CSV contains regional/local resources for only four areas:

| Area Covered | Resource |
|---|---|
| New York City | NYC Well |
| San Francisco | Bay Area Crisis Stabilization |
| Illinois (statewide) | Illinois Call4Calm |
| Georgia (statewide) | Georgia Crisis & Access Line |

**Missing states/regions where Headway has significant provider and patient volume:**

- **Texas** — No state crisis line listed. Texas has the statewide Crisis Services line (accessible via 988 routing, but a dedicated entry would be valuable).
- **Florida** — No state crisis line listed.
- **California (outside San Francisco)** — The Bay Area entry does not serve Los Angeles, San Diego, Sacramento, or other major metro areas. California has county-level crisis lines that should be represented.
- **Pennsylvania** — No entry. PA has a statewide crisis text line and county crisis programs.
- **New Jersey** — No entry, despite geographic proximity to Headway's NYC operations.
- **Ohio, Michigan, Virginia, North Carolina, Massachusetts, Colorado, Washington, Arizona, Maryland** — All are states with high mental health service demand and no entries in the CSV.

**Recommendation:** At minimum, add statewide crisis resources for the 10 states where Headway has the largest patient populations. Consider integrating with the SAMHSA treatment locator API to dynamically surface local resources by ZIP code.

### 4B — Resource Type Gaps

| Gap | Details |
|---|---|
| **Warm lines (non-crisis peer support)** | The CSV has no warm lines. Warm lines serve patients who are distressed but not in acute crisis and prefer peer support over clinical intervention. Examples: NAMI state warm lines, DBSA peer lines. |
| **Spanish-language resources** | SAMHSA is noted as bilingual, but no dedicated Spanish-language crisis line is listed. The 988 Lifeline offers Spanish service (press 2), but this is not called out. For a patient population that may include Spanish-speaking individuals, a clearly labeled Spanish option is important. |
| **Deaf/Hard of Hearing access** | No TTY numbers or video relay service (VRS) information is provided. The 988 Lifeline supports TTY (use 711 then 988), but this is not noted. |
| **Chat-only resources for text-averse populations** | Only the 988 Lifeline and Crisis Text Line offer chat. Consider adding resources that specialize in chat-based support, e.g., IMAlive or local crisis chat services. |
| **Substance use crisis (acute)** | SAMHSA is listed for referrals, but there is no resource for acute substance use emergencies (e.g., overdose). Consider adding a poison control center (1-800-222-1222) and noting that 911 should be called for overdose. |
| **Firearms-specific counseling** | No resource for patients who need help securing firearms. Consider adding the Counseling on Access to Lethal Means (CALM) resource or a firearms storage program referral. |
| **International resources** | No resources for patients who may be traveling or living abroad temporarily. Consider adding the International Association for Suicide Prevention (IASP) directory link. |

### 4C — Data Quality Issues

| Issue | Details |
|---|---|
| **Inconsistent specialty labeling** | The `Specialty` column uses varying levels of specificity (e.g., "General crisis and suicide prevention" vs. "Text-based crisis support"). A controlled vocabulary would improve filtering. |
| **Missing modality coverage** | Several resources have no text option (SAMHSA, Trans Lifeline, Bay Area Crisis Stabilization, National Alliance on Eating Disorders, Childhelp, Georgia Crisis & Access Line). This is a real limitation but should be explicitly noted so coordinators do not attempt to text those numbers. |
| **Limited-hours resources not flagged** | NAMI (M-F 10am-10pm ET), National Alliance on Eating Disorders (M-F 11am-9pm ET), and Postpartum Support International (text is M-F 9am-9pm ET) have restricted hours. The CSV stores this in the `Hours` column, but there is no boolean `is_24_7` flag for easy filtering in an automated system. |

---

## Section 5: One-Page Summary for Non-Clinical Care Coordinators

### What This Workflow Is

This workflow supports the creation, use, and maintenance of a patient safety plan based on the Stanley-Brown Safety Planning Intervention. A safety plan is a written, prioritized list of coping strategies and resources that a patient can use during a mental health crisis. It is developed collaboratively between a patient and their provider during a therapy session.

**Your role as a care coordinator:** You do not create or modify the clinical content of a safety plan. You support the process by ensuring plans are documented, stored, up to date, and that crisis resources are accurate and available when needed.

### How the Safety Plan Works (Six Steps)

The plan follows a specific sequence. A patient in crisis starts at Step 1 and works through the steps in order, escalating only if the previous step did not help.

1. **Warning Signs** — The patient recognizes personal cues (thoughts, behaviors, moods) that signal a crisis is developing. This is the trigger to pull out the safety plan.
2. **Internal Coping Strategies** — The patient tries activities they can do alone (walking, breathing exercises, journaling) to manage distress without contacting anyone.
3. **Social Contacts for Distraction** — If coping alone is not enough, the patient reaches out to specific people or goes to specific places to be around others. They do not need to disclose they are in crisis.
4. **People to Ask for Help** — If distraction is not enough, the patient contacts trusted individuals who know about their mental health and tells them they need help.
5. **Professional and Crisis Resources** — If personal contacts cannot resolve the crisis, the patient contacts professional crisis services (988 Lifeline, Crisis Text Line, their therapist or psychiatrist, or 911).
6. **Environmental Safety** — Ongoing steps to reduce access to dangerous items (medications, alcohol, sharp objects). These are taken proactively, not just during a crisis.

A separate "Reasons for Living" section lists personal motivations the patient can review at any point.

### What You Need to Know About Crisis Resources

- **988 Suicide & Crisis Lifeline** (call or text 988) and **Crisis Text Line** (text HOME to 741741) are the two national defaults. They are available 24/7, free, and confidential.
- **Local/state resources** exist for New York City, San Francisco, Illinois, and Georgia. If a patient is in one of those areas, the local resource should be offered first because it can connect to mobile crisis teams and local services.
- **Specialty resources** exist for veterans, LGBTQ+ youth, transgender individuals, postpartum patients, domestic violence survivors, disaster-affected individuals, eating disorders, and child abuse. Surface these when they match the patient's situation, in addition to the general resources.
- **Not all resources are 24/7.** NAMI and the National Alliance on Eating Disorders are weekday-only. Check the hours before recommending.
- **Not all resources support every modality.** Some have no text option. If a patient prefers texting, verify the resource supports it before recommending.

### Your Key Responsibilities

1. **Before a session where a safety plan will be created or reviewed:** Confirm that the patient's demographic information in the system is current (name, location, emergency contacts). Pull the most recent version of the safety plan if one exists.
2. **After a session:** Verify the provider has documented the plan in the patient record. Confirm the plan status is "active" and the next review date is set.
3. **Ongoing maintenance:** Flag plans that are past their review date (default: 30 days). Notify the assigned provider. Periodically verify that crisis resource phone numbers and URLs are still active.
4. **If a patient contacts you in distress:** You are not expected to provide clinical intervention. Direct them to the crisis resources on their plan, starting with 988 or Crisis Text Line. If they are in immediate danger, direct them to call 911. Notify their provider as soon as possible.

### Quick Reference Card

| Situation | Action |
|---|---|
| Patient mentions thoughts of self-harm | Direct to their provider immediately; if provider unavailable, direct to 988 or Crisis Text Line |
| Safety plan is past review date | Flag for provider; send reminder through scheduling system |
| Patient moved to a new state | Alert provider to update the nearest ED and local crisis resource on the plan |
| Patient reports a means restriction step is no longer in place | Alert provider immediately; this is clinically significant |
| You are unsure whether something is a crisis | Err on the side of caution. Contact the provider. If you cannot reach the provider within 15 minutes, direct the patient to 988 |
