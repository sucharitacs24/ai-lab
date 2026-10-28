
import random


def heuristic(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def get_neighbors(state):
    neighbors = []
    n = len(state)

    for col in range(n):
        for row in range(n):
            if row != state[col]:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)

    return neighbors


def hill_climbing():
    state = [random.randint(0, 3) for _ in range(4)]

    while True:
        h = heuristic(state)
        print("State:", [x + 1 for x in state], "Heuristic:", h)

        if h == 0:
            print("Solution found!")
            return state

        neighbors = get_neighbors(state)
        best_neighbor = min(neighbors, key=heuristic)

        if heuristic(best_neighbor) >= h:
            print("Local optimum reached. Restarting...")
            state = [random.randint(0, 3) for _ in range(4)]
        else:
            state = best_neighbor


solution = hill_climbing()

print("Final solution:", [x + 1 for x in solution])