"""
  an implementation of a go stone:
    with attributes:
      - move number
      - color
      - position [x,y,z]
"""

class Stone:

    move_number=None
    
# color is usually 'Black' or 'White'
    color=None
    
    # the position is a vector (in 2D or 3D)
    position=None
    
    "construct a new stone with: n: move number, c: color (Black or White), p: position vector."

    def __init__(self,n,c,p):
        self.move_number=n
        self.color=c
        self.position=p

# more elaborate, but nasty format
#    def __str__(self):
#        st="move "+str(self.move_number)+" by "+self.color+" at "+str(self.position)
#        return st

    def __str__(self):
        st=str(self.move_number)+" "+self.color+" "+str(self.position)
        return st

    def get_move(self):
        return self.move_number

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_distance(self,x):
        return self.position.distance(x.position)


# EOF
