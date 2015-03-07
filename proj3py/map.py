#map.py
#Rachael Byrkit rmb11d
from random import randint

#0 : empty
#1 : player
#2 : enemy (pyro)
#3 : trap (backstab)
#4 : backpack (intel)

class Map:
    def __init__(self):
        self.map=[[0 for x in range (5)] for x in range (5)]



    def setMap(self):
        #set player locationn
        self.map[2][0]=1
        #set trap
        self.map[randint(0,4)][randint(0,4)] = 3
        #set enemies
        for x in range (0,4):
            randx=randint(0,4)
            randy=randint(0,4)
            if self.map[randx][randy] is not 0:
                break
            else:
                self.map[randx][randy]= 2
        #set backpack
        randx=randint(0,4)
        randy=randint(0,4)
        while self.map[randx][randy] is not 0:
            randx=randint(0,4)
            randy=randint(0,4)
        else:
            self.map[randx][randy]=4
        
                



    #def nextMove:
        


    
    
