# import copy
# from queue import Queue
#
# size = 8
# initial_board_incremental = [['_' for j in range(size)] for i in range(size)]
# # print(initial_board_incremental)
#
# initial_board_computational = [[0, i] for i in range(8)]
#
# sol = [[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]
#
#
# # print(initial_board_computational)
#
#
# def is_safe(row, col, board):
#     for i in range(size):  # checking for the same column and row
#         if board[i][col] == 'q' and i != row:
#             return False
#         if board[row][i] == 'q' and i != col:
#             return False
#
#         # Check upper diagonal on left side
#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 'q':
#             return False
#
#         # Check lower diagonal on left side
#     for i, j in zip(range(row, size, 1), range(col, -1, -1)):
#         if board[i][j] == 'q':
#             return False
#
#         # Check upper diagonal on right side
#     for i, j in zip(range(row, -1, -1), range(col, size, 1)):
#         if board[i][j] == 'q':
#             return False
#
#         # Check lower diagonal on right side
#     for i, j in zip(range(row, size, 1), range(col, size, 1)):
#         if board[i][j] == 'q':
#             return False
#
#     return True
#
#
# def print_board(board):
#     for row in board:
#         print(row)
#
#
# def next_safest_board_incremental(board, row):
#     if row == size:  # All queens placed successfully
#         print_board(board)
#         return True
#
#     for col in range(size):
#         if is_safe(row, col, board):
#             board[row][col] = 'q'
#             if next_safest_board_incremental(copy.deepcopy(board), row + 1):
#                 return True
#             board[row][col] = '_'
#
#
# def is_safe_comp(queen_coords, board_size):
#     """
#     Checks if a given list of queen coordinates is safe on a board of size board_size.
#
#     Args:
#       queen_coords: A list of tuples, where each tuple represents the (row, col) coordinates of a queen.
#       board_size: The size of the chessboard (e.g., 8 for an 8x8 board).
#
#     Returns:
#       True if the placement is safe (no queens attack each other), False otherwise.
#     """
#
#     for i, (row1, col1) in enumerate(queen_coords):
#         # Check for other queens in the same row
#         for (row2, col2) in queen_coords[(i + 1):]:
#             if row1 == row2:
#                 return False
#
#         # Check for other queens in the same column
#         for (row2, col2) in queen_coords:
#             if col1 == col2:
#                 return False
#
#         # Check for other queens in diagonals
#         for j in range(1, board_size):
#             # Check diagonal going top-left
#             row2 = row1 - j
#             col2 = col1 - j
#             if 0 <= row2 < board_size and 0 <= col2 < board_size:
#                 if (row2, col2) in queen_coords:
#                     return False
#
#             # Check diagonal going top-right
#             row2 = row1 - j
#             col2 = col1 + j
#             if 0 <= row2 < board_size and 0 <= col2 < board_size:
#                 if (row2, col2) in queen_coords:
#                     return False
#
#             # Check diagonal going bottom-left
#             row2 = row1 + j
#             col2 = col1 - j
#             if 0 <= row2 < board_size and 0 <= col2 < board_size:
#                 if (row2, col2) in queen_coords:
#                     return False
#
#             # Check diagonal going bottom-right
#             row2 = row1 + j
#             col2 = col1 + j
#             if 0 <= row2 < board_size and 0 <= col2 < board_size:
#                 if (row2, col2) in queen_coords:
#                     return False
#
#     # No attacking queens found, so the placement is safe
#     return True
#
#
# def next_safe_computational(places):
#     next_safes = []
#
#     for i in range(8):
#         temp = copy.deepcopy(places)
#         temp[i][0] += 1
#         if temp[i][0] < size:
#             next_safes.append(temp)
#     return next_safes
#
#
# def bfs(initial_state):
#     frontier = Queue()  # Use a queue for BFS
#     frontier.put(initial_state)
#     explored = []
#
#     while not frontier.empty():
#         state = frontier.get()
#         if is_safe_comp(state, size):
#             print(state)
#             return
#
#         if state == sol:
#             print("State found")
#             print(state)
#             return
#         explored.append(state)
#         for successor in next_safe_computational(state):
#             if successor not in explored:
#                 frontier.put(successor)
#                 print(successor)
#     return None
#
#
# def dfs(state, explored):
#     if is_safe_comp(state, size):
#         print(state)
#         return True
#     for successor in next_safe_computational(state):
#         if successor not in explored:
#             print(successor)
#         if dfs(successor, explored):
#             break
#
#
# def main():
#     # cur_row = 0
#     # # this is for the incremental state.
#     # board = initial_board_incremental
#     # next_safest_board_incremental(board, cur_row)
#
#     # bfs(initial_board_computational)
#     explored = []
#     dfs(initial_board_computational, explored)
#
#
# if __name__ == "__main__":
#     main()
# import copy
#
# size = 8
#
#
# class Board:
#     # store only the y index of the queens.
#     def __init__(self, queens):
#         self.size = size
#         self.queens = queens
#         self.parent = None
#
#
# class Solver:
#     def __init__(self):
#         self.explored = []
#         self.solution = []
#         self.iter = 0
#         self.start_board = Board([i for i in range(size)])
#         self.solver_logic(self.start_board)
#
#     # we need to check the diagonals and rows and columns.
#     def is_safe(self, board):
#         for i in range(len(board.queens)):
#             for j in range(i + 1, len(board.queens)):
#                 # Check if queens are in the same column or on the same diagonal
#                 if board.queens[i] == board.queens[j] or abs(board.queens[i] - board.queens[j]) == j - i:
#                     return False
#
#         return True
#
#     def check_explored(self, board):
#         for temp in self.explored:
#             if board.queens == temp.queens:
#                 return True
#         return False
#
#     # generating the next states.
#     # def next_states_incremental(self, board):
#     #     next_states = []
#     #     for i in range(board.size):
#     #         temp = copy.deepcopy(board.queens)
#     #         # move every queen by one.
#     #         temp[i] += 1
#     #         if temp[i] < board.size:
#     #             next_states.append(Board(temp))
#     #     return next_states
#     def next_states_incremental(self, board):
#         next_states = []
#         for i in range(board.size):
#             for j in range(board.size):
#                 temp = copy.deepcopy(board.queens)
#                 temp[i] = j
#                 t_board = Board(temp)
#                 if not self.check_explored(t_board):
#                     next_states.append(t_board)
#         return next_states
#
#     def solver_logic(self, board):
#         if self.is_safe(board):
#             temp = board
#             while temp is not None:
#                 self.solution.append(temp.queens)
#                 temp = temp.parent
#             self.solution = self.solution[::-1]
#
#             return True
#
#         self.explored.append(board)
#         print(board.queens)
#
#         for state in self.next_states_incremental(board):
#             if not self.check_explored(state):
#                 self.iter += 1
#                 state.parent = board
#                 if self.solver_logic(state):
#                     return True
#
#
# def main():
#     AI = Solver()
#     print(AI.iter)
#     print(AI.solution)
#
#
# if __name__ == "__main__":
#     main()

