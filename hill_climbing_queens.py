import random

explored = set()


def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]


def conflicts(board):
    total = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                total += 1
            offset = j - i
            if abs(board[i] - board[j]) == offset:
                total += 1
    return total


def get_neighbors(board):
    neighbors = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                continue
            new_board = list(board)
            new_board[row] = col
            if tuple(new_board) not in explored:
                neighbors.append(new_board)
    return neighbors


def hill_climbing(board, itr):
    while True:
        itr += 1
        neighbors = get_neighbors(board)
        current_conflicts = conflicts(board)
        if not neighbors:
            break

        neighbors.sort(key=lambda x: conflicts(x))
        if conflicts(neighbors[0]) >= current_conflicts:
            break

        board = neighbors[0]
        explored.add(tuple(board))
    return board, itr


best_board = None
best_conflicts = None
itr = 0
while True:
    initial_board = [0, 0, 0, 0, 0, 0, 0, 0]
    solution, itr = hill_climbing(initial_board, itr)
    num_conflicts = conflicts(solution)
    if best_conflicts is None or num_conflicts < best_conflicts:
        best_board = solution
        best_conflicts = num_conflicts

    if num_conflicts == 0:
        break;
print("Best solution:", best_board, "Conflicts:", best_conflicts)
print(itr)
