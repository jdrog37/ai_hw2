# Python program to print DFS traversal from a given graph
from collections import defaultdict
 
# This class represents a directed graph using adjacency
# list representation
class Room:
    def __init__(self, vertices, map, dirty):
        self.V = vertices
        self.room = defaultdict(list)
        self.map = map

        #stores costs
        self.left = 1.0
        self.right = 0.9
        self.up = 0.8
        self.down = 0.7
        self.suck = 0.6
        self.cost = 0.0

        self.dirty = dirty
 
    def addEdge(self, index, target):
        self.room[index].append(target)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self, src, target, maxDepth, path):
        if self.map[src[0]][src[1]] == target:
            self.map[src[0]][src[1]] = 0
            self.cost += self.suck
            self.dirty -= 1
            return True
 
        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.room[src]:
            #print(i)
            if(self.DLS(i,target,maxDepth-1, path)):
                last = path[-1]
                path.append(i)
                #self.findCost(last, i)
                return True
        return False
 
    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def idt_search(self, src, target, maxDepth, path):
        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i, path)):
                return True
        return False
    
    def findCost(self, last, current):
        if(current[0] == last[0]+1):
            self.cost += self.down
        elif(current[0] == last[0]-1):
            self.cost += self.up
        elif(current[1] == last[1]+1):
            self.cost += self.right
        elif(current[1] == last[1]-1):
            self.cost += self.left

def createRoom(map, dirty):
# Create a graph given in the above diagram
    room = Room (20, map, dirty)
    room.addEdge((0,0), (0,1))
    room.addEdge((0,0), (1,0))

    room.addEdge((1,0), (1,1))
    room.addEdge((1,0), (2,0))
    room.addEdge((1,0), (0,0))

    room.addEdge((2,0), (2,1))
    room.addEdge((2,0), (3,0))
    room.addEdge((2,0), (1,0))

    room.addEdge((3,0), (3,1))
    room.addEdge((3,0), (2,0))

    room.addEdge((3,1), (3,2))
    room.addEdge((3,1), (2,1))
    room.addEdge((3,1), (3,0))

    room.addEdge((2,1), (1,1))
    room.addEdge((2,1), (2,2))
    room.addEdge((2,1), (3,1))
    room.addEdge((2,1), (2,0))

    room.addEdge((1,1), (1,2))
    room.addEdge((1,1), (0,1))
    room.addEdge((1,1), (1,0))
    room.addEdge((1,1), (2,1))

    room.addEdge((0,1), (0,2))
    room.addEdge((0,1), (0,0))
    room.addEdge((0,1), (1,1))

    room.addEdge((0,2), (1,2))
    room.addEdge((0,2), (0,3))
    room.addEdge((0,2), (0,1))

    room.addEdge((1,2), (1,3))
    room.addEdge((1,2), (2,2))
    room.addEdge((1,2), (1,1))
    room.addEdge((1,2), (0,2))

    room.addEdge((2,2), (2,3))
    room.addEdge((2,2), (3,2))
    room.addEdge((2,2), (2,1))
    room.addEdge((2,2), (1,2))

    room.addEdge((3,2), (3,3))
    room.addEdge((3,2), (3,1))
    room.addEdge((3,2), (2,2))

    room.addEdge((3,3), (3,4))
    room.addEdge((3,3), (2,3))
    room.addEdge((3,3), (3,2))

    room.addEdge((2,3), (2,4))
    room.addEdge((2,3), (1,3))
    room.addEdge((2,3), (2,2))
    room.addEdge((2,3), (3,3))

    room.addEdge((1,3), (1,4))
    room.addEdge((1,3), (0,3))
    room.addEdge((1,3), (1,2))
    room.addEdge((1,3), (2,3))

    room.addEdge((0,3), (0,4))
    room.addEdge((0,3), (1,3))
    room.addEdge((0,3), (0,2))

    room.addEdge((0,4), (1,4))
    room.addEdge((0,4), (0,3))

    room.addEdge((1,4), (2,4))
    room.addEdge((1,4), (0,4))
    room.addEdge((1,4), (1,3))

    room.addEdge((2,4), (3,4))
    room.addEdge((2,4), (1,4))
    room.addEdge((2,4), (2,3))

    room.addEdge((3,4), (2,4))
    room.addEdge((3,4), (3,3))

    return room

def algorithm(room, starting_position, path, target_state, maxDepth):
    while(room.dirty != 0):
        temp = [starting_position]
        if room.idt_search(starting_position, target_state, maxDepth, temp) == True:
            #print(path)
            temp.pop(0)
            i=len(temp)
            while(i!=0):
                path.append(temp[i-1])
                i -= 1
            #print(path)

            starting_position = path[-1]
            '''print("sp: ")
            print(starting_position)
            print()
            print(room.map)'''
        else:
            print ("Error")

    for i in range(len(path)-1):
        room.findCost(path[i], path[i+1])
    print(room.cost)
    print(path)

dirty = 3
room1 = createRoom([[0,1,0,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1],
                    [0,0,0,0,0]],
                    dirty)

dirty = 4
room2 = createRoom([[0,1,0,0,0],
                    [1,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]],
                    dirty)

r1_starting_position = (1,1)
r2_starting_position = (2,1)
path1 = [r1_starting_position]
path2 = [r2_starting_position]
target_state = 1
maxDepth = 8

algorithm(room1, r1_starting_position, path1, target_state, maxDepth)
algorithm(room2, r2_starting_position, path2, target_state, maxDepth)