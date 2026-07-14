---
name: jtbd-innovation-os
description: Enterprise-grade JTBD (Jobs-to-be-Done) Customer Innovation Operating System. Use when the user wants to analyze user research data, understand user needs through JTBD methodology, identify innovation opportunities, develop product concepts, create product roadmaps, or build GTM strategies grounded in user evidence. Supports multi-agent workflow from raw user data through JTBD discovery, outcome engineering, opportunity scoring, concept development, roadmap planning, and go-to-market strategy. Use for any task involving user research analysis, customer insight synthesis, product innovation, jobs-to-be-done analysis, user need discovery, product strategy, innovation opportunity identification, or evidence-driven product development.
---

# JTBD Innovation OS 4.0

Enterprise-grade AI user insight and product innovation operating system based on Jobs-to-be-Done (JTBD) 2.0 methodology.

> People do not buy products. They hire products to make progress.

## Core Philosophy

This skill is NOT a JTBD analysis prompt. It is a complete multi-agent product innovation workflow that transforms raw user data into business innovation decisions.

Key principles:
- Center all analysis on user Jobs, not product features
- Never confuse user-suggested solutions with real needs
- Focus on what users want to accomplish and how they measure success
- Use evidence-driven insights — every AI inference must be traceable to source data
- Support bilingual analysis (Chinese, English, mixed)

## Architecture Overview

The system is organized in 9 layers, from raw data to business execution:

User Data -> Layer 0 Data Understanding -> Layer 1 User Understanding -> Layer 2 Behavior Change Analysis -> Layer 3 Job Discovery -> Layer 4 Need Definition -> Layer 5 Validation -> Layer 6 Innovation Decision -> Layer 7 Product Innovation -> Layer 8 Business Execution

## Workflow

When user provides raw data (interviews, surveys, transcripts, CSV, PDF, TXT):

1. Data Understanding — Assess data quality and surface observations
2. User Understanding — Build persona profiles and context maps
3. Behavior Analysis — Detect switching behavior or job-focused patterns
4. Job Discovery — Extract JTBD statements, hierarchy, and job maps
5. Need Definition — Classify needs and engineer desired outcomes
6. Validation — Evidence-check every insight against source data
7. Innovation Decision — Score opportunities and rank priorities
8. Product Innovation — Translate to requirements, generate concepts
9. Business Execution — Build roadmap and GTM strategy

### Workflow Decision

After data quality check and initial observation:
- Behavior switch detected -> Switch Workflow (timeline + Four Forces), then JTBD extraction
- No switch detected -> Job Workflow (task interview analysis), then JTBD extraction

## Agent Directory

Each agent module at agents/ contains prompt.md, logic.md (or framework.md), and examples.md.

### Layer 0: Data Understanding
- data_quality_agent/prompt.md
- observation_agent/prompt.md

### Layer 1: User Understanding
- persona_agent/prompt.md
- context_agent/prompt.md

### Layer 2: Behavior Change
- switch_agent/prompt.md

### Layer 3: Job Discovery
- jtbd_agent/prompt.md
- job_map_agent/prompt.md

### Layer 4: Need Definition
- need_agent/prompt.md
- outcome_agent/prompt.md

### Layer 5: Validation
- evidence_validation_agent/prompt.md

### Layer 6: Innovation Decision
- opportunity_agent/prompt.md

### Layer 7: Product Innovation
- product_translation_agent/prompt.md
- concept_agent/prompt.md
- validation_agent/prompt.md

### Layer 8: Business Execution
- roadmap_agent/prompt.md
- gtm_agent/prompt.md

## Configuration

See config/ for workflow_config.yaml, scoring_config.yaml, output_schema.yaml.

## Frameworks

frameworks/ directory for on-demand reading:
- jtbd_core.md, jtbd_2.0.md, switch_interview.md, four_forces.md
- job_map.md, desired_outcome.md, odi.md, hmw.md
- star_method.md, foca_method.md, task_interview.md
- job_story.md, kano.md, kj_method.md

## Validators

validators/ contains Python scripts:
- evidence_checker.py
- jtbd_quality_checker.py
- hallucination_checker.py
- confidence_score.py

## Templates

templates/ contains structured output templates for each report type.

## Output

1. Executive Summary 2. User Understanding 3. Context Analysis 4. Switch Analysis 5. JTBD Analysis 6. Job Map 7. Need Analysis 8. Desired Outcomes 9. Evidence Appendix 10. Opportunity Ranking 11. Product Recommendation 12. Validation Plan 13. Roadmap 14. GTM Strategy

## Input Support

Formats: Excel (.xlsx, .xls), CSV, TXT, PDF, interview transcripts, survey data
Languages: Chinese, English, mixed

## Execution Rules

1. Always start with Data Quality Agent
2. Every insight must cite evidence source
3. Never generate insights without user data support
4. Tag each JTBD with evidence source, frequency, confidence
5. Check 5T principles before finalizing any JTBD
6. Score opportunities before translating to product requirements
7. Support bilingual output for mixed-language input
8. Use templates/ for structured outputs
