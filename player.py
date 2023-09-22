class Player:
    def __init__(self, name, no, sym):
        self.name = name
        self.no = no  # player number
        self.sym = sym
        self.score = 0

    def get_move(self, gameBoard):
        valid_spot = False

        while not valid_spot:
            x = []
            x.append(int(input(self.sym + ' Row')))
            x.append(int(input(self.sym + ' Col')))
            try:
                if x not in gameBoard.emptySpot():
                    print("Invalid")
                else:
                    valid_spot = True
            except ValueError:
                print('Invalid')

        return x

    def update_score(self, gameBoard):
        if gameBoard.checkWin(self.sym):
            self.score += 1
        return self.score


class WeakComputer:
    def __init__(self):
        self.sym = 'O'

    def get_move(self, gameBoard):
        return gameBoard.randomMove()


class SmartComputer:
    def __init__(self, player):
        self.sym = 'O'
        self.player = player

    def get_move(self, board):
        if len(board.emptySpot()) == 9:
            move = board.randomMove()
        else:
            move = self.findMove(board)
        return move

    def minimax(self, board, step, isMax):
        if board.checkWin(self.player.sym):
            return -10
        if board.checkWin(self.sym):
            return 10
        if board.checkTie():
            return 0
        if isMax:
            best = -100
            for i in range(3):
                for j in range(3):
                    if board.matrix[i][j] == "":
                        board.matrix[i][j] = self.sym
                        best = max(best, self.minimax(board, step + 1, not isMax))
                        board.matrix[i][j] = ""
            return best
        else:
            best = 100
            for i in range(3):
                for j in range(3):
                    if board.matrix[i][j] == "":
                        board.matrix[i][j] = self.player.sym
                        best = min(best, self.minimax(board, step + 1, not isMax))
                        board.matrix[i][j] = ""
            return best

    def findMove(self, board):
        value = -1000
        best = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board.matrix[i][j] == "":
                    board.matrix[i][j] = self.sym
                    score = self.minimax(board, 0, False)

                    board.matrix[i][j] = ""
                    if score > value:
                        best = (i, j)
                        value = score
        return best
