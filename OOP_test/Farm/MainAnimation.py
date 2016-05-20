# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:52:06 2016

@author: andre
"""

import classes.Fox as f
import classes.Rabbit as r
import classes.Salad as s

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import animation

# use this link to learn about how to animate the positions..
# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

# This site also seems to be good for animation
# http://www.labri.fr/perso/nrougier/teaching/matplotlib/#simple-plot


if __name__ == '__main__':
    
    
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
    foxPlot, = ax.plot([], [], 'o',c='red')
    rabbitPlot, = ax.plot([], [], 'o', c='blue')
    saladPlot, = ax.plot([], [], 'o', c='green')
    
    
    
    # initialization function: plot the background of each frame
    def init():
        foxPlot.set_data([], [])
        rabbitPlot.set_data([], [])
        saladPlot.set_data([],[])
        return foxPlot, rabbitPlot, saladPlot,
    
    # Initialize all animals into lists. range(x) defines numbers of animals for each list.
    foxList = [f.Fox(np.random.randint(1,10)-5,np.random.randint(1,10)-5) for i in range(10)]
    rabbitList = [r.Rabbit(np.random.randint(1,10)-5,np.random.randint(1,10)-5,100) for i in range(10)]
    saladList = [s.Salad(np.random.randint(1,50)-25,np.random.randint(1,50)-25) for i in range(30)]
    #print len(foxList)
    #print len(rabbitList)
    
    
    def animate(i):
        global foxList, rabbitList, saladList
        
        # New salad grows after 10 rounds
        if i % 10 == 0:
            saladList += [s.Salad(np.random.randint(1,50)-25,np.random.randint(1,50)-25) for j in range(10)]
        
        for fox in foxList:
            # Change position of all foxes (fox walk).
            fox.setCoord(np.random.randint(0,3)-1,np.random.randint(0,3)-1)
            
            #print fox.getLife()
            
            # Kill fox if its starving to death
            if fox.getLife() == 0:
                del foxList[foxList.index(fox)]
            
            # Kill rabbit if fox has neighboring position with rabbit (fox eats the rabbit).
            for rabbit in rabbitList:            
                if fox.getCoord() == rabbit.getCoord():
                    del rabbitList[rabbitList.index(rabbit)]
                    fox.setLife(100) # add more life points to fox (ressources from eating rabbit)
                    print fox.getLife()
            
        
        for rabbit in rabbitList:
            #print rabbit.getCoord()
            # Change position of all rabbits (rabbit walk).
            rabbit.setCoord(np.random.randint(0,3)-1,np.random.randint(0,3)-1)
            #print rabbit.getCoord()
            
            
            # Kill rabbit if its starving to death
            if rabbit.getLife() == 0:
                del rabbitList[rabbitList.index(rabbit)]
        
            # Eat salad if rabbit is at position with salad
            for salad in saladList:
                if rabbit.getCoord() == salad.getCoord():
                    del saladList[saladList.index(salad)]
                    rabbit.setLife(100) # add more life points to rabbit (ressources from eating salad)
                    print rabbit.getLife()
            
        # rabbit mating, if two rabbits overlaps:
        for rabbitI in rabbitList:
            for rabbitJ in rabbitList:
                if rabbitI.getCoord() == rabbitJ.getCoord and rabbitI != rabbitJ:
                    rabbitList += [s.Salad(np.random.randint(1,50)-25,np.random.randint(1,50)-25)]
        
        
        # print out amount of rabbits and foxes:
        #print len(foxList), "foxes after round:", i+1
        #print len(rabbitList), "rabbits after round:", i+1


        # get coordinates for all objects
        foxX=[fox.getCoord()[0] for fox in foxList]
        foxY=[fox.getCoord()[1] for fox in foxList]
        rabbitX=[rabbit.getCoord()[0] for rabbit in rabbitList]
        rabbitY=[rabbit.getCoord()[1] for rabbit in rabbitList]
        saladX=[salad.getCoord()[0] for salad in saladList]
        saladY=[salad.getCoord()[1] for salad in saladList]
        
        #plt.scatter(foxX,foxY, c='red')
        #plt.scatter(rabbitY,rabbitY, c='white')
        foxPlot.set_data(foxX,foxY)
        rabbitPlot.set_data(rabbitX,rabbitY)
        saladPlot.set_data(saladX,saladY)
        
        return foxPlot, rabbitPlot, saladPlot,
        
    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=30, blit=True)
        
    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()