# Opportunity and Decision Intelligence (ODI)

## Purpose

Score and prioritize innovation opportunities based on multiple dimensions.

## Scoring Dimensions

1. User Importance
2. Dissatisfaction (with current solutions)
3. Frequency (of the job occurrence)
4. Market Size (addressable users)
5. Business Value (revenue/margin potential)
6. Strategic Fit (alignment with business strategy)
7. Technical Feasibility (can we build it?)

## Scoring Process

1. Score each dimension 1-10
2. Apply weight from scoring_config.yaml
3. Calculate weighted average
4. Classify into category (Core/Adjacent/Exploratory)
5. Rank all opportunities

## Decision Framework

- Core (7.0+): High priority, strong evidence, immediate investment
- Adjacent (5.0-6.9): Medium priority, needs validation
- Exploratory (<5.0): Low priority, research phase
