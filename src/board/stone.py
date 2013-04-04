"""
  an implementation of a go stone:
    with attributes:
      - move number
      - color
      - position [x,y,z]
"""

class Stone:

    move_number
    
# color is usually 'Black' or 'White'
    color
    position

    def __init__(self,n,c,p):
        self.move_number=n
        self.color=c
        self.position=p

    def __str__(self):
        st="move "+str(move_number)+" by "+color+" at"+str(position)+""+str(color)+
        return st

    def get_move():
        return move_number

    def get_color():
        return color

    def get_position():
        return position

# EOF
