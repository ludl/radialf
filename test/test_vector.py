# -*- coding: utf-8 -*-
"""
    Test of vector class


Created on Wed Mar 27 19:45:14 2013

@author: ludl
"""

# Test of vector
from vector import Vector
import pdb

print 'test vector constructor'
x=Vector()
print 'x ', x
print 'x.x is ', x.x

print 'test vector from String'
a='[1, 2, 3, 4, 5, 6, 7, 8]'
x.fromString(a)
print 'a =',a
print 'x =',x

b='[3,8,6]'
z=Vector().fromString(b)

print 'b, z are :'
print b, z

c='[3, 8, 6]'
z1=Vector()

print 'z1 is :'
print z1

z1.fromString(c)

print 'c, z1 are :'
print c, z1

print 'test vector from array'
y=Vector([0.0,1.0,2.0])    
print 'y is ',y
 
#print 'test vector product'
#t=y.vectorial3D(z)
#s=y.vectorial3D(x)

print 'a new test'

xy0=Vector().fromString2(c)
xy1=Vector()

xy1.fromString2(c)
print 'xy0 is ', xy0

print 'xy1 is ', xy1

print 'xy1.x is ', xy1.x


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
