from collections import deque


class NQueens:
    itr_bfs = 0
    itr_dfs = 0

    def __init__(self, size):
        self.size = size
        self.queenPosition = [0 for _ in range(size)]
        self.explored = set()

    def neighbourhood_states(self, position):
        neighbors = []
        for row in range(len(position)):
            for col in range(len(position)):
                if position[row] == col:
                    continue
                new_board = list(position)
                new_board[row] = col
                if tuple(new_board) not in self.explored:
                    neighbors.append(new_board)
        return neighbors

    def number_of_conflicts(self, position):
        size = len(position)
        conflicts = 0
        for i in range(size):
            for j in range(i + 1, size):
                if abs(position[i] - position[j]) == abs(i - j):
                    conflicts += 1

                if position[i] == position[j]:
                    conflicts += 1
        return conflicts

    def solver_DFS(self, position):
        if self.number_of_conflicts(position) == 0:
            print("Solution found as:")
            print(position)
            print(f"Solution found in : {NQueens.itr_dfs} iterations.")
            return True

        self.explored.add(tuple(position))
        next_states = self.neighbourhood_states(position)
        next_states.sort(key=lambda x: self.number_of_conflicts(x))
        print(f"next states : {next_states}")

        for pos in next_states:
            NQueens.itr_dfs += 1
            if self.solver_DFS(pos):
                return True

        return False

    def solver_BFS(self):
        queue = deque([self.queenPosition])
        while queue:
            position = queue.popleft()
            print(f"Current board: {position}")
            if self.number_of_conflicts(position) == 0:
                print("Solution found as:")
                print(position)
                print(f"Solution found in : {NQueens.itr_bfs} iterations.")
                return True

            self.explored.add(tuple(position))
            next_states = self.neighbourhood_states(position)
            next_states.sort(key=lambda x: self.number_of_conflicts(x))
            # print(f"next states : {next_states}")

            for pos in next_states:
                NQueens.itr_bfs += 1
                if tuple(pos) not in self.explored:
                    queue.append(pos)

        print("No solution found.")
        return False


def main():
    q = NQueens(8)
    # q.solver_DFS(q.queenPosition)
    q.solver_BFS()


if __name__ == "__main__":
    main()
