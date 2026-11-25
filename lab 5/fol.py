import re

def parse_expression(expr):
    match = re.match(r'(\w+)\((.*)\)', expr.strip())
    if not match:
        return None, []
    predicate = match.group(1)
    args = [x.strip() for x in match.group(2).split(',')]
    return predicate, args

def is_variable(term):
    return term.islower() and term.isalpha()

def occurs(variable, term, substitution):
    term = apply_substitution(term, substitution)
    return variable == term

def apply_substitution(term, substitution):
    while term in substitution:
        term = substitution[term]
    return term

def unify_terms(x, y, substitution):
    x = apply_substitution(x, substitution)
    y = apply_substitution(y, substitution)

    if x == y:
        return True

    if is_variable(x):
        if occurs(x, y, substitution):
            return False
        substitution[x] = y
        return True

    if is_variable(y):
        if occurs(y, x, substitution):
            return False
        substitution[y] = x
        return True

    return False

def unify(expr1, expr2):
    pred1, args1 = parse_expression(expr1)
    pred2, args2 = parse_expression(expr2)

    if pred1 is None or pred2 is None:
        return None

    if pred1 != pred2 or len(args1) != len(args2):
        return None

    substitution = {}

    for x, y in zip(args1, args2):
        if not unify_terms(x, y, substitution):
            return None

    return substitution

expr1 = input("Enter first expression: ")
expr2 = input("Enter second expression: ")

result = unify(expr1, expr2)

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitution:", result)

    pred, args = parse_expression(expr1)
    unified_args = [apply_substitution(arg, result) for arg in args]

    print("Unified Expression:", pred + "(" + ", ".join(unified_args) + ")")










