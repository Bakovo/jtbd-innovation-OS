\"\"\"
Opportunity Scoring Engine - Scores and ranks innovation opportunities.

Computes weighted scores across 7 dimensions using configurable weights.
Usage: python scoring.py <opportunities_json> [scoring_config_yaml]
\"\"\"

import json
import sys

# Default weights from scoring_config.yaml
DEFAULT_WEIGHTS = {
    'user_importance': 1.5,
    'dissatisfaction': 1.3,
    'frequency': 1.2,
    'market_size': 1.0,
    'business_value': 1.0,
    'strategic_fit': 0.8,
    'technical_feasibility': 0.7,
}

CATEGORY_THRESHOLDS = [
    ('Core Opportunity', 7.0),
    ('Adjacent Opportunity', 5.0),
    ('Exploratory Opportunity', 0.0),
]


def score_opportunity(opportunity, weights=None):
    if weights is None:
        weights = DEFAULT_WEIGHTS

    scores = opportunity.get('scores', {})
    total_weight = 0.0
    weighted_sum = 0.0

    for dim, weight in weights.items():
        score = scores.get(dim, 0)
        if isinstance(score, (int, float)) and 1 <= score <= 10:
            weighted_sum += score * weight
            total_weight += weight

    avg_score = weighted_sum / total_weight if total_weight > 0 else 0

    category = 'Exploratory Opportunity'
    for cat_name, threshold in sorted(CATEGORY_THRESHOLDS, key=lambda x: -x[1]):
        if avg_score >= threshold:
            category = cat_name
            break

    return {
        'id': opportunity.get('id', 'unknown'),
        'name': opportunity.get('name', 'Unnamed'),
        'weighted_score': round(avg_score, 2),
        'dimension_scores': scores,
        'category': category,
        'evidence_strength': opportunity.get('evidence_strength', 'weak'),
    }


def main():
    if len(sys.argv) < 2:
        print('Usage: python scoring.py <opportunities_json>')
        print('Input format: JSON array of opportunity objects')
        print('  Each opportunity: {"id": "...", "name": "...", "scores": {...}, "evidence_strength": "..."}')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        opportunities = json.load(f)

    results = [score_opportunity(opp) for opp in opportunities]
    results.sort(key=lambda x: -x['weighted_score'])

    for i, r in enumerate(results, 1):
        print(f'{i}. [{r[\"category\"]}] {r[\"name\"]} (Score: {r[\"weighted_score\"]})')
        print(f'   Evidence: {r[\"evidence_strength\"]}')

    # Output JSON for downstream agents
    output_path = sys.argv[2] if len(sys.argv) > 2 else 'scored_opportunities.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({'ranked_opportunities': results, 'count': len(results)}, f, ensure_ascii=False, indent=2)

    print(f'\nSaved ranked opportunities to {output_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
