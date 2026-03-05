# Clinical PRD Review

**PRD Reviewed:** Async Messaging Between Sessions (v1.3)
**Reviewer:** Clinical Review (Automated)
**Date:** 2026-03-04
**PRD Status:** Draft -- Pending Clinical Review

---

## Score Summary

| Dimension | Score | Max Score | % Score | |
|---|---|---|---|---|
| Patient Safety | 2 | 5 | 40% | NEEDS ATTENTION |
| Industry Standards Alignment | 3 | 5 | 60% | NEEDS ATTENTION |
| Medicolegal Risk | 2 | 5 | 40% | NEEDS ATTENTION |
| Reputation Risk | 3 | 5 | 60% | NEEDS ATTENTION |
| Outcome Improvement Potential | 3 | 5 | 60% | NEEDS ATTENTION |
| Patient Satisfaction Impact | 4 | 5 | 80% | |
| Evidence Base | 2 | 5 | 40% | NEEDS ATTENTION |
| Innovation Score | 4 | 5 | 80% | |

**Weighted Overall Score: 53.5%**

*(Weighted calculation: 0.20x2 + 0.15x3 + 0.15x2 + 0.10x3 + 0.15x3 + 0.10x4 + 0.10x2 + 0.05x4 = 2.675 out of 5.0 = 53.5%)*

---

## Dimension-Level Feedback

### Patient Safety -- 2/5 (40%) NEEDS ATTENTION

The PRD identifies a triage layer that flags safety-relevant messages and prompts providers to respond within 4 hours, with an automated crisis resource message as a backstop. However, the PRD itself acknowledges (Risk #1) that a 4-hour window may be dangerously insufficient for imminent self-harm disclosures, and there is no real-time escalation pathway to emergency services, no warm handoff protocol, and no integration with a crisis response team. Additionally, the image sharing feature (Risk #5) explicitly lacks content moderation in V1, meaning self-harm images could be received with no system-level safeguard. To improve, the PRD needs a redundant, multi-layered crisis response design: immediate automated crisis resources upon flag detection (not after 4 hours), an on-call clinical escalation pathway for high-acuity flags, a defined protocol for contacting emergency services when a patient is unreachable, and content moderation for image uploads.

### Industry Standards Alignment -- 3/5 (60%) NEEDS ATTENTION

The PRD references HIPAA compliance, AES-256 encryption, and CPT code exploration, demonstrating awareness of regulatory frameworks. However, the document lacks explicit alignment with APA Practice Guidelines for digital interventions, SAMHSA evidence-based protocols for between-session contact, or Joint Commission telehealth standards. The PHQ-2 micro-screener is being deployed in an unvalidated context (Risk #7), which conflicts with clinical standards requiring instruments be used within their validated parameters. Documentation standards are also unclear: messages are excluded from patient data export in V1, which may not meet medical record requirements. To improve, the PRD should map each feature component against specific APA and SAMHSA guidelines, use only validated instruments in validated contexts (or plan a validation study), and ensure messaging records meet medical record documentation standards from launch.

### Medicolegal Risk -- 2/5 (40%) NEEDS ATTENTION

The PRD creates substantial duty-of-care ambiguity. When a patient messages a provider about a crisis and the provider does not see it for 12+ hours, the medicolegal question of whether the messaging channel creates a duty to respond in a timely manner is unresolved. The cross-state licensure question (Risk #4) is flagged but entirely open, meaning a patient could message from a state where the provider is not licensed, creating scope-of-practice exposure. There is no informed consent mechanism described for the messaging feature -- patients need to understand this is not a crisis channel and that response times are not guaranteed. The exclusion of messages from patient data exports (Risk #6) is a potential violation of state-level patient access laws. To improve, the PRD must define an informed consent flow that explicitly sets patient expectations, resolve the cross-state licensure check (block or disclose), establish clear duty-of-care boundaries in the product UX and terms, and include messages in the patient record from day one.

### Reputation Risk -- 3/5 (60%) NEEDS ATTENTION

The feature concept aligns well with Headway's mission of expanding access to care and supporting therapeutic relationships. However, two elements pose meaningful reputation risk. First, AI-generated response suggestions (Risk #2) could be perceived as replacing human clinical judgment with automation -- if a patient learns their therapist's reply was AI-drafted, it could damage trust and generate negative coverage. Second, providers are not compensated for messaging responses in V1 (Risk #3), which could trigger provider backlash and be framed as extracting free labor from an already-strained workforce. To improve, the PRD should mandate transparent disclosure to patients when AI suggestions are used, develop a clear provider compensation roadmap with a committed timeline, and ensure marketing positions the feature as provider-empowering rather than provider-replacing.

### Outcome Improvement Potential -- 3/5 (60%) NEEDS ATTENTION

The clinical logic model is plausible: maintaining therapeutic alliance through between-session contact should reduce dropout and support engagement, and the internal data (34% higher dropout with 3+ week gaps) supports the hypothesis. The success metrics include clinically relevant endpoints (90-day retention, no-show reduction). However, the PRD lacks a formal clinical logic model tracing the causal pathway from messaging to symptom reduction or functional improvement. The measurement plan uses engagement proxies (messages sent, NPS) rather than validated clinical outcome measures (e.g., PHQ-9 change scores, GAD-7 trajectories). There is no plan for a controlled evaluation to distinguish feature impact from selection effects. To improve, the PRD should add validated clinical outcome measures to the success metrics, articulate an explicit theory of change, and plan an A/B evaluation or matched-cohort study.

### Patient Satisfaction Impact -- 4/5 (80%)

The feature is well-designed to improve the patient experience. It addresses a clearly documented patient need (between-session support), offers convenience without mandating participation, and includes thoughtful touches like automated check-ins and mood prompts that can reinforce a sense of being cared for. The 500-character limit and 5-message-per-day cap strike a reasonable balance between access and boundary-setting. The one gap is accessibility: the PRD does not address patients with limited digital literacy, non-English-speaking patients, or accommodations for patients with disabilities. Adding accessibility requirements and multilingual support plans would push this to a top score.

### Evidence Base -- 2/5 (40%) NEEDS ATTENTION

The PRD references internal survey data and engagement metrics but cites no published clinical evidence supporting asynchronous messaging as a therapeutic adjunct. While platforms like Talkspace and BetterHelp offer messaging, the evidence base for async messaging specifically improving clinical outcomes in therapist-patient dyads is thin and mixed. The competitive analysis is mentioned in the appendix but not synthesized in the body. The PHQ-2 is a validated instrument, but using it in an async chat context is explicitly unvalidated (Risk #7). The AI response suggestion system is based on a fine-tuned model with no referenced evidence for safety or efficacy of AI-assisted provider communication in mental health. To improve, the PRD should include a literature review summary, cite relevant RCTs or meta-analyses for between-session digital contact, plan a validation study for the PHQ-2 in the async context, and reference published evidence on AI-assisted clinical communication.

### Innovation Score -- 4/5 (80%)

The combination of NLP-based triage, AI response suggestions, automated validated screeners, and structured async messaging in an insurance-integrated platform is genuinely differentiated. Competitors offer messaging but generally lack triage intelligence, integrated screeners, or the payer-network infrastructure Headway provides. The feature has clear potential to generate publishable clinical insights (e.g., between-session messaging patterns as predictors of dropout, NLP triage model performance in real-world deployment). The data generated could advance Headway's learning health system objectives. The main limitation is that much of the innovation depends on AI components (triage, response suggestions) that carry the highest clinical and reputational risk.

---

## Overall Clinical Readiness Assessment

**Not Ready**

This PRD demonstrates strong product thinking and a genuine clinical intuition about the value of between-session contact. However, it is not ready for clinical approval in its current form. Five of eight review dimensions score below 70%, and three of the four highest-weighted dimensions (Patient Safety, Medicolegal Risk, and Evidence Base) score at 40%. The most critical gaps are the absence of a robust crisis escalation protocol beyond an inadequate 4-hour timer, unresolved duty-of-care and licensure ambiguities that create material legal exposure, no informed consent mechanism, use of a validated instrument outside its validated context, and no published evidence cited to support the clinical approach. The PRD commendably identifies many of these issues in its own Risks section, but leaves all seven risks in "Open" status with no mitigation plans. Before clinical sign-off, the team should close every open risk item with a concrete mitigation or a documented accept-the-risk decision, redesign the safety escalation pathway with input from the clinical operations team, add an informed consent flow and clear patient-facing expectations, and plan a staged clinical evaluation with validated outcome measures.
