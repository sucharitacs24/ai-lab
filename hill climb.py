
import random

N = 4  


def heuristic(board):
   
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (board[i] == board[j] or
                    abs(board[i] - board[j]) == j - i):
                conflicts += 1

    return conflicts


def print_board(board):
    for row in range(N):
        line = ""
        for col in range(N):
            if board[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()


def hill_climbing():
  
    board = [random.randrange(N) for _ in range(N)]

    g = 0
    step = 0

    while True:
        step += 1
        h = heuristic(board)
        f = g + h

        print(f"STEP {step}")
        print_board(board)

        print(f"g(n) = {g} (moves made)")
        print(f"h(n) = {h} (attacking pairs)")
        print(f"f(n) = g(n) + h(n) = {g} + {h} = {f}")

        if h == 0:
            print("Solution found!")
            print("Total moves:", g)
            return

        best_board = board[:]
        best_h = h

        for col in range(N):
            original_row = board[col]

            for row in range(N):
                if row == original_row:
                    continue

                candidate = board[:]
                candidate[col] = row
                candidate_h = heuristic(candidate)

                print(
                    f"Move queen in column {col} "
                    f"to row {row}: "
                    f"g(n)={g + 1}, h(n)={candidate_h}, "
                    f"f(n)={g + 1 + candidate_h}"
                )

                if candidate_h < best_h:
                    best_h = candidate_h
                    best_board = candidate

        
        if best_h >= h:
            print("No better neighbor found.")
            print("Hill climbing reached a local minimum.")
            print("Restarting with a random board...\n")
            board = [
                random.randrange(N) for _ in range(N)
            ]
            g = 0
            continue

        board = best_board
        g += 1


hill_climbing()
