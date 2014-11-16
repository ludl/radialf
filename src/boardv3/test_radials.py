# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:14:06 2013

@author: ludl
"""

# Test of vector
from boardgame import BoardGame
import radials

import pdb
import random

#@Test0
#	load a file and rewrite
#
def test0():
    
    print 'test 0'
    infile='example/game_test0.txt'
    myform='movelist'    
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame()
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
    
    print 'test 0 ended'
    
#    x=assert()

# @Test1
#	load a file, test printing and rewrite
#
def test1():

    print 'test 1'
    
    infile='example/game_test01.txt'
    myform='movelist'
    
    outfile='test1_outboard.txt'
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame()
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
    
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)
    
    print 'test 1 ended'
    
#    x=assert()

#@Test2
#
#
def test2():

    print 'test 2'
    
    infile='example/game_test2.txt'
    myform='myf'
    
    outfile='test2_outboard.txt'
    
    n=19    
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
    
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)
    
    print 'test 2 ended'
#    x=assert()

#@Test3
#
#
def test3():

    print 'test 3'
    
    infile='example/17lg1-1.sgf'
    myform='sgf'
    
    outfile='test3_outboard.txt'
    
    n=19
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
    
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)
        
    print 'test 3 ended'
#    x=assert()

#@Test4
#
#
def test4():

    print 'test 4'
    
    infile='example/test3_outboard.txt'
    myform='myf'
    
    outfile='test4_outboard.txt'
    
    n=19
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
        
    print 'write board to file in myformat'
    myboard.writeSGF(outfile)    
    
    print 'test 4 ended'
#    x=assert()

#@Test4
#
#
def test5():

    print 'test 5'
    
    infile='example/test4_outboard.txt'
    myform='sgf'
    
    outfile='test5_outboard.txt'
    
    n=19
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
        
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)    
    
    print 'test 5 ended'
#    x=assert()

#@Test6
#
#
def test6():

    print 'test 6'
    
    infile='example/yamadori-kentaur.sgf'
    myform='sgf'
    
    outfile='test6_outboard.txt'
    
    n=19
    
    print 'load file : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.load_File(myform, infile)
    
    print 'print board'
    print str(myboard)
        
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)    
    
    print 'test 6 ended'
#    x=assert()

#
#	test random moves
#
def test7():

    print 'test 7'
    
#    nmoves=20
    nmoves=random.randint(0,361)
    print nmoves
#    for i in range(nmoves):
#        x=random.random()
#        print x
    
    infile=''
    out_graph='graph_test7'
#    myform='sgf'
    
    outfile='test7_outboard_random3.txt'
    
    n=19
    
    print 'make random board : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.make_random(nmoves)
    
    print 'print board'
    print str(myboard)
    
    myboard.graph(out_graph)
        
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)    
    
    print 'test 7 ended'


#
#	test random moves
#
def test8():

    print 'test 8'
    
#    nmoves=20
    nmoves=random.randint(0,361)
    print nmoves
#    for i in range(nmoves):
#        x=random.random()
#        print x
    
    vers=8
    vs=str(vers)
    
    infile=''
    out_graph='graph_test'+vs
    plot_name='graph_g_distribution_30'+vs
#    myform='sgf'
    
    outfile='test'+vs+'_outboard_random3.txt'
    
    n=19
    
    print 'make random board : '+infile
#    myboard=BoardGame(infile,myform)
    myboard=BoardGame(n,n)
    myboard.make_random(nmoves)
    
    print 'print board'
    print str(myboard)
    
    myboard.graph(out_graph)
        
    print 'write board to file in myformat'
    myboard.writeGameFile(outfile)    
    
    #
    #
    #
    print 'calculating g(r) functions'
    
    # one general, BB, WW, BW
    rg=radials.make_gofr(plot_name,myboard)
    #radials.make_gofr(plot_name,myboard)
    #radials.plot(plot_name,rg)
    
    print 'test 8 ended'


#
#   run tests
#

#test0()
#test1()
#test2()
#test3()
#test4()

#test5()
#test6()

#test7()
test8()

