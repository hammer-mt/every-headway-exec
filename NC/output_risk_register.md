# Risk Register Update Assessment

**Prepared:** 2026-03-04
**Data Sources:** `risk_register.csv` (15 entries, RISK-001 through RISK-015), `regulatory_news_feed.csv` (20 items, 2025-12-15 through 2026-02-27)
**Methodology:** Each news item was evaluated against Headway's business model (telehealth marketplace connecting therapists and psychiatrists with insurance) and mapped to existing risk register entries. Likelihood and impact scores follow the register's existing scale (Low / Medium / High / Critical).

---

## 1. Change Summary Table

| # | News Item (Date) | Action | Risk ID(s) | Rationale |
|---|---|---|---|---|
| 1 | DOJ $15M Cerebral settlement over prescribing practices (2/27) | **Update** | RISK-007 | Direct precedent for enforcement against telehealth prescribing oversight deficiencies. Suggests the federal enforcement likelihood has increased; recommend upgrading RISK-007 Likelihood from Medium to High. |
| 2 | California AG sues BetterHelp over data sharing with social media (2/24) | **Update** | RISK-004, RISK-012 | Demonstrates active state AG enforcement on marketing-pixel data leakage in digital mental health. RISK-004 should remain as-is (already Low/Critical), but RISK-012 Likelihood should increase from Low to Medium given the enforcement trend targeting digital health specifically. |
| 3 | CMS proposes mandatory behavioral health quality reporting for MA plans (2/21) | **Update** | RISK-015, RISK-009 | If finalized, payers will require outcome reporting from network providers. Strengthens the case for measurement-based care investment. Recommend upgrading RISK-015 Impact from Medium to High (non-compliance could jeopardize payer contracts). Also mildly relevant to RISK-009 as payer policy shifts may affect claim adjudication. |
| 4 | Bipartisan Senate bill mandating insurance coverage of digital therapeutics (2/18) | **No Action** | N/A | Indirect relevance. If enacted, it would expand the addressable market for digital mental health tools but does not map directly to a current risk. Monitor only. |
| 5 | New York passes Telehealth Parity Permanence Act (2/15) | **Downgrade** | RISK-005 | Favorable development: one of Headway's key states now has permanent telehealth parity. Does not change the overall risk rating for RISK-005 (other states remain volatile), but should be noted in the mitigation log as a positive signal. |
| 6 | FTC warning letters to 5 mental health apps over deceptive outcome claims (2/12) | **Update** | RISK-010 | Indicates FTC is actively targeting mental health marketing claims. Recommend upgrading RISK-010 Likelihood from Low to Medium. |
| 7 | Class action against Talkspace over inadequate credentialing (2/8) | **Add** | NEW: RISK-016 | No existing risk register entry covers credentialing-specific litigation risk. While RISK-011 addresses treatment matching, credentialing verification failures are a distinct risk vector (see proposed entry below). |
| 8 | Texas Medical Board proposes telehealth prescribing restrictions for Schedule II (2/5) | **Update** | RISK-005, RISK-007 | State-level prescribing restriction would directly affect Headway psychiatrists in Texas. Reinforces the High likelihood on RISK-005. For RISK-007, adds a compliance dimension: even with good clinical oversight, state rules may prohibit certain prescribing modalities. |
| 9 | HHS OCR $1.2M settlement over HIPAA Right of Access violation (2/1) | **Add** | NEW: RISK-017 | Right-of-access compliance is distinct from breach prevention (RISK-004). Headway must ensure patient record access requests are fulfilled within 30 days. No existing entry covers this (see proposed entry below). |
| 10 | PSYPACT adds 5 new states, now covers 45 states (1/28) | **Downgrade** | RISK-005 | Positive development reducing interstate licensure barriers for psychologists. Recommend noting in RISK-005 mitigation log. The overall RISK-005 risk remains High due to countervailing trends (e.g., Texas prescribing restrictions), but the PSYPACT expansion partially offsets. |
| 11 | FDA releases final guidance on AI/ML clinical decision support in behavioral health (1/25) | **Update** | RISK-003, RISK-014 | Provides regulatory clarity for Headway's AI features. If Headway's tools meet the exemption criteria, RISK-003 regulatory exposure decreases. Recommend adding the FDA guidance to the RISK-003 mitigation plan and reviewing whether the exemption criteria apply. Could also lower RISK-003 Likelihood from Medium to Low pending legal review. For RISK-014, the guidance informs consent and disclosure requirements. |
| 12 | Illinois Healthcare AI Transparency Act, effective July 2026 (1/22) | **Update** | RISK-014 | New state-level obligation. Illinois joins the growing set of jurisdictions requiring AI disclosures. Confirms RISK-014 as an active area; recommend adding Illinois compliance deadline to the mitigation plan. No score change needed (Medium/Medium remains appropriate). |
| 13 | Ninth Circuit rules telehealth companies must comply with state consumer protection laws in each patient state (1/18) | **Update** | RISK-010, RISK-005 | Court precedent reinforcing multi-state compliance burden. Supports current RISK-010 and RISK-005 ratings. Recommend adding the Ninth Circuit ruling to the Related Regulation field for both. |
| 14 | Medicaid MCO behavioral health access requirements finalized by CMS (1/15) | **Update** | RISK-008 | Directly affects Headway's Centene Medicaid pilot. Recommend upgrading RISK-008 Impact from Medium to High, given that non-compliance could result in losing Medicaid contracts and CMS sanctions. Appointment availability standards (10 business days routine, 48 hours urgent) are concrete and measurable. |
| 15 | Record $4.75M HIPAA fine for unencrypted PHI at mental health practice (1/10) | **Update** | RISK-004 | Confirms OCR enforcement intensity in mental health. Headway's current mitigations (AES-256, TLS 1.3) address this, but the fine amount signals increased penalty exposure. No score change recommended (already Low/Critical), but note the enforcement escalation in the mitigation log. |
| 16 | DEA extends COVID telehealth prescribing flexibilities through Dec 2026 (1/7) | **Update** | RISK-007 | Short-term positive: current workflows can continue. But the extension is temporary and a permanent rule is pending, which may be more restrictive. Recommend no score change but adding the December 2026 deadline to the RISK-007 monitoring plan as a key date. |
| 17 | Oregon mandates standardized outcome reporting for behavioral health providers (1/4) | **Update** | RISK-015 | Reinforces the trend toward mandatory outcome reporting. Headway's MBC infrastructure is a strength, but non-compliance by providers on the platform is a risk. No score change needed, but add Oregon to the compliance tracking matrix referenced in RISK-015. |
| 18 | Multi-state AG investigation into digital health marketing practices (12/30) | **Update** | RISK-010 | Twelve-state coordinated investigation further raises the enforcement likelihood for marketing compliance. Combined with the FTC warning letters (item 6), this supports upgrading RISK-010 Likelihood from Low to Medium. |
| 19 | Study finds significant variability in telehealth informed consent practices (12/22) | **Update** | RISK-014 | Academic study, not enforcement, but useful for benchmarking. Recommend conducting an internal audit of Headway's consent flows against the study's recommended elements and documenting findings. No score change. |
| 20 | EEOC guidance on employer use of AI mental health screening tools (12/15) | **No Action** | N/A | Low relevance to Headway's current business model. Only relevant if Headway pursues employer wellness channel. Flag for monitoring only. |

