# Example Prompts for Building with Claude

These are ready-to-use prompts demonstrating what you can build with Claude. Each references an actual project file in this folder.

---

## 1. NPS Dashboard

**What this does:** Takes raw NPS survey data and turns it into a polished, interactive HTML dashboard — no spreadsheet required.

**The prompt:**

```
I have a CSV file called nps_and_descriptions_only.csv that contains NPS survey data from Every subscribers. Each row has a numeric NPS score (0-10) and an open-ended text response to the question "How would you describe Every?"

Please analyze this data and build a single self-contained HTML dashboard that does the following:

1. Calculates and prominently displays the overall NPS score (% Promoters minus % Detractors, where 0-6 = Detractors, 7-8 = Passives, 9-10 = Promoters)
2. Shows a bar chart of the score distribution (how many respondents gave each score 0-10)
3. Shows a donut or pie chart breaking down the three segments (Promoters, Passives, Detractors) with their percentages
4. Reads through all the open-ended descriptions and groups them into 4-6 meaningful themes (e.g., "high-quality writing", "practical business advice", "smart founders", etc.) — show a theme breakdown with representative quotes for each
5. Surfaces the top 5 most positive and top 5 most critical verbatim quotes in a side-by-side display
6. Uses a clean, modern dark-themed design with Every's aesthetic (dark background, clean typography, subtle card borders)
7. Is entirely self-contained in one HTML file using Chart.js from a CDN — no external dependencies needed beyond that

The goal is something I could present in a board meeting or share with the team as a link. Make it look professional and polished.
```

---

## 2. Landing Page Modification

**What this does:** Takes an existing landing page and makes targeted improvements — demonstrating how Claude can edit and extend real code, not just generate from scratch.

**The prompt:**

```
I have an HTML file called every-landing.html — it's a landing page for "Learn Claude Code in One Day" by Every. Please open it and make the following changes:

1. Add a testimonials section between the Agenda section and the FAQ section. Create 4 fictional but realistic testimonials from past attendees with names, titles, and companies that feel authentic (e.g., a VC, a startup founder, a product leader, a marketing executive). Style it to match the existing dark aesthetic.

2. The hero section currently has a single CTA button — add a secondary "Learn More" link next to it that smoothly scrolls down to the About section.

3. Make the page fully responsive for mobile (under 768px). Right now the agenda table and the two-column sections break on small screens — fix the layout so it stacks cleanly on mobile with readable font sizes.

4. Add a sticky top navigation bar that appears after the user scrolls past the hero section. It should show the Every logo on the left and anchor links to the main sections (About, Agenda, FAQ) on the right, with a subtle blur/frosted glass background.

5. Keep all existing content and styling exactly as-is — only add the new elements and fix the responsive issues. Do not change the color scheme, fonts, or any existing copy.

Return the complete updated every-landing.html file.
```

---

## 3. Hidden Gems Vacation Guide

**What this does:** Generates a complete, beautiful interactive travel guide for any city — the kind of thing that normally takes a designer and developer days to build. Great for personal trips, team offsites, or sharing with friends.

**The prompt:**

```
I have a file called hoboken-hidden-gems.html — it's an interactive local guide I built for Hoboken, NJ. It has a vintage aesthetic, a Leaflet.js map with pinned locations, category filters (restaurants, bars, parks, family activities), and card-based listings with descriptions and tips.

I want you to build something nearly identical but for Kyoto, Japan — tailored for a 5-day trip in late March (cherry blossom season).

Here's what I need:

1. Use the same vintage-styled design as the Hoboken guide — warm cream/sepia background, hand-drawn-style borders, serif typography, the whole aesthetic
2. Include a Leaflet.js map centered on Kyoto with pins for each recommendation
3. Include these categories with 4-6 recommendations each:
   - Hidden Temples & Shrines (lesser-known spots beyond the tourist classics)
   - Local Food & Markets (great places to eat that aren't on every "best of" list)
   - Traditional Crafts & Shops (pottery, textiles, knives, etc.)
   - Day Trips (Nara, Osaka, Uji — with tips on timing and getting there)
   - Cherry Blossom Spots (ranked by crowd level, best time of day to visit)
4. Each card should have: name, neighborhood, a 2-3 sentence description, a practical tip ("Pro tip: go before 8am"), and realistic coordinates for the map pin
5. Add a filter bar at the top so you can show/hide categories
6. Make it fully self-contained in one HTML file — all CSS and JS inline, Leaflet loaded from CDN

Generate realistic, specific, useful recommendations — not generic tourist advice. The goal is something that feels like it was made by a local who really knows the city.
```

---

## 4. Therapist Directory — Add a Feature

**What this does:** Takes an existing therapist search page and adds a new feature — showing how Claude can work with real multi-file web projects (HTML + a JavaScript database of 132 providers).

**The prompt:**

```
I have a therapist directory built with three files:
- therapists-index.html — the main search/browse page for finding family counselors in New York
- therapists-provider.html — the individual provider detail page
- therapists-db.js — a JavaScript file containing data for 132 therapists (names, specialties, insurance accepted, locations, bios, therapy methods, etc.)

I'd like you to make the following changes to the directory:

1. Add a "Compare Therapists" feature — let users select 2-3 therapists from the search results and see them side-by-side in a comparison view showing: specialties, therapy methods, insurance accepted, years of experience, and availability. Add a subtle checkbox or "Compare" button to each therapist card, and a floating comparison bar at the bottom when therapists are selected.

2. Add a "Best Match" sorting option that considers multiple factors: years of experience, number of specialties relevant to family counseling, number of insurance plans accepted, and whether they offer virtual sessions. Show a match score on each card when this sort is active.

3. Keep all existing styling and functionality intact — just add these new features on top.

Return the updated therapists-index.html file.
```

---

## 5. Therapist Database Analysis

**What this does:** Analyzes the therapist database to surface workforce insights — the kind of analysis that would normally require SQL queries or a data team.

**The prompt:**

```
I have a file called therapists-db.js that contains a JavaScript array of 132 therapist records from Headway's provider network in New York. Each therapist record includes: name, license type, location, years of experience, specialties, therapy methods, care types (individual, couples, family), ages served, languages spoken, insurance plans accepted, whether they offer virtual sessions, and their bio.

Please analyze this dataset and produce a comprehensive workforce insights report covering:

1. **Network Composition** — Break down the provider network by license type (LCSW, LMHC, PhD, PsyD, etc.), years of experience distribution, and care type availability. What's our mix?

2. **Specialty Coverage** — Which specialties are most and least represented? Are there gaps? For example, how many therapists list "Substance use / addiction" vs "Anxiety"? Create a ranked list.

3. **Insurance Coverage** — Which insurance plans have the most in-network providers? Which plans have the fewest? Flag any plans with critically low coverage (fewer than 10 providers).

4. **Access & Diversity** — What languages are available beyond English? How many providers offer virtual sessions? What age groups are underserved?

5. **Competitive Insights** — Based on the bios and therapy methods, what therapeutic approaches are trending in our network (e.g., CBT, DBT, EMDR, psychodynamic)? Which approaches might we want to recruit more of?

6. **Recommendations** — Based on the gaps you find, recommend 5 specific recruiting priorities (e.g., "Recruit 3+ Spanish-speaking LMFTs specializing in family therapy who accept Medicaid").

Format this as a clean executive summary I could share with our clinical leadership team. Include actual numbers and percentages, not just generalizations.
```
