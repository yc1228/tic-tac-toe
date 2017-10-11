import time


class Agent(object):
    def __init__(self, board):
        self.board = board
        self.choice = None
        if self.board.count('X') >= self.board.count('O'):
            self.player = 'O'
        else:
            self.player = 'X'

    def next_move(self):
        time.sleep(2)
        best = -100
        Agent.minimax(self, 1, self.player, best)
        if Agent.game_over(self) is True:
            print('Game Over!')
            return self.board
        # print(self.choice)
        self.board[self.choice] = self.player
        print("Next Move: ")
        #self.board[self.choice] = self.player
        print(self.board)
        return self.board

    def check_winner(self):
        winstate = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8],
                    [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
        for win in winstate:
            if self.board[win[0]] == 'X' or self.board[win[0]] == 'O':
                if self.board[win[0]] == self.board[win[1]] and self.board[win[1]] == self.board[win[2]]:
                    return self.board[win[0]]

    def score(self, depth):
        if Agent.check_winner(self) == self.player:
            return 10 - depth
        else:
            return depth - 10

    def game_over(self):
        if self.board.count(None) == 0:
            return True
        elif Agent.check_winner(self) == 'X' or Agent.check_winner(self) == 'O':
            return True
        else:
            return False

    def possible_moves(self):
        return [i for i in range(len(self.board)) if self.board[i] is None]

    def make_move(self, position, player):
        self.board[position] = player

    def switch_player(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def minimax(self, depth, player, best):
        if Agent.game_over(self) is True:
            return Agent.score(self, depth)
            best = -1000
        depth += 1
        moves = Agent.possible_moves(self)
        print(moves)
        for m in moves:
            Agent.make_move(self, m, player)
            val = Agent.minimax(
                self, depth, Agent.switch_player(self, player), best)
            print(player, val, best)
            Agent.make_move(self, m, None)
            if player == self.player:
                if val > best:
                    best = val
                    self.choice = m
            else:
                if val > best:
                    best = val
                    self.choice = m
        return best
