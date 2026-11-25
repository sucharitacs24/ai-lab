from itertools import product
import re

def evaluate(expression, values):
    for variable, value in values.items():
        expression = re.sub(r'\b' + variable + r'\b', str(value), expression)
    expression = expression.replace('&', ' and ')
    expression = expression.replace('|', ' or ')
    expression = expression.replace('~', ' not ')
    expression = expression.replace('>>', ' <= ')
    return eval(expression)

kb = input("Enter Knowledge Base (use & for AND, | for OR, ~ for NOT, >> for IMPLIES): ")
query = input("Enter Query: ")

expressions = [kb, query]
variables = sorted(set(re.findall(r'\b[A-Z]\b', ' '.join(expressions))))

print("\nTruth Table:")
print(" | ".join(variables + ["KB", "Query"]))

entailed = True
found_model = False

for combination in product([True, False], repeat=len(variables)):
    values = dict(zip(variables, combination))

    kb_result = evaluate(kb, values)
    query_result = evaluate(query, values)

    if kb_result:
        found_model = True
        if not query_result:
            entailed = False

    row = [str(values[v]) for v in variables]
    row.extend([str(kb_result), str(query_result)])
    print(" | ".join(row))

print("\nResult:")

if not found_model:
    print("Knowledge Base is UNSATISFIABLE")
elif entailed:
    print("Query is ENTAILED by Knowledge Base")
else:
    print("Query is NOT ENTAILED by Knowledge Base")