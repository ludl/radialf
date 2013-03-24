#
# test of python ide for ...
#
#  calculate some g(r) etc
#
#
# this documentation is to be licensed under gnu fdl
# the code will be licensed under gnu GPL


molecules

positions=[ H, x, y, z]
gr=[[],[]]


def read_positions():
   

# end of read_positions



""" calculate g(i,j,r,dr) for elements from positions
    pairs(i,j) are ordered
    with the formula:
        g(i,j,r)= number of pairs(i,j) whose distance is in [r+-dr] / total number of pairs (i,j)

       
        i: first particle species
        j: second particle species
        r: distance between the species pair
        dr: bin width
...
"""
def calc_gr(i,j,r,dr):
   
    nijr=calc_pairs(i,j,r,dr)
    ntot=positions.getntot(i,j)
   
    gijr=float(nijr)/float(ntot)
   
   
# end of calc_gr

""" calculate number of pairs n(i,j,r,dr) for elements (i,j) from positions, it is an integer
    pairs(i,j) are ordered
        n(i,j,r,dr)=number of pairs(i,j) whose distance is in [r+-dr]
       
        i: first particle species
        j: second particle species
        r: distance between the species pair
        dr: bin width
...
"""
def calc_pairs(i,j,r,dr):
   
    nijr = 0
    ntot = 0
    for a in i.getset():
        for b in j.getset():
            d  = (b.pos().diff(a.pos())).norm()
            if (abs(d-r)<dr):
                nijr+=1
            ntot+=1
    return nijr
# end of calc_pairs

"""
 is_pair_distance_r(ela,elb,r,dr):
    returns 1 if the distance between the pairs is r with tolerance dr
             0 otherwise.
"""
def is_pair_distance_r(ela,elb,r,dr):

    n=False
    d  = (ela.pos().diff(elb.pos())).norm()
#
# add some or loops here
#
#  to account for periodic boundary
#    eg: if d1= a.image(+-x, +-y , +-z).pos - b.image(+-x, +-y , +-z).pos
#
#    eg: if d2= a.pos().diff(b.pos()).modulo(box).norm
#    ....
#
#   check if double counting is avoided !
#
#
    if (abs(d-r)<dr):
        n=True
    return n
# end of calc_pairs


def calc_pairs_v2(i,j,r,dr):
   
    nijr = 0
    ntot = 0
    for a in i.getset():
        for b in j.getset():
            ab_dist_is_r=is_pair_distance_r(ela,elb,r,dr)
            if (ab_dist_is_r):
                nijr+=1
            ntot+=1
    self.set_ntot(ntot)
    self.set_nijr(i,j,r,nijr)
# end of calc_pairs_v2


def calc_pairs_allr(i,j,r,dr):
   
    for r in radial_range(r,dr):
       
       
        set_gijr(i,j,r,dr,gijr)
# end of calc_pairs_allr


def molecule:



class particles:
