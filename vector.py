"""
    a class for the storage and manipulation of vectors
        in a fixed dimension n
"""

import math

class Vector:

    dimension=None
    x=None

    def __init__(self, y=[]):
        self.x=y
        self.dimension=len(y)

    def __str__(self):
        st="[ "
        if(len(self.x) > 0):
            for y in self.x[:-1]:
                st+=str(y)+", "
                st+=str(self.x[-1])
        st+=" ]"
        return st

#
# x= [1,2,3,4,5,6,7,8,9]
# y= x[:-1]

    def add(self,y):
        if (len(y)==self.dimension):
            for i in range(0, self.dimension):
                self.x[i]+=y[i]

    def norm(self):
        nx2=0.0
        for z in self.x:
            nx2+=z*z
        nx=math.sqrt(nx2)
        return nx

    def scalar(self,y):
        scal=0.0
        if (len(y)==self.dimension):
            for i in range(0, self.dimension):
                scal+=self.x[i]*y[i]
        return scal

    # otherwise implement some version with the Levi-Civita tensor
    #
    # X cross Y = e(ijk) *Xi*Yj
    #
    def vectorial3D(self,y):
        if ( len(self.x)==3  and  len(y)==3 ):
            vect=[0.0, 0.0, 0.0]
            for i in range(0, 1):
                j=(i%3)
                vect[3-i]=self.x[i]*y[j]-self.x[j]*y[i]

#                vect[3-i]=self.x[i]*y[i+1]-self.x[i+1]*y[i]
#
#                vect[3]=self.x[1]*y[2]-self.x[2]*y[1]
#                vect[1]=self.x[2]*y[3]-self.x[3]*y[2]
#                vect[2]=self.x[3]*y[1]-self.x[1]*y[3]
#
            return vect
        else:
            print 'Dimension Error, vector'

        
    def times_scalar(self, ll):
        for z in self.x:
            z=z*ll
    
    # convert a string to a vector object
    def fromString(self,text):
        data=text.strip("[ ]")
        self.x=map(int,data.split(','))
        self.dimension=len(self.x)
#        x_new=[]

"""
 test:
     from vector import Vector
     x=Vector()
     x
     x.x
     a='[1, 2, 3, 4, 5, 6, 7, 8]'
     x.fromString(a)

     y=Vector([0.0,1.0,2.0])    

     b='[3,8,6]'
     z=Vector().fromString(b)
     
     print 'test vector product'
     t=y.vectorial3D(z)
     s=y.vectorial3D(x)

"""
     

# alternative ideas ...        
#        float(x) if '.' in x else int(x)
#        map(int, list)        
        
    # vector product in 3D ...

# EOF
