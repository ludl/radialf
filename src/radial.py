"""
a class to do radial function calculations

"""

class RadialFunction:

  kind1=None
	kind2=None

	dr=None
	rmin=None
	rmax=None
	
#    table of pairs
	pairs=None
	g=None
	#    distances (indexed by pairs)


#    def calc_distances(self):
#        
#        for x in pairs:
#            for y in pairs[minus x and preceeding]:
#                d=x.distance(y)

	def __init__(self, kinda, kindb, dr, rmin=0.0, rmax):
		self.kind1=kinda
		self.kind2=kindb
		self.dr=dr
		self.rmin=rmin
		self.rmax=rmax
	# end of init
	
	
	def get_pairs(self):
		return self.pairs
	# end of get_pairs
	
	def calculate_distances(self):
		for p in pairs:
			p.distance=p.x.get_distance(p.y)
	# end of calculate_distances
	
	#
	# this function generates a list of all pairs, not sorted
	#	slice this to get lists of pairs with first black, white etc ...
	#
	def generate_pairs(self, board):
		
		my_pairs=[]
		
		othermoves=board.moves
		
		for stone1 in board.moves:
			othermoves=othermoves[1:]
			for stone2 in board.moves - stone1 and preceding:
				myp=Pair(stone1,stone2)
				my_pairs+=[myp]
	# end of generate_pairs
	
	def calculate_g_of_r(self):
		if (len(self.pairs)>0):
			
			myg=[0.0]
			
			for p in self.pairs:
				
				for xr in range(rmin, rmax, dr):
					if ( self.rmin+i*self.dr < p.distance < )
						myg[i]=p.distance
	
#
# add some ideas for r_max=boxsize/2
#
