#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yet another Tic Tac Toe game

@author: André Vidas Olsen
"""



################################################
# tic tac toe game
################################################
import numpy as np

class Board:
    
    def __init__(self):
        self.board = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
    
    def resetBoard(self):
        Board.__init__(self)
    
    def printBoard(self):
        print("-------------")
        print("|",self.board[0,0],"|",self.board[0,1],"|",self.board[0,2],"|")
        print("-------------")
        print("|",self.board[1,0],"|",self.board[1,1],"|",self.board[1,2],"|")
        print("-------------")
        print("|",self.board[2,0],"|",self.board[2,1],"|",self.board[2,2],"|")
        print("-------------")


        #print(self.board)
    
    def setPeice(self, x, y, player):
        self.board[x,y] = player 
        
        
    def isFull(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i,j] == " ":
                    return False
        return True

    
    def isTaken(self, x, y):
        if self.board[x,y] != " ":
            return True
        else:
            return False
            

    def hasWon(self, player):
        for i in range(0,3):
            # check rows
            if all(self.board[i,:] == player):
                return True
            
            # check columns
            if all(self.board[:,i] == player):
                return True
            
        # check diagonal
        if all(self.board.diagonal() == player):
            return True
        
        # check opposite diagonal
        if all(np.fliplr(self.board).diagonal() == player):
            return True
            
        # if not won    
        return False
            
    


class Player:
    
    def __init__(self):
        self.player = "x"
    
    def shiftPlayer(self):
        if self.player == "x":
            self.player = "o"
        else:
            self.player = "x"
    
    def getPlayer(self):
        return self.player
        


###### main #######
if __name__ == "__main__":
    board = Board()
    players = Player()
    cont = True
    while(cont):
        board.printBoard()
        print("move player:", players.getPlayer())
        x = int(input("row: "))
        y = int(input("col: "))
        
        x -= 1
        y -= 1
        
        if board.isTaken(x,y):
            print("Coordinate already taken. Please take make another move.")
        else:
            board.setPeice(x,y,players.getPlayer())
            if board.hasWon(players.getPlayer()):
                board.printBoard()
                print("Player", players.getPlayer(), "has won!!")
                cont = False
            elif board.isFull():
                print("Draw")
                cont = False
            players.shiftPlayer()

















"""
# tests
spil = Board()
#spil.resetBoard()
spil.setPeice(1,2,"x")
spil.setPeice(2,2, "o")
spil.printBoard()

print("Is (1,2) taken? ", spil.isTaken(1,2))
print("Is (0,2) taken? ", spil.isTaken(0,2))

print(spil.isFull())
spil.setPeice(0,0,"x")
spil.setPeice(1,0, "o")
spil.setPeice(1,1,"x")
spil.setPeice(2,0, "o")        
spil.setPeice(2,1, "o")        
spil.setPeice(0,2, "o")        
spil.setPeice(0,1, "o")
spil.printBoard()
print(spil.isFull())

spil.resetBoard()
spil.printBoard()

print(spil.hasWon("x"))
spil.setPeice(0,0,"x")
spil.setPeice(0,1,"x")
spil.setPeice(0,2,"x")
spil.printBoard()
print(spil.hasWon("x"))
print(spil.hasWon("o"))




spil.resetBoard()
spil.printBoard()

spil.setPeice(0,0,"x")
spil.setPeice(1,0,"x")
spil.setPeice(2,0,"x")
spil.printBoard()
print(spil.hasWon("x"))
print(spil.hasWon("o"))


spil.resetBoard()
spil.printBoard()

spil.setPeice(0,0,"x")
spil.setPeice(1,1,"x")
spil.setPeice(2,2,"x")
spil.printBoard()
print(spil.hasWon("x"))
print(spil.hasWon("o"))


spil.resetBoard()
spil.printBoard()

spil.setPeice(2,0,"x")
spil.setPeice(1,1,"x")
spil.setPeice(0,2,"x")
spil.printBoard()
print(spil.hasWon("x"))
print(spil.hasWon("o"))

spillere = Player()
print(spillere.getPlayer())
spillere.shiftPlayer()
print(spillere.getPlayer())
"""