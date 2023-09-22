import random

WINCASE = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]]
]


class Board:
    def __init__(self, row, col):
        self.currentWinner = None
        self.row = row
        self.col = col
        self.matrix = []
        for r in range(self.row):
            self.matrix.append([])
            for c in range(self.col):
                self.matrix[r].append("")

    def printBoard(self):
        s = ''
        for r in range(self.row):
            for c in range(self.col):
                if c != 2:
                    s += "\t" +str(self.matrix[r][c]) + "\t|"
                else:
                    s += "\t" + str(self.matrix[r][c])
            if r !=2:
                s+= '\n-------------------------\n'
            else:
                s+='\n'
        return s

    def makePlay(self, row, col, sym):
        if self.matrix[row][col] == "":
            self.matrix[row][col] = sym
            return True
        return False

    def checkWin(self, sym):
        for i in range(len(WINCASE)):
            count = 0
            for j in range(len(WINCASE[i])):
                if self.matrix[WINCASE[i][j][0]][WINCASE[i][j][1]] == sym:
                    count += 1
            if count == 3:
                return True
        return False

    def emptySpot(self):
        empty = []
        for i in range(self.row):
            for j in range(self.col):
                if self.matrix[i][j] == "":
                    empty.append([i, j])

        return empty

    def randomMove(self):
        return random.choice(self.emptySpot())

    def checkTie(self):
        if len(self.emptySpot()) == 0:
            return True
        return False


