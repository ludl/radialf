"""
  an implementation of a go board:
    with attributes:
      - title
      - size
      - moves
      - game_commentary
"""

class BoardGame:
    
    # the title of the game
    title

    # Comments
    game_commentary

    # the size is a couple [n,m] usually equal
    size

    # the list of moves
    moves


    def __init__(self,n,m,t="a new game",c=""):
        self.title=t
        self.size=[n,m]
        self.moves=[]
        self.game_commentary=c

    def __str__(self):
        sts="Title: "+self.title
        sts+="Commentary:\n"
        sts+=self.game_commentary
        sts+="\n"
        sts+="The boardsize is "+str(size)+"\n"
        sts+="\n"
        sts+="Moves\n"
        for m in moves:
            sts+=str(m)+"\n"
        return sts

    def writeGameFile(self, file_name):
        output=open(file_name)
        output.write(str(self))
        output.close()

    def add_move(stone):
        moves.append(stone)

#    def read_move():

#    def get_position():
#        return position

# EOF
