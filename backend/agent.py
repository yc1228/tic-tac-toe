import time


class Agent(object):
    def __init__(self, board):
        self.board = board

    def next_move(self):
        time.sleep(2)
        print(self.board)
        return self.board

    def check_winner(self):
        pass
