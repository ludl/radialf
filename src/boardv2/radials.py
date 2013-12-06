#
# some radial distribution calculations
# for statistics on a 2d board
# to be extended to N dimensions.
#


def histogram(game, dr=0.1):

  R=game.get_Rmax()
  N=int(R/dr)

  r=0
  g=[]
  
  for i in range (N):
    
    upper=r+dr
    g+=[0]
    
    for m in game:
      for n in game:
        dist=m.distance(n)
        if (r<dist=<upper):
          g[i]+=1
    r=upper
  return g

def test_g():
  
  test if integral of g is equal to the number of moves? (squared?)


def conversions:

  between the following formats

  gs=[ig, (i+1g), ...]
  or  same with rg
  
  ig=[i,gi]
  rg=[r,gr]
  
  g[i]=[...,g(i),g(i+1),...]
  g[r]=[...,g(r),g(r+1),...]

  ordinals=[0,1, ...i,i+1...]
  r=[0,dr,2dr, ... Rmax]


def plot():

# TODO make this plotting routine
