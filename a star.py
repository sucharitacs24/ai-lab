import heapq
from itertools import count

initial = (1, 2, 3,
           4, 5, 6,
           7, 0, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan_distance(state, goal):
    """Calculate the Manhattan distance heuristic."""
    goal_positions = {
        tile: divmod(i, 3)
        for i, tile in enumerate(goal)
    }

    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        row, col = divmod(i, 3)
        goal_row, goal_col = goal_positions[tile]

        distance += (
            abs(row - goal_row)
            + abs(col - goal_col)
        )

    return distance


def get_neighbors(state):
    """Generate all valid states by moving the blank."""
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0), 
        (1, 0), 
        (0, -1),
        (0, 1) 
    ]

    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def reconstruct_path(parent, state):
    """Trace parent links from goal to initial state."""
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    return path[::-1]


def a_star(initial, goal):
    """Find the shortest path using A* search."""

    counter = count()
    open_list = []

    heapq.heappush(
        open_list,
        (
            manhattan_distance(initial, goal),
            next(counter),
            0,
            initial
        )
    )

    parent = {initial: None}
    best_g = {initial: 0}
    explored = 0

    while open_list:
        f, _, g, current = heapq.heappop(open_list)

        if g != best_g.get(current):
            continue

        explored += 1

        if current == goal:
            path = reconstruct_path(parent, current)
            return path, explored

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                parent[neighbor] = current

                h = manhattan_distance(neighbor, goal)
                new_f = new_g + h

                heapq.heappush(
                    open_list,
                    (
                        new_f,
                        next(counter),
                        new_g,
                        neighbor
                    )
                )

    return None, explored


def print_board(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join(
            "_" if tile == 0 else str(tile)
            for tile in row
        ))
    print()
path, explored = a_star(initial, goal)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:
        print_board(state)

    print("States explored:", explored)
else:
    print("No solution found.")