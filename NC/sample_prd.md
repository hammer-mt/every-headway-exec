# Product Requirements Document: Async Messaging Between Sessions

**Document Version:** 1.3
**Author:** Jordan Reeves, Product Manager — Patient Experience
**Last Updated:** 2026-02-18
**Status:** Draft — Pending Clinical Review
**Stakeholders:** Product, Engineering, Clinical, Legal, Compliance, Design

---

## 1. Overview

This PRD describes a new asynchronous messaging feature that enables patients and their providers to communicate between scheduled therapy or psychiatry sessions on the Headway platform. The goal is to increase patient engagement, reduce appointment no-shows, and give providers lightweight touchpoints with their patients outside of the 45- or 60-minute session window.

The feature will be available to all Headway patients and providers on supported health plans, accessible via the Headway mobile app and web portal.

---

## 2. Problem Statement

Patients frequently experience moments of distress, breakthrough, or logistical confusion between sessions but have no structured channel to reach their provider through Headway. Currently, patients either:

- Wait until their next session to raise important concerns
- Call or text their provider's personal phone (inconsistent, undocumented)
- Use third-party messaging apps with no clinical record integration
- Disengage entirely when they feel unsupported between sessions

Provider feedback indicates that 68% of surveyed Headway therapists wish they had a way to check in with patients between sessions, especially those showing early signs of disengagement or worsening symptoms.

Internal data shows that patients who have 3+ weeks between sessions have a 34% higher dropout rate than those seen biweekly. An asynchronous messaging channel could serve as a bridge to maintain therapeutic alliance during gaps.

---

## 3. Proposed Solution

### 3.1 Core Feature

A HIPAA-compliant, in-app asynchronous messaging system allowing:

- **Patient-initiated messages:** Patients can send text messages to their provider at any time. Messages are limited to 500 characters per message, with up to 5 messages per day.
- **Provider responses:** Providers can respond at their convenience. There is no SLA or required response time, but the system will surface unread messages in the provider dashboard.
- **Automated check-ins:** The system will send automated, templated check-in messages to patients at configurable intervals (e.g., 3 days post-session, 7 days post-session). These messages will include brief mood check prompts and a PHQ-2 micro-screener.
- **AI-generated response suggestions:** When a provider opens a patient message, the system will generate 2-3 suggested brief responses based on the message content and the patient's treatment history. Providers can use, edit, or dismiss suggestions.
- **Image and file sharing:** Patients can share images (e.g., journal entries, worksheets) and providers can share PDF resources.

### 3.2 Triage Layer

Messages from patients will be processed through a lightweight NLP triage layer that flags messages containing potential safety-relevant content (e.g., self-harm language, crisis indicators). Flagged messages will be:

- Surfaced with a visual indicator to the provider
- Accompanied by a prompt for the provider to respond within 4 hours
- If no provider response within 4 hours, an automated message will be sent to the patient with crisis resource links (988 Lifeline, Crisis Text Line)

### 3.3 Billing and Reimbursement

- Messaging will be offered as a free value-add feature to patients; no additional copay.
- Headway will explore CPT code 98970-98972 (online digital E/M) for potential future provider reimbursement, but initial launch will not bill insurance.
- Providers will not be compensated for message responses in V1.

---

## 4. User Stories

| ID | Role | Story | Priority |
|----|------|-------|----------|
| US-01 | Patient | As a patient, I want to send my therapist a message between sessions so I can share something important that came up. | P0 |
| US-02 | Provider | As a provider, I want to see flagged messages from at-risk patients so I can prioritize my responses. | P0 |
| US-03 | Patient | As a patient, I want to receive automated check-ins so I feel supported between sessions. | P1 |
| US-04 | Provider | As a provider, I want AI-suggested responses so I can reply efficiently to routine messages. | P1 |
| US-05 | Patient | As a patient, I want to share a photo of my thought record worksheet so my therapist can see my progress. | P2 |
| US-06 | Provider | As a provider, I want to send resource PDFs to my patients so they have materials to work with between sessions. | P2 |
| US-07 | Patient | As a patient, I want to complete a quick mood check when prompted so my therapist has data about how I'm doing. | P1 |
| US-08 | Admin | As a Headway admin, I want to monitor messaging volume and triage flag rates so I can assess system health. | P1 |