---

## 2. Recommended Score Changes

| Risk ID | Current Likelihood | Proposed Likelihood | Current Impact | Proposed Impact | Current Score | Proposed Score | Trigger |
|---|---|---|---|---|---|---|---|
| RISK-007 | Medium | **High** | Critical | Critical | High | **Critical** | DOJ Cerebral settlement (item 1); Texas prescribing restrictions (item 8) |
| RISK-008 | Medium | Medium | Medium | **High** | Medium | **High** | CMS Medicaid access requirements (item 14) |
| RISK-010 | Low | **Medium** | High | High | Medium | **High** | FTC warning letters (item 6); multi-state AG investigation (item 18) |
| RISK-012 | Low | **Medium** | High | High | Medium | **High** | California AG BetterHelp lawsuit (item 2) |
| RISK-015 | Medium | Medium | Medium | **High** | Medium | **High** | CMS proposed MA quality reporting (item 3); Oregon mandate (item 17) |

---

## 3. Proposed New Risk Register Entries

### RISK-016: Credentialing Verification

| Field | Value |
|---|---|
| **Risk_ID** | RISK-016 |
| **Category** | Clinical Quality |
| **Risk_Description** | Litigation or regulatory action alleging Headway failed to adequately verify provider credentials, licensure status, or board certifications, resulting in unqualified individuals delivering care through the platform. |
| **Likelihood** | Medium |
| **Impact** | Critical |
| **Risk_Score** | High |
| **Owner** | VP Legal + Chief Medical Officer |
| **Status** | Active — Monitoring |
| **Mitigation_Plan** | Primary source verification of all provider licenses and certifications at onboarding; automated NPDB query at onboarding and biannually; real-time state license status monitoring via license verification API; re-credentialing every 3 years per NCQA standards; credentialing committee review of any malpractice history, disciplinary actions, or gaps in practice; maintain auditable credentialing files for each provider; document policies exceeding standards cited in Talkspace class action. |
| **Last_Reviewed** | 2026-03-04 |
| **Related_Regulation** | NCQA credentialing standards; state medical board licensure requirements; CMS Conditions of Participation; relevant case law including 2026 Talkspace class action (SDNY) |

