\"\"\"
JTBD Quality Checker - Validates JTBD statements against the 5T principles.

Checks:
1. True - Is this a genuine user job?
2. Tacit - Is this unspoken but real?
3. Touch - Does it personally affect the user?
4. Tension - Is there friction or desire?
5. Trigger - What event activates this?

Also checks for:
- No product/feature solution mentioned
- Clear context (When)
- Clear motivation (I want to)
- Clear outcome (So I can)
\"\"\"

import json
import sys
import re


# Prohibited patterns - solution language
PROHIBITED_PATTERNS = [
    r'\b(app|application|software|platform|tool)\b',
    r'\b(buy|purchase|subscribe|download|install)\b',
    r'\b(feature|functionality|capability)\b',
    r'\b(click|tap|swipe|scroll|select)\b',
]


def check_5t(statement):
    results = {}
    text = str(statement).lower()

    # True: Check if statement describes a real human activity
    results['True'] = len(text) > 30 and any(
        word in text for word in ['want', 'need', 'can', 'able', 'when', 'so that'])

    # Tacit: Check if it describes something implicit
    results['Tacit'] = any(
        word in text for word in ['without', 'instead', 'rather', 'wish', 'hope'])

    # Touch: Check if it personally involves the user
    results['Touch'] = any(
        word in text for word in ['i', 'my', 'me', 'feel'])

    # Tension: Check if there is friction or desire
    results['Tension'] = any(
        word in text for word in ['want', 'need', 'wish', 'can\'t', 'cannot', 'struggle', 'hard', 'difficult'])

    # Trigger: Check if context/situation is specified
    results['Trigger'] = text.startswith('when')

    return results


def has_solution_bias(text):
    \"\"\"Check if statement mentions a product/solution.\"\"\"
    text_lower = text.lower()
    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def validate_jtbd(jtbd):
    checks = {
        'has_when': False,
        'has_motivation': False,
        'has_outcome': False,
        'no_solution_bias': True,
        '5t_check': {},
        'issues': []
    }

    if isinstance(jtbd, dict):
        text = jtbd.get('when', '') + ' ' + jtbd.get('motivation', '') + ' ' + jtbd.get('outcome', '')
        checks['has_when'] = bool(jtbd.get('when'))
        checks['has_motivation'] = bool(jtbd.get('motivation'))
        checks['has_outcome'] = bool(jtbd.get('outcome'))
    else:
        text = str(jtbd)
        checks['has_when'] = text.lower().startswith('when')
        checks['has_motivation'] = 'want to' in text.lower()
        checks['has_outcome'] = 'so i can' in text.lower() or 'so that' in text.lower()

    checks['no_solution_bias'] = not has_solution_bias(text)
    checks['5t_check'] = check_5t(text)

    if not checks['has_when']:
        checks['issues'].append('Missing context (When)')
    if not checks['has_motivation']:
        checks['issues'].append('Missing motivation (I want to)')
    if not checks['has_outcome']:
        checks['issues'].append('Missing outcome (So I can)')
    if not checks['no_solution_bias']:
        checks['issues'].append('Contains product/solution language')

    checks['pass'] = all([
        checks['has_when'], checks['has_motivation'],
        checks['has_outcome'], checks['no_solution_bias'],
        all(checks['5t_check'].values())
    ])

    return checks


def main():
    if len(sys.argv) < 2:
        print('Usage: python jtbd_quality_checker.py <jtbd_json>')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        jtbds = json.load(f) if str(sys.argv[1]).endswith('.json') else [sys.argv[1]]

    for i, jtbd in enumerate(jtbds):
        result = validate_jtbd(jtbd)
        status = 'PASS' if result['pass'] else 'FAIL'
        print(f'JTBD {i}: {status}')
        for issue in result['issues']:
            print(f'  - {issue}')
        for t, v in result['5t_check'].items():
            icon = 'OK' if v else 'XX'
            print(f'  [{icon}] 5T-{t}')

    return 0


if __name__ == '__main__':
    main()
