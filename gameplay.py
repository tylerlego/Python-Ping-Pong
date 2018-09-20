import sys
import time
import math

class PlayerScore:
    def __init__(self):
        self.points = 0
        self.games = 0

class MatchScore:
    def __init__(self):
        self.player1_points = 0
        self.player1_games = 0
        self.player2_points = 0
        self.player2_games = 0

class Match:
    def __init__(self, id, player1, player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.score = MatchScore()

    def point(self, point_winner):
        print('Point scored by %s!' % (point_winner.first_name))
        point_winner.score.points += 1
        if point_winner.id == self.player1.id:
            self.score.player1_points += 1
        else:
            self.score.player2_points += 1
        if (self.score.player1_points >= 11) or (self.score.player2_points >= 11):
            if abs(self.score.player1_points - self.score.player2_points) >= 2:
                self.game(point_winner)

    def game(self, point_winner):
        print('Game won by %s!!\n' % (point_winner.first_name))
        point_winner.score.games += 1
        result = self.score.player1_points > self.score.player2_points
        if (result == True):
            self.score.player1_games += 1
        else:
            self.score.player2_games += 1
        self.score.player1_points = 0
        self.score.player2_points = 0
        if point_winner.score.games >= 2:
            # put in 5th game logic
            self.end_match(point_winner)

    def end_match(self, point_winner):
        print('MATCH OVER!')

class Player:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.score = PlayerScore()
