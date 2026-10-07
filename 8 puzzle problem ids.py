N = 3

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, N)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < N and 0 <= nc < N:
            new_zero = nr * N + nc

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def depth_limited_search(state, depth, path, visited):

    if state == GOAL:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for next_state in get_neighbors(state):

        if next_state not in visited:

            result = depth_limited_search(
                next_state,
                depth - 1,
                path + [next_state],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


def iterative_deepening(start):

    for depth in range(50):

        result = depth_limited_search(
            start,
            depth,
            [start],
            set()
        )

        if result is not None:
            return result

    return None


def print_state(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()




print("Enter the initial state (use 0 for blank):")

values = list(map(int, input().split()))

if len(values) != 9:
    print("Please enter exactly 9 numbers.")
    exit()

start = tuple(values)

print("\nInitial State:")
print_state(start)

solution = iterative_deepening(start)

if solution:

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for i, state in enumerate(solution):

        print("Step", i)
        print_state(state)

else:
    print("No solution found.")
