# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:52:51 2016

@author: andre
"""
import Shape.Rectangle as rect
#import Shape.Square as sq
import Shape.Triangle as tr

# instantiate 
box1 = rect.Rectangle(5,8)
box2 = rect.Rectangle(10,1)
box3 = rect.Square(2)
triangle1 = tr.RightAngleTriangle(10,3)


# use objects
print triangle1.getArea()

box1.setAuthor("André")
print box1.getAuthor()
print box1.getDimension()

print box3.getArea()

print box3.getAuthor()

box4 = rect.Rectangle(10,12,"New box","André")
print box4.getAuthor()
print box4.getDescription()


print box4.getArea()
box4.scaleSize(2)
print box4.getArea()

triangle1.scaleSize(3)
print triangle1.getArea()
print triangle1.getPerimeter()