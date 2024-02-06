import random


class Nqueens:
    def __init__(self, size):
        self.size = size
        self.queenPosition = []
        for x in range(size):
            randomIndex = random.randint(0, size - 1)
            self.queenPosition.append((x, randomIndex))

    def pickRandomQueen(self):
        newIndex = random.randint(0, len(self.queenPosition) - 1)
        return self.queenPosition[newIndex]

    def safe_board(self):
        for pos in self.queenPosition:
            if self.gettingAttacked(pos):
                return False
        return True

    def availablePositions(self, queen_pick):
        availablePositions = []
        for x in range(self.size):
            availablePositions.append((queen_pick[0], x))
        return availablePositions

    def position_queen(self, start, to):
        assert start in self.queenPosition
        self.queenPosition.remove(start)
        self.queenPosition.append(to)

    def getAttacks(self, pos):
        assert pos in self.queenPosition
        attackCount = 0
        for queen in self.queenPosition:
            if abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos:
                attackCount += 1

            if pos[0] == queen[0] and queen != pos:
                attackCount += 1

            if pos[1] == queen[1] and queen != pos:
                attackCount += 1

        return attackCount

    def printBoard(self):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in self.queenPosition else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)

    def gettingAttacked(self, pos):
        for otherPos in self.queenPosition:
            if otherPos != pos:
                a, b = pos
                c, d = otherPos
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False
