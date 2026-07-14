\"\"\"
Confidence Score Calculator - Computes confidence scores based on evidence strength.

Factors:
- Evidence count (number of supporting data points)
- Evidence diversity (multiple users vs single)
- Evidence specificity (direct quotes vs general patterns)
- Source quality (interview vs survey vs review)
- Consistency (across users)

Usage: python confidence_score.py <insights_json>
\"\"\"

import json
import sys


def calculate_confidence(insight):
    score = 0.0
    factors = []

    # Factor 1: Evidence count
    evidence_count = len(insight.get('evidence_sources', []))
    if evidence_count >= 5:
        score += 0.3
        factors.append('count:5+')
    elif evidence_count >= 3:
        score += 0.2
        factors.append('count:3-4')
    elif evidence_count >= 1:
        score += 0.1
        factors.append('count:1-2')
    else:
        factors.append('count:0')

    # Factor 2: Evidence diversity (multiple users)
    if insight.get('frequency') == 'pattern_across_users':
        score += 0.3
        factors.append('pattern')
    elif insight.get('frequency') == 'multiple_mentions':
        score += 0.2
        factors.append('multi_mention')
    elif insight.get('frequency') == 'single_mention':
        score += 0.1
        factors.append('single')

    # Factor 3: Source quality
    source_type = insight.get('source_type', '')
    if source_type in ('interview', 'observation'):
        score += 0.2
        factors.append('high_quality_source')
    elif source_type in ('survey', 'review'):
        score += 0.15
        factors.append('medium_quality_source')

    # Factor 4: Has direct quotes
    if insight.get('has_direct_quotes', False):
        score += 0.2
        factors.append('direct_quotes')

    return {
        'score': min(score, 1.0),
        'factors': factors,
        'label': 'Strong' if score >= 0.7 else 'Moderate' if score >= 0.4 else 'Weak'
    }


def main():
    if len(sys.argv) < 2:
        print('Usage: python confidence_score.py <insights_json>')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        insights = json.load(f)

    for i, insight in enumerate(insights):
        result = calculate_confidence(insight)
        print(f'Insight {i}: {result["label"]} (score: {result["score"]:.2f})')
        print(f'  Factors: {\", \".join(result[\"factors\"])}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
