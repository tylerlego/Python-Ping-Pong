import sys
import time
import math
from pp_scoring import Player, Match, PlayerScore, MatchScore
from pp_movement import *

# Define the players
pTL = Player(1, 'Tyler', 'Lego')
pJA = Player(2, 'Jenni', 'Austin')

# Define the match
match1 = Match(1, pTL, pJA)

# Gameplay
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pJA)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pJA)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pJA)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pJA)
match1.point(pTL)
match1.point(pTL)
match1.point(pTL)
match1.point(pJA)
match1.point(pTL)
match1.point(pTL)

# Print match info
print('\nMatch 1 participants: %s, %s' % (match1.player1.first_name,match1.player2.first_name))
print('Match 1 Score: \nGames: %s - %s \nPoints: %s - %s' % (match1.score.player1_games, match1.score.player2_games, match1.score.player1_points, match1.score.player2_points))
