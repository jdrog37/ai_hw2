'''
HW2 Authors:
Mikey Joyce
Jake Rogers
Roshan Neupane
'''

#0 indicates clean; 1 indicates dirty; 2 indicates starting location, might need to change this
#data set for uniform cost tree search
room1_UCT = [[0,1,0,0,0],
             [0,2,0,1,0],
             [0,0,0,0,1],
             [0,0,0,0,0]] #starting position room1_UCT[1,1]
room2_UCT = [[0,1,0,0,0],
             [1,0,0,1,0],
             [0,2,1,0,0],
             [0,0,0,0,0]]#starting position room1_UCT[2,1]

#data set for uniform cost graph search
room1_UCG = [[0,1,0,0,0],
             [0,2,0,1,0],
             [0,0,0,0,1],
             [0,0,0,0,0]]#starting position room1_UCG[1,1]
room2_UCG = [[0,1,0,0,0],
             [1,0,0,1,0],
             [0,2,1,0,0],
             [0,0,0,0,0]]#starting position room1_UCT[2,1]

#data set for iterative deepening tree search
room1_IDT = [[0,1,0,0,0],
             [0,2,0,1,0],
             [0,0,0,0,1],
             [0,0,0,0,0]]#starting position room1_IDT[1,1]
room2_IDT = [[0,1,0,0,0],
             [1,0,0,1,0],
             [0,2,1,0,0],
             [0,0,0,0,0]]#starting position room1_UCT[2,1]

#array dimensions
columns = 5
rows = 4

#costs
left = 1.0
right = 0.9
up = 0.8
down = 0.7
suck = 0.6