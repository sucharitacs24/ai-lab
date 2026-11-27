
def alpha_beta(depth, node, is_maximizing, values, alpha, beta):
   
    if depth == 0:
        return values[node]

    if is_maximizing:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(
                depth - 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(
                depth - 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

depth = int(input("Enter the depth of the tree: "))

n = 2 ** depth

print("Enter", n, "leaf node values:")
values = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    values.append(value)

result = alpha_beta(
    depth,
    0,
    True,
    values,
    float('-inf'),
    float('inf')
)

print("\nOptimal value:", result)
