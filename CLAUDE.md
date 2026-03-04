# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Workshop materials for the Headway x Every executive AI offsite. Contains **synthetic data** and **example prompts** organized by executive, plus example Claude Code extensions (skill, subagent, MCP server).

The audience is non-technical C-suite executives at Headway (a mental health tech company). Everything should be simple, practical, and jargon-free.

## Repo Structure

- `RS/`, `NC/`, `LB/`, `OMD/` — Executive folders with synthetic CSV/JSON/MD data files and an `example_prompts.md` with copy-paste-ready prompts for each exec's projects
- `MT/` — Facilitator demo projects (NPS dashboard, landing page, Hoboken guide, therapist directory)
- `examples/` — Three beginner-friendly Claude Code extension templates (skill, subagent, MCP server), each with its own README

## Key Conventions

- **Headway context:** Mental health tech company connecting therapists with insurance. Key systems referenced: Snowflake, Jira, Greenhouse, Workday, Sigmund (EHR). Payers include Aetna, Cigna, UnitedHealthcare, BCBS, Anthem, Humana, Kaiser, etc.
- **Data files within each exec folder are internally consistent** — names, numbers, and narratives cross-reference across files in the same folder.
- **Example prompts reference specific filenames** in their folder. If renaming data files, update the corresponding `example_prompts.md`.
- HTML files in MT/ are self-contained single-file apps (inline CSS/JS, CDN dependencies only). The therapist directory is a 3-file set: `therapists-index.html`, `therapists-provider.html`, and `therapists-db.js`.

## When Adding or Modifying Content

- Keep language accessible for executive-level users, trying claude code for the first time (assume non-technical)
- Maintain internal consistency within each exec's folder (cross-reference names, figures, dates)
- Update `README.md` file tables if adding/removing data files