---

## 5. Technical Requirements

### 5.1 Infrastructure
- End-to-end encryption for all messages (AES-256 at rest, TLS 1.3 in transit)
- Messages stored for 7 years per HIPAA retention requirements
- Real-time delivery via WebSocket with push notification fallback
- 99.9% uptime SLA for messaging service

### 5.2 NLP Triage Model
- Binary classification model for safety-relevant content
- Training data: 50,000 labeled therapy session transcript excerpts (de-identified)
- Target performance: 92% recall for safety-relevant content, <15% false positive rate
- Model will run inference on-device for latency and privacy; cloud fallback for complex cases

### 5.3 AI Response Suggestions
- LLM-based response generation using fine-tuned model on de-identified provider response patterns
- Responses constrained to supportive/logistical tone; no clinical recommendations or diagnostic language
- Provider must explicitly select or edit any suggestion before sending
- All AI-suggested responses logged with acceptance/rejection metadata

### 5.4 Integrations
- EHR integration for message threading in patient chart
- Calendar integration for appointment-aware automated check-ins
- Analytics pipeline for engagement metrics
- Notification service (push, SMS fallback, email digest)

### 5.5 Access Controls
- Patients can only message their assigned provider(s)
- Providers can disable messaging for specific patients
- Headway clinical operations team can view flagged message threads for quality assurance
- Messages are excluded from patient-facing data export in V1 (to be revisited in V2)

---

## 6. Success Metrics

| Metric | Target | Measurement Period |
|--------|--------|--------------------|
| Patient messaging adoption rate | 40% of active patients send at least 1 message | 6 months post-launch |
| Appointment no-show rate reduction | 15% reduction in no-shows for messaging users | 6 months post-launch |
| Provider response rate | 70% of patient messages receive a provider reply within 48 hours | 3 months post-launch |
| Patient satisfaction (NPS) | +8 point NPS increase for messaging users | 6 months post-launch |
| Safety flag accuracy | 92% recall, <15% false positive rate | Ongoing |
| Patient retention | 20% improvement in 90-day retention for messaging users | 6 months post-launch |
| Avg. messages per patient per week | 2.5 messages | 3 months post-launch |

---

## 7. Risks and Open Questions

| # | Risk / Question | Status |
|---|-----------------|--------|
| 1 | What happens if a patient sends a message indicating imminent self-harm and the provider doesn't see it for 12+ hours? The 4-hour automated response may not be sufficient. | Open |
| 2 | Could AI-generated response suggestions inadvertently provide clinical advice that the provider hasn't reviewed carefully? | Open |
| 3 | Without provider compensation, will response rates be high enough to make the feature valuable? | Open |
| 4 | How do we handle messages from patients in states where the provider is not licensed? | Open |
| 5 | Image sharing could introduce risk of receiving distressing content (self-harm images). No content moderation is planned for V1. | Open |
| 6 | Excluding messages from patient data export may conflict with state-level patient access to records laws. | Open |
| 7 | The PHQ-2 micro-screener delivered via chat has not been validated in an asynchronous digital context. | Open |

---

## 8. Timeline

| Phase | Scope | Target Date |
|-------|-------|-------------|
| Design Sprint | UX flows, provider/patient interviews | 2026-03-10 |
| Technical Design | Architecture review, security review | 2026-03-24 |
| Clinical Review | CMO review against clinical rubric | 2026-03-31 |
| Alpha Build | Core messaging (no AI, no triage) | 2026-05-01 |
| Beta (Internal) | Full feature set, internal testing | 2026-06-15 |
| Beta (Limited GA) | 500 provider-patient pairs | 2026-07-15 |
| General Availability | Full rollout | 2026-09-01 |

---

## 9. Appendix

- Competitive analysis: Talkspace, BetterHelp, Alma, and Grow Therapy async messaging features
- Provider survey results (N=342): "Between-session communication preferences"
- Patient survey results (N=1,207): "What would improve your Headway experience?"
- HIPAA messaging compliance checklist (Legal team, v2.1)
