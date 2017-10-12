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
        _, choice = Agent.minimax(self, 1, self.player)
        if Agent.game_over(self) is True:
            print('Game Over!')
            return self.board
        self.board[choice] = self.player
        print(self.board)
        return self.board

    def check_winner(self):
        winstate = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8],
                    [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
        for win in winstate:
            if self.board[win[0]] == 'X' or self.board[win[0]] == 'O':
                if self.board[win[0]] == self.board[win[1]] \
                        and self.board[win[1]] == self.board[win[2]]:
                    return self.board[win[0]]

    def score(self, depth):
        if Agent.check_winner(self) == self.player:
            return 10 - depth
        elif Agent.check_winner(self) == self.opponent:
            return depth - 10
        else:
            return 0

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

    def minimax(self, depth, currplayer):
        if Agent.game_over(self) is True:
            return Agent.score(self, depth), None
        if currplayer == self.player:
            bestval = -10
            bestmove = -1
        else:
            bestval = 10
            bestmove = -1
        possiblemoves = Agent.possible_moves(self)
        for m in possiblemoves:
            Agent.make_move(self, m, currplayer)
            val, _ = Agent.minimax(
                self, depth + 1, Agent.switch_player(self, currplayer))
            Agent.make_move(self, m, None)
            if currplayer == self.player:
                if val > bestval:
                    bestval = val
                    bestmove = m
            else:
                if val < bestval:
                    bestval = val
                    bestmove = m
        return bestval, bestmove
