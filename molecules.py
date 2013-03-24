"""
the class Molecules provides a basic represenation of a collection of atoms with:
    - number
    - kind
    - positions
    - bonds
    - some functions to manipulate them (subsets etc)
"""
class molecule:
    
    elements=[[]]
    bonds=[]

    def __init__(self):
        initialize this object


    """ the function make element will generate the ...
    """
    def add_element(self.atom):
        elements=[elements[:], atom]
    # TODO check if we can get the ordinal of atom

    def add_bond(bond):
        if bond.contains(bond)):
            bonds=[ bonds[:], bond ]
        else:
            print "the bond "+bond_toString(bond)+" is already in the list of existing bonds."

    def get_elements(self):
        return fullcopy(self.elements)

    " The string for a bond is [ela,elb,dist, order]"
    def bond_toString(bond)
        bond_name="[ "+bond.getpair().toString()+bond.dist+bond.order+" ]"
        return bond_name

    def pair_toString(pair):
        stp="( "+str(pair)+" )"

    # a list of atoms
