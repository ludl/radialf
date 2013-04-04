# -*- coding: utf-8 -*-
"""
  an implementation of a go board:
  with attributes:
      - title
      - size
      - moves
      - game_commentary

Created on Wed Mar 27 19:22:07 2013

@author: ludl

"""

import stone
from vector import Vector

"""
    an implementation of a Board for a game of go
    with attributes:
        - a title
        - comments
        - size of the board        
        - a list of moves
"""
class BoardGame:

    # the title of the game
    title=""

    # Comments
    game_commentary=""

    # the size is a couple [n,m] usually equal
    size=[]

    # the list of moves
    moves=[]


    def __init__(self,n=1,m=1,t="a new game",c=""):
        self.title=t
        self.size=[n,m]
        self.moves=[]
        self.game_commentary=c


    def __str__(self):
        sts="Title: \n"
        sts+=self.title+"\n"
        sts+="Commentary:\n"
        sts+=self.game_commentary+"\n"
        sts+="The boardsize is\n"
        sts+=str(self.size).strip('[ ]')+"\n"
        sts+="Moves\n"
        for m in self.moves:
            sts+=str(m)+"\n"
        return sts


    def writeGameFile(self, file_name):
        output=open(file_name, 'w')
        output.write(str(self))
        output.close()

    def writeSGF(self, file_name):
        output=open(file_name, 'w')
        output.write(self.make_sgf_format())
        output.close()

    def add_move(self, stone):
        self.moves.append(stone)

    def setsize(self,text):
        s=[int(x) for x in text.split(',')]
        self.size=s

    def load_File(self, gofileformat, filename):
#        filetext=file(filename, 'r')
#        go_lines=split(filetext)
        if(gofileformat is "sgf"):
            self.load_sgf(filename)
        elif(gofileformat is "myf"):
            self.load_myformat(filename)
        elif(gofileformat is "movelist"):
            self.load_movelist_format(filename)
        else:
            print 'error : query unsupported format : '+gofileformat
        # TODO finish this !
    
    def make_sgf_format(self):
        sgf='(;\n'
        sgf+='EV['+self.title[:-1]+']\n'

        abc='abcdefghijklmnopqrs'
        nums=self.make_numalpha(abc)

        for m in self.moves:
            color=m.get_color()
            p=m.get_position()
            
            mx=nums.get(p.x[0])
            my=nums.get(p.x[1])

            stm=';'+color[0]+'['+mx+my+']\n'
            sgf+=stm
            print m
        sgf+=')'
#        print sgf
        return sgf
        
#Assuming that the values in the dict are unique:
#dict((v,k) for k, v in map.iteritems())
    
    def load_sgf(self, filename):
        filetext=file(filename, 'r')
        go_lines=filetext.readlines()
#        alpha={'a' : 1, 'b' : 2 }
        abc='abcdefghijklmnopqrs'
        alpha=self.make_alphabet(abc)
        
        nb=0
        #,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}
#        alphabet={a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}
#        go_lines=str.splitlines(filetext)
        for line in go_lines:
#            print 'Error: not implemented yet'            
            #bla
            if( line[0] is ';' ):
#                skip lines (eventually implement reading of size, komi, players and result)
#                for line in remaining_lines:
                for x in line[1:].split(';'):
                        # format is B[pd] with spaces for pass
                        print x
                        nb=nb+1
                        color=x[0]
                        if(x[2] is ' '):
                            position=[0,0]
                        else:
                            position=[ alpha.get(x[2]), alpha.get(x[3]) ]
                        next_move=stone.Stone(nb,color,position)
                        self.moves.append(next_move)
    # end of load_sgf (v1)

#
# construct alphabet
#
#        ab='abscdefghijklmnopqrs'
    def make_alphabet(self, ab):
        alpha=dict.fromkeys(ab)
        i=0
        for x in ab:
            i=i+1
            alpha[x]=i+1
        return alpha
#

    def make_numalpha(self, ab):
        alpha=self.make_alphabet(ab)
        numa=dict((v,k) for k, v in alpha.iteritems())
        return numa
#

    def load_myformat(self, filename):
        filetext=file(filename, 'r')
        go_lines=filetext.readlines()
        
        header=go_lines[0:6]

        self.title=header[1]
        self.game_commentary=header[3]
        self.setsize(header[5])
        
        movelines=go_lines[7:]
#        go_lines=str.splitlines(filetext)
#        go_lines=filetext.splitlines()
        #
        # TODO add the part to read the header and board size
        #
        for line in movelines:
            content=line.split(None,2)
            
            number=content[0]
            color=content[1]
            pos=Vector()
#            pos.fromString3(content[2].strip(" "))
            pos.fromString(content[2].strip(" "))
            next_move=stone.Stone(number,color,pos)
            self.moves.append(next_move)
        #TODO write this
        
    " this version is for testing mostly, only reads a list of moves, no headers"        
    def load_movelist_format(self, filename):
        filetext=file(filename, 'r')
        go_lines=filetext.readlines()
        for line in go_lines:
            content=line.split(None,2)
            
            number=content[0]
            color=content[1]
            pos=Vector()
#            print content[2]
            pos.fromString3(content[2].strip(" "))
#            pos.fromString(content[2].strip(" "))
            
            next_move=stone.Stone(number,color,pos)
            self.moves.append(next_move)        
        
#
# OLD version
#
#    def load_myformat(self, filename):
#        filetext=file(filename, 'r')
#        go_lines=filetext.readlines()
##        go_lines=str.splitlines(filetext)
##        go_lines=filetext.splitlines()
#        #
#        # TODO add the part to read the header and board size
#        #
#        for line in go_lines:
#            content=line.split(None,6)
#            
#            number=content[2]
#            color=content[4]
#            pos=Vector.fromString(content[6].strip(" "))
#            
#            next_move=stone.Stone(number,color,pos)
#            self.moves.append(next_move)
#        #TODO write this
        
        

#    def read_move():

#    def get_position():
#        return position

# EOF
