

from copy import deepcopy


GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

MOVES = [
    (-1, 0, "Up"),
    (1, 0, "Down"),
    (0, -1, "Left"),
    (0, 1, "Right")
]

nodes = 0


def find_empty(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j


def is_goal(grid):
    return grid == GOAL


def print_grid(grid):
    for row in grid:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


def depth_limited_search(grid, depth, path, visited):

    global nodes
    nodes += 1

    if is_goal(grid):
        return path

    if depth == 0:
        return None

    x, y = find_empty(grid)

    for dx, dy, move in MOVES:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_grid = deepcopy(grid)

            new_grid[x][y], new_grid[nx][ny] = (
                new_grid[nx][ny],
                new_grid[x][y]
            )

            state = tuple(tuple(row) for row in new_grid)

            if state not in visited:
                visited.add(state)

                result = depth_limited_search(
                    new_grid,
                    depth - 1,
                    path + [(move, new_grid)],
                    visited
                )

                if result is not None:
                    return result

                visited.remove(state)

    return None


def iddfs(start_grid, max_depth=30):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        start_state = tuple(tuple(row) for row in start_grid)
        visited = {start_state}

        result = depth_limited_search(
            start_grid,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

    return None


start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("\nINITIAL STATE:")
print_grid(start)

solution = iddfs(start)

if solution is not None:

    print("SOLUTION FOUND!")
    print("Number of moves:", len(solution))
    print("Number of nodes traversed:", nodes)
    print()

    current = start

    print("INITIAL STATE:")
    print_grid(current)

    for step, (move, grid) in enumerate(solution, start=1):

        print("Step", step, "-", move)
        print_grid(grid)

    print("FINAL GOAL STATE:")
    print_grid(GOAL)

else:
    print("No solution found within the depth limit.")
