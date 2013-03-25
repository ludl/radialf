"""
    the class Pair defines a pair of atoms (for use with Bond)
"""

class Pair:

    first=None

    second=None

    def __init__(self, ata, atb):
        first=ata
        second=atb
    # end of init(ata, atb)

    def getpair(self):
        return [first,second]

    def __str__(self):
        sp="[ "+str(first)+", "+str(second)+" ]"
        return sp
    #end of str()
    
# EOF
