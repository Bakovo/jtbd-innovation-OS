\"\"\"
Hallucination Checker - Prevents AI from generating insights without user data support.

This validator checks generated outputs to ensure every claim traces back to source data.
\"\"\"

import json
import sys


# Generic phrases that indicate AI hallucination
GENERIC_PATTERNS = [
    'many users', 'users often', 'commonly', 'typically',
    'research shows', 'studies indicate',
    'in my experience', 'based on my knowledge'
]


def check_hallucination(output_text, evidence_refs):
    \"\"\"Check for hallucination indicators.\"\"\"
    issues = []
    text = str(output_text).lower()

    # Check for generic phrases
    for pattern in GENERIC_PATTERNS:
        if pattern in text:
            issues.append(f'Generic phrase detected: "{pattern}"')

    # Check evidence density
    evidence_count = len(evidence_refs) if isinstance(evidence_refs, list) else 0
    if evidence_count == 0:
        issues.append('No evidence references found')

    return {
        'has_hallucination_risk': len(issues) > 0,
        'issues': issues,
        'evidence_count': evidence_count
    }


def main():
    if len(sys.argv) < 2:
        print('Usage: python hallucination_checker.py <output_file> [evidence_file]')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        output = f.read()

    refs = []
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            refs = json.load(f)

    result = check_hallucination(output, refs)
    if result['has_hallucination_risk']:
        print('WARNING: Hallucination risk detected')
        for issue in result['issues']:
            print(f'  - {issue}')
    else:
        print('OK: No hallucination risk detected')

    print(f'Evidence count: {result["evidence_count"]}')
    return 1 if result['has_hallucination_risk'] else 0


if __name__ == '__main__':
    sys.exit(main())
