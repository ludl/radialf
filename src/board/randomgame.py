"""
  RandomGame is an implementation of a random generator of a game of go:
    with attributes:
      - title
      - size
      - moves
      - game_commentary
"""

import math, boardgame
import random
# random stuff

class RandomGame:

    # the title of the game
    random_board

    # Comments
    game_commentary

    # the size is a couple [n,m] usually equal
    size

    # the list of moves
    moves


    def __init__(self,n,m,t="",c=""):
        title="Random game "+t
        random_board=boardgame.BoardGame(n,m,title,c)
        random_board.moves=[]

    def generate_random_moves(self,board):
        
        n=size[0]        
        m=size[1]
        
        number_of_moves=ran()*n*m
        
        ran_x=random.random()
        
        ran_nb=random.randint(a,b)        
        
    def generate_sequence(self, length):
        
        # blabla
