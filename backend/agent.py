import time


class Agent(object):
    def __init__(self, board):
        self.board = board
        if self.board.count('X') >= self.board.count('O'):
            self.player = 'O'
            self.opponent = 'X'
        else:
            self.player = 'X'
            self.opponent = 'O'

    def next_move(self):
        time.sleep(2)
        print(self.board)
        return self.board

    def check_winner(self):
        winstate = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
        for win in winstate:
            if self.board[win[0]] == 'X' or self.board[win[0]] == 'O':
                if self.board[win[0]] == self.board[win[1]] and self.board[win[1]] == self.board[win[2]]:
                    return self.board[win[0]]

    def score(self, depth):
        if Agent.check_winner(self) == self.player:
            return 10 - depth
        else:
            return depth - 10