from queue import Queue


class NQueens:

    def __init__(self, size):
        self.size = size

    def solve_dfs(self):
        if self.size < 1:
            return []
        solutions = []
        stack = [[]]
        while stack:
            solution = stack.pop()
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                stack.append(queens)
        return solutions

    def solve_bfs(self):
        if self.size < 1:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solution = queue.get()
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                queue.put(queens)
        return solutions

    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)


def main():
    print('.: N-Queens Problem :.')
    size = int(input('Please enter the size of board: '))
    print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    n_queens = NQueens(size)
    dfs_solutions = n_queens.solve_dfs()
    bfs_solutions = n_queens.solve_bfs()
    if print_solutions:
        for i, solution in enumerate(dfs_solutions):
            print('DFS Solution %d:' % (i + 1))
            n_queens.print(solution)
        for i, solution in enumerate(bfs_solutions):
            print('BFS Solution %d:' % (i + 1))
            n_queens.print(solution)
    print('Total DFS solutions: %d' % len(dfs_solutions))
    print('Total BFS solutions: %d' % len(bfs_solutions))


if __name__ == '__main__':
    main()


# def solve_n_queens(N):
#     # Initialize the board
#     board = [-1] * N
#
#     def is_safe(board, column):
#         for i in range(column):
#             if board[i] == board[column] or \
#                 board[i] - i == board[column] - column or \
#                 board[i] + i == board[column] + column:
#                 return False
#         return True
#
#     def place_queen(board, current_column):
#         if current_column == N:
#             print_board(board)
#             return
#
#         for i in range(N):
#             board[current_column] = i
#             if is_safe(board, current_column):
#                 place_queen(board, current_column + 1)
#
#     def print_board(board):
#         for row in range(N):
#             line = ""
#             for column in range(N):
#                 if board[column] == row:
#                     line += "Q "
#                 else:
#                     line += ". "
#             print(line)
#         print("\n")
#
#     place_queen(board, 0)
#
# # Test the function
# solve_n_queens(8)
