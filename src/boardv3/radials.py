#
# some radial distribution calculations
# for statistics on a 2d board
# to be extended to N dimensions.
#

import boardgame
#from boardgame import BoardGame


def make_gofr(graph_name,boardg):
    
    game=boardg.moves
    print 'game'
    print game
    
    gsize=boardg.size
    
    dr=0.10
    
    #z=my_radial(game, dr=2.0)
    z=my_radial(game,gsize, dr)
    plot(graph_name+'_all',z)
        
    black_game=game[0::2]
    v=my_radial(black_game,gsize, dr)
    plot(graph_name+'_black',z)

    white_game=game[1::2]
    w=my_radial(white_game,gsize, dr)
    plot(graph_name+'_white',z)
    
    return z
    

def my_radial(game, game_size, dr=0.1):

  #R=pow(game.size[0],0.5)
  #R=game.size[0]*pow(2.0,0.5)
  rm=float(game_size[0])
  rn=float(game_size[1])
  R=pow(rm**2+rn**2,0.5)
  N=int(R/dr)+1
  
  print 'R = ',R
  print 'N = ',N
  print 'dr = ',dr
  print 'nb of moves = ', len(game)

  #r=0
  #g=[]
  g=[0 for j in range(N) ]
  r=[k*dr for k in range(N) ]
  
  #ds=[]
  for m in game:
      for n in game:
          #ds+=[m.get_distance(n)]
          ds=m.get_distance(n)
          i=int(ds/dr)
          print 'i = ',i
          print 'd = ',ds
          g[i]+=1
  # sort ds

  #for i in range (N):

    #upper=r+dr
    #g+=[0]

    #for d in ds:
    #    i=int(d/dr)
    #    print 'i = ',i
    #    print 'd = ',d
    #    g[i]+=1
        #
        #   should perhaps exclude d==0
        #
        #if (r<d and d<=upper):
        #    g[i]+=1
    #r=upper
  return [r,g]

#
#   todo: make a normalisation
#

def histogram(game, dr=0.1):

  R=game.get_Rmax()
  N=int(R/dr)

  r=0
  g=[0 for j in range(N) ]

  for i in range (N):

    upper=r+dr
    g+=[0]

    for m in game:
      for n in game:
        dist=m.distance(n)
        i=dist/dr
        g[i]+=1
        #if (r<dist<=upper):
        #  g[i]+=1
    r=upper
  return g

def test_g():

    bla=1
#  test if integral of g is equal to the number of moves? (squared?)

#
#def conversions():
#
#  between the following formats
#
#  gs=[ig, (i+1g), ...]
#  or  same with rg
#
#  ig=[i,gi]
#  rg=[r,gr]
#
#  g[i]=[...,g(i),g(i+1),...]
#  g[r]=[...,g(r),g(r+1),...]
#
#  ordinals=[0,1, ...i,i+1...]
#  r=[0,dr,2dr, ... Rmax]
#

def plot(outfile,rg):
        #a=1
        # use matplot lib here        
        import numpy as np
        import math
        import matplotlib.pyplot as plt
        #import matplotlib.cm as cm
        
        my_fig = plt.figure()
        #my_plt_one = my_fig.add_subplot(1, 1, 1, aspect='equal')
        my_plt_one = my_fig.add_subplot(1, 1, 1)

        my_plt_one.set_title('distribution')
        my_plt_one.set_xlabel('r')
        my_plt_one.set_ylabel('g(r)')
        
        #my_plt_one.set_ylim([0,20])
        #my_plt_one.set_autoscaley_on(False)
        #my_plt_one.set_xlim([0,20])
        #my_plt_one.set_autoscalex_on(False)
        
        ax=my_fig.gca()
        #ax.set_xticks(np.arange(1,20,1))
        #ax.set_yticks(np.arange(1,20,1))
        
        ax.xaxis.grid('-')
#        ax.xaxis.grid(color='0.5', linestyle='-')
#        ax.yaxis.grid(color='0.5', linestyle='-')
#        ax.yaxis.grid(color='gray', linestyle='dashed')
        plt.grid( color='gray', linestyle='-')
        [line.set_zorder(3) for line in ax.lines]


        my_plt_one.plot(rg[0], rg[1], linestyle='-', markersize=1.0, label='g1',color='Black', zorder=300)
        #my_plt_one.plot(rg[0], rg[1], marker='-', markersize=1.0, label='g1',color='Black', zorder=300)
        #my_plt_one.plot(r, g, marker='-', markersize=13,label=str(m.get_move()),color=m.get_color(), zorder=300)
        
        #for m in self.moves:
        #     print m.get_color()
        #    [mx, my]=m.get_position().get_x()
        #    my_plt_one.plot(mx, my, marker='o', markersize=13,label=str(m.get_move()),color=m.get_color(), zorder=300)

        plt.savefig(outfile+'.png',bbox_inches=0)
        plt.savefig(outfile+'.pdf',bbox_inches=0)
        plt.show()


# TODO make this plotting routine
