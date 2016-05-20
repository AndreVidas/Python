# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:08:20 2016

@author: andre
"""

class Salad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getCoord(self):
        return self.x, self.y