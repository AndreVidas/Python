# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:49:26 2016

@author: andre
"""

import numpy as n

class RightAngleTriangle:
    def __init__(self,
               x,
               h,
               description = "This shape has not been described yet",
               author = "Nobody has claimed to make this shape yet"):
    
        self.x = x
        self.h = h
        self.description = description
        self.author = author

    def getArea(self):
        return self.x * self.h / 2.0
    
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.h = self.h * scale
    
    def getPerimeter(self):
        return 2 * self.x + n.sqrt(self.x + self.h)
        