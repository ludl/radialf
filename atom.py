"""
  a class to handle atoms (kind, number, position ...)
"""

class Atom:

    kind

    position

    velocity    

    nb

    def __init__(self, k, x, v=None):
        self.kind=k
        self.position=x
        self.velocity=v

    def set_nb(ni):
        self.nb=ni

    def get_nb():
        return self.nb

    def get_kind():
        return kind

    def get_position():
        return position
        
    def get_velocity():
        return velocity
        
# note on slicing
#         a[i:j:k] selects all items of a with index x where x = i + n*k, n >= 0 and i <= x < j.
#
# EOF
