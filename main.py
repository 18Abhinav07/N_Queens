from solver import *


def main():
    n = 8
    solver = Nqueens(n)

    while not solver.safe_board():
        # these are the maximum possible attacks.
        possible_attacks = n + 1

        queen_pick = solver.pickRandomQueen()
        available_positions = solver.availablePositions(queen_pick)

        safest_position = (-1, -1)

        for pos in available_positions:
            # move the queen to that pos and check for conflicts.
            solver.position_queen(queen_pick, pos)

            attacks = solver.getAttacks(pos)
            if attacks < possible_attacks:
                possible_attacks = attacks
                safest_position = pos

            solver.position_queen(pos, queen_pick)

        solver.position_queen(queen_pick, safest_position)
        print(solver.queenPosition)
    solver.printBoard()
    print(solver.queenPosition)


if __name__ == "__main__":
    main()
