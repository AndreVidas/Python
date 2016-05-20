# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:55:18 2016

@author: andre
"""

class Rectangle:
    """
    This class creates a rectangle.
    """
    def __init__(self,
                 x,
                 y,
                 description = "This shape has not been described yet",
                 author = "Nobody has claimed to make this shape yet"):

        self.x = x
        self.y = y
        self.description = description
        self.author = author
        
    def getArea(self):
        return self.x * self.y
    
    def getPerimeter(self):
        return 2 * self.x + 2 * self.y
    
    def setDescription(self,text):
        self.description = text
    
    def getDescription(self):
        return self.description
    
    def setAuthor(self, text):
        self.author = text
    
    def getAuthor(self):
        return self.author
    
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
    
    def getDimension(self):
        return self.x, self.y



class Square(Rectangle):
    """
    This class creates a square, and inheritates all functions from the Rectangle class.
    """
    def __init__(self,
                 x,
                 description = "This shape has not been described yet",
                 author = "Nobody has claimed to make this shape yet"):
                     
        self.x = x
        self.y = x
        self.description = description
        self.author = author