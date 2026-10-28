
import heapq
from itertools import count

# 0 represents the blank tile
initial = (1, 2, 3,
           4, 5, 6,
           7, 0, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate misplaced tiles heuristic
def misplaced_tiles(state, goal):
    misplaced = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            misplaced += 1

    return misplaced


# Print the puzzle board
def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(
            "_" if tile == 0 else str(tile)
            for tile in state[i:i + 3]
        ))


# Generate neighboring states
def get_neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    neighbors = []

    for dr, dc, direction in moves:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            new_state = list(state)

            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank]
            )

            neighbors.append((tuple(new_state), direction))

    return neighbors


# Reconstruct the solution path
def reconstruct_path(parent, state):
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    return path[::-1]


# A* search using misplaced tiles
def a_star(initial, goal):
    print("A* SEARCH USING MISPLACED TILES")

    counter = count()
    open_list = []

    h = misplaced_tiles(initial, goal)

    heapq.heappush(
        open_list, (h, next(counter), 0, initial)
    )

    parent = {initial: None}
    best_g = {initial: 0}
    step = 0

    while open_list:
        f, _, g, current = heapq.heappop(open_list)

        if g != best_g.get(current):
            continue

        step += 1
        h = misplaced_tiles(current, goal)
        f = g + h

        print(f"\nSTEP {step}: CURRENT STATE")
        print_board(current)
        print(f"g(n) = {g} (cost so far)")
        print(f"h(n) = {h} (misplaced tiles)")
        print(f"f(n) = g(n) + h(n) = {g} + {h} = {f}")

        if current == goal:
            path = reconstruct_path(parent, current)

            print("\nGOAL REACHED!")
            print("Total moves:", len(path) - 1)

            print("\nFINAL SOLUTION PATH")

            for i, state in enumerate(path):
                path_g = i
                path_h = misplaced_tiles(state, goal)

                print(f"\nSolution step {i}")
                print_board(state)
                print(f"g(n) = {path_g}")
                print(f"h(n) = {path_h}")
                print(
                    f"f(n) = g(n) + h(n) "
                    f"= {path_g} + {path_h} "
                    f"= {path_g + path_h}"
                )

            print("\nStates expanded:", step)
            return

        print("\nGENERATING NEIGHBORS:")

        for neighbor, direction in get_neighbors(current):
            new_g = g + 1
            new_h = misplaced_tiles(neighbor, goal)
            new_f = new_g + new_h

            print(f"\nMove blank: {direction}")
            print_board(neighbor)
            print(f"g(n) = {new_g}")
            print(f"h(n) = {new_h}")
            print(
                f"f(n) = {new_g} + {new_h} = {new_f}"
            )

            if new_g < best_g.get(
                neighbor, float("inf")
            ):
                best_g[neighbor] = new_g
                parent[neighbor] = current

                heapq.heappush(
                    open_list,
                    (new_f, next(counter), new_g, neighbor)
                )

                print("Decision: Added to OPEN list")
            else:
                print("Decision: Ignored (no better path)")

    print("No solution found.")


# Execute the program
a_star(initial, goal)
