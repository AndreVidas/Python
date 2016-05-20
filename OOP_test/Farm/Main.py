# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:52:06 2016

@author: andre
"""

import classes.Fox as f
import classes.Rabbit as r
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import animation

# use this link to learn about how to animate the positions..
# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

# This site also seems to be good for animation
# http://www.labri.fr/perso/nrougier/teaching/matplotlib/#simple-plot


if __name__ == '__main__':
    
    # Initialize all animals into lists. range(x) defines numbers of animals for each list.
    foxList = [f.Fox(np.random.randint(1,10),np.random.randint(1,10)) for i in range(10)]
    rabbitList = [r.Rabbit(np.random.randint(1,10),np.random.randint(1,10)) for i in range(10)]
    print len(foxList)
    print len(rabbitList)
    
    
    for i in range(2):
        
        
        for fox in foxList:
            # Change position of all foxes (fox walk).
            fox.setCoord(np.random.randint(0,3)-1,np.random.randint(0,3)-1)
            
            #print fox.getLife()
            
            # Kill fox if its starving to death
            if fox.getLife() == 0:
                del foxList[foxList.index(fox)]
            
            # Kill rabbit if fox has neighboring position with rabbit r (fox eats the rabbit).
            for rabbit in rabbitList:            
                if fox.getCoord() == rabbit.getCoord():
                    del rabbitList[rabbitList.index(rabbit)]
                    fox.setLife(100) # add more life points to fox (resources from eating rabbit)
                    print fox.getLife()
            
        
        for rabbit in rabbitList:
            #print rabbit.getCoord()
            # Change position of all rabbits (rabbit walk).
            rabbit.setCoord(np.random.randint(0,3)-1,np.random.randint(0,3)-1)
            #print rabbit.getCoord()
            
            
        # print out amount of rabbits and foxes:
        print len(foxList), "foxes after round:", i+1
        print len(rabbitList), "rabbits after round:", i+1

 