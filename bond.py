"""
  the class bond is a model for a molecular bond
"""
class Bond:

  atom_1

  atom_2

  "distance seperating the atoms (centers)" 
  bond_length

  " order of the bond, an integer, usually (0),1,2,3,4 ..."
  order

    " The string for a bond is [ela,elb,dist, order]"
    def bond_toString(bond)
        bond_name="[ "+bond.getpair().toString()+bond.dist+bond.order+" ]"
        return bond_name
