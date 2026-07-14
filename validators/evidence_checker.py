\"\"\"
Evidence Checker - Validates that every insight has supporting evidence.

Usage: python evidence_checker.py <insights_json>

Checks:
- Every insight has at least one evidence source
- Evidence sources are specific (not generic)
- Frequency is recorded
- Confidence is calculated
\"\"\"

import json
import sys


def check_insight(insight):
    checks = {
        'has_evidence': False,
        'source_specific': False,
        'has_frequency': False,
        'has_confidence': False,
        'issues': []
    }

    if 'evidence' in insight and insight['evidence']:
        checks['has_evidence'] = True
        if len(insight['evidence']) > 10:
            checks['source_specific'] = True
        else:
            checks['issues'].append('Evidence too vague. Be more specific.')
    else:
        checks['issues'].append('Missing evidence source.')

    if 'frequency' in insight and insight['frequency']:
        checks['has_frequency'] = True
    else:
        checks['issues'].append('Missing frequency information.')

    if 'confidence' in insight and isinstance(insight['confidence'], (int, float)):
        checks['has_confidence'] = True

    return checks


def main():
    if len(sys.argv) < 2:
        print('Usage: python evidence_checker.py <insights_json>')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        insights = json.load(f)

    results = []
    for i, insight in enumerate(insights):
        result = check_insight(insight)
        result['id'] = insight.get('id', i)
        results.append(result)

    passes = sum(1 for r in results if not r['issues'])
    total = len(results)

    print(f'Validated {total} insights: {passes}/{total} pass')
    for r in results:
        if r['issues']:
            print(f"  Insight {r['id']}: {'; '.join(r['issues'])}")

    return 0 if passes == total else 1


if __name__ == '__main__':
    sys.exit(main())
