"""
  the class Bond is a model for a molecular bond.
    its attributes are:
        atoms: a list of 2 atoms
        order: the order of the bond, an integar (0),1,2,3,4, ...
        bond_length: 
"""
class Bond:

    " a list of the two atoms connected by the bond"
    atoms=None

    " distance seperating the two atoms (centers)" 
    bond_length=None

    " order of the bond, an integer, usually (0),1,2,3,4 ..."
    order=None

    " The string for a bond is [ela,elb,dist, order]"
    def bond_toString(self)
        bond_name="[ "+str(self.atoms())+" "+str(self.dist)+" "+str(self.order)+" ]"
        return bond_name

    " define the behaviour of str() when called on a bond. it is : [ela,elb,dist, order]"
    def __str__(self)
        bond_name="[ "+str(self.atoms)+" "+str(self.dist)+" "+str(self.order)+" ]"
        return bond_name

    "dir() tells you the attributes of a class object"

    def __init__(self):
        
    
    "make a bon from a list of 2 atoms, order of the bond and its length."
    def make_bond(self, atoms, n_order, x_length)
        __set_atoms(atoms)
        set_order(n_order)
        set_bondlength(x_length)

    "set atoms which the bond connects."
    def __set_atoms(self,atoms):
        self.atoms=atoms

    def set_bondlength(self,dist):
        self.bond_length=dist

    def set_order(self,n_order):
        self.order=n_order
        
    "below are get functions"
    def get_bondlength(self):
        return self.bond_length
        
    def get_order(self):
        return self.order

    def get_atoms(self):
        return self.atoms
    
    def get_atom_1(self):
        return self.atom[0]
    
    def get_atom_2(self):
        return self.atom[1]
        
        
#Everything looks good here; we're unable to call it. It is, in fact, 'private'. Well, actually it isn't. Running dir() on the object reveals a new magical method that python creates magically for all of your 'private' methods.
#
# dir(obj)
#  gives: ['_MyClass__myPrivateMethod', '__doc__', '__module__', 'myPublicMethod']

#
# http://docs.python.org/2/reference/datamodel.html
#
# http://www.rafekettler.com/magicmethods.html
#

# http://www.faqs.org/docs/diveintopython/fileinfo_private.html
#
# Footnotes
#
#[5] Strictly speaking, private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private; internally, the names of private methods and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given names. You can access the __parse method of the MP3FileInfo class by the name _MP3FileInfo__parse. Acknowledge that this is interesting, then promise to never, ever do it in real code. Private methods are private for a reason, but like many other things in Python, their privateness is ultimately a matter of convention, not force.

