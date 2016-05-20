# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:52:33 2016

@author: andre
"""

class Rabbit:
    def __init__(self, x, y, life = 10, coordRate = 1, lifeRate = 1):
        self.x = x
        self.y = y
        self.life = life
        self.coordRate = coordRate
        self.lifeRate = lifeRate
    
    def setCoord(self,x,y):
        self.x = self.x + x*self.coordRate
        self.y = self.y + y*self.coordRate
        self.life = self.life - self.lifeRate
    
    def getCoord(self):
        return self.x, self.y
    
    def getLife(self):
        return self.life
    
    def setLife(self,lifeAdd):
        self.life = self.life + lifeAdd