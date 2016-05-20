# -*- coding: utf-8 -*-
import numpy as np

class Board:
    def __init__(self, boardMatrix = np.array([[0,0,0],[0,0,0],[0,0,0]])):
        self.boardMatrix = boardMatrix

    def setBoard(self,row,col,value):
        self.boardMatrix[row,col] = value

    def getBoard(self):
        return self.boardMatrix

    def getBoardValue(self,row,col):
        return self.boardMatrix[row,col]