### RISK-017: HIPAA Right of Access Compliance

| Field | Value |
|---|---|
| **Risk_ID** | RISK-017 |
| **Category** | Data Privacy |
| **Risk_Description** | Failure to provide patients with timely access to their health records within HIPAA-mandated timelines (30 calendar days, with one 30-day extension if justified), resulting in OCR enforcement action, fines, or patient complaints. |
| **Likelihood** | Low |
| **Impact** | High |
| **Risk_Score** | Medium |
| **Owner** | DPO + VP Product |
| **Status** | Active — Monitoring |
| **Mitigation_Plan** | Patient-facing portal provides real-time access to therapy session notes, billing records, and assessment results; documented process for handling formal records requests with tracking and SLA of 15 calendar days (half the HIPAA maximum); staff training on right-of-access requirements; quarterly audit of records request fulfillment times and denial rates; fee schedule for records compliant with state and federal limits; escalation path for complex or high-volume requests. |
| **Last_Reviewed** | 2026-03-04 |
| **Related_Regulation** | HIPAA Privacy Rule 45 CFR 164.524; HHS OCR Right of Access Initiative enforcement actions; state health records access laws |

---

## 4. Low-Confidence Relevance Assessments

The following news items have assessments where confidence is lower and human review is recommended:

1. **Bipartisan Senate bill on digital therapeutics coverage (item 4, marked No Action):** This was assessed as indirect relevance because Headway is primarily a provider marketplace, not a digital therapeutics company. However, if Headway's product roadmap includes integrating or distributing FDA-cleared digital therapeutics (e.g., as adjunct tools for therapists), relevance would increase significantly. **Recommend product team review.**

2. **EEOC guidance on employer AI mental health screening (item 20, marked No Action):** Assessed as low relevance to Headway's current B2C/B2B2C model. If Headway has or is exploring employer-sponsored EAP channels or workplace wellness partnerships, this becomes directly relevant. **Recommend business development team review.**

3. **HHS OCR Right of Access settlement (item 9, marked Add):** The decision to add this as a new risk entry (RISK-017) rather than folding it into existing RISK-004 (PHI breach) is a judgment call. Right-of-access failures are operationally and legally distinct from breach events, warranting a separate entry, but this is a moderate-confidence assessment. **Recommend legal team review of whether the risk is adequately covered by RISK-004 or warrants a standalone entry.**

4. **FDA final guidance on AI/ML clinical decision support (item 11, suggestion to potentially lower RISK-003 Likelihood):** The recommendation to consider downgrading RISK-003 depends on whether Headway's AI features actually meet the FDA exemption criteria, which requires legal and clinical review. **Do not change the score without confirming exemption eligibility with counsel.**

5. **New York Telehealth Parity Permanence Act (item 5, marked Downgrade for RISK-005):** Assessed as a positive signal, but the overall RISK-005 score should remain High given countervailing restrictive trends in other states (e.g., Texas). The "downgrade" notation reflects a favorable data point, not a recommendation to lower the overall risk score. **Recommend updating the mitigation log rather than changing the rating.**

---

## 5. Next Steps

- **Immediate (this week):** Review proposed score changes for RISK-007, RISK-008, RISK-010, RISK-012, and RISK-015 with risk owners.
- **Short-term (within 30 days):** Draft and approve RISK-016 (Credentialing) and RISK-017 (Right of Access) entries; conduct marketing claims audit in light of FTC and multi-state AG activity; add Illinois AI Transparency Act compliance deadline (July 2026) to the regulatory calendar.
- **Medium-term (within 90 days):** Complete legal review of FDA AI/ML exemption criteria applicability to Headway's features; benchmark informed consent flows against the JMIR study recommendations; prepare for December 2026 DEA telehealth prescribing flexibility expiration.
- **Ongoing monitoring:** Texas Medical Board prescribing rule (final rule expected Q2 2026); CMS MA quality reporting final rule; permanent DEA telehealth prescribing rule development.
