"""
    the class Pair defines a pair.
    can be used with Atom (for use with Bond)
            or with Stone (for Go analysis).
"""

class Pair:

    first=None

    second=None

"""
    initialization of the object.
    a, and b may be any general class, usually the same.
    this class can be used with Atom or Stone
"""
    def __init__(self, a, b):
        first=a
        second=b
    # end of init(ata, atb)

    def getpair(self):
        return [first, second]

    def get_atom(self, i):
        at=0
        if (i==1): at = first
        elif(i==2): at = second
        else: print "error, specified i= "+str(i)+" out of range."
        return at

    def get_first(self)
        return first

    def get_second(self)
        return second

    def __str__(self):
        sp="[ "+str(first)+", "+str(second)+" ]"
        return sp
    #end of str()
    
# EOF
