
import time

global numexp
global numgen
numgen = 0
numexp = 0

graph = {
          'a': {'b': .9, 'f':  .7},
          'b': {'a':  1, 'c':  .9, 'g':  .7},
          'c': {'b':  1, 'd':  .9, 'h':  .7},
          'd': {'c':  1, 'e':  .9, 'i':  .7},
          'e': {'d':  1, 'j':  .7},
          'f': {'a': .8, 'g':  .9, 'k':  .7},
          'g': {'b': .8, 'f':   1, 'h':  .9, 'l': .7},
          'h': {'c': .8, 'g':   1, 'i':  .9, 'm': .7},
          'i': {'d': .8, 'h':   1, 'j':  .9, 'n': .7},
          'j': {'e': .8, 'i':   1, 'o':  .7},
          'k': {'f': .8, 'l':  .9, 'p':  .7},
          'l': {'g': .8, 'k':   1, 'm':  .9, 'q': .7},
          'm': {'h': .8, 'l':   1, 'n':  .9, 'r': .7},
          'n': {'i': .8, 'm':   1, 'o':  .9, 's': .7},
          'o': {'j': .8, 'n':   1, 't':  .7},
          'p': {'k': .8, 'q':  .9},
          'q': {'p':  1, 'r':  .9, 'l':  .8},
          'r': {'q':  1, 's':  .9, 'm':  .8},
          's': {'r':  1, 't':  .9, 'n':  .8},
          't': {'s':  1, 'o':  .8},
          
        }

class Node:
    def __init__(self, dirty, start, path, cost):
        self.cost = cost
        self.__path = path
        self.pos = start
        self.dirty = dirty
        self.numdirty = len(dirty)
        global numgen
        numgen += 1
        # print('NODE PATH: '+str(self.path))

    def isclean(self):
        if self.numdirty==0:
            return True
        return False
    
    def suck(self):
        if self.pos in self.dirty:
            self.cost += .6
            self.numdirty -= 1
            self.dirty.remove(self.pos)
        return self

    def addToPath(self, data):
        self.__path.append(data)

    def incCost(self, num):
        self.cost+=num

    def getPath(self):
        return self.__path


def createNode(dirty, start, path, cost):
    node = Node(dirty, start, path, cost)
    return node


# Priority Queue code adapted from https://www.geeksforgeeks.org/priority-queue-in-python/

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    # for popping an element based on lowest cost
    def delete(self):
        try:
            mincost = -1
            if not self.isEmpty():
                i = 0
                while mincost == -1:
                    if type(self.queue[i]) == Node:
                        mincost = i
                    i+=1

                for i in range(len(self.queue)):
                    if type(self.queue[i]) == Node:
                        if self.queue[i].cost < self.queue[mincost].cost :
                            mincost = i
                item = self.queue[mincost]
                del self.queue[mincost]
                return item
        except IndexError:
            print()
            exit()

def uct(dirty, start):

    global numexp
    queue = PriorityQueue()
    node = createNode(dirty, start, [], 0)
    queue.insert(node)

    visited = {start: [start]}

    while not queue.isEmpty():

        temp = queue.delete()
        temp.addToPath(temp.pos)
        # print('temppath: '+str(temp.path))

        path = temp.getPath()
        cost = temp.cost

        # print(str(path))
        # print('dirty: '+str(dirty))
        temp.suck()

        numexp += 1

        if temp.isclean():

            print('success')
            # print(str(temp.getPath()))
            # print(str(temp.cost))
            return

        else:

            # print('cost: '+str(temp.cost))
            # print('position: '+str(temp.pos))

            for i in graph[temp.pos]:
                # print(str(i))
                temp2 = createNode(temp.dirty, i, path, cost)

                # print('cost '+str(graph[temp.pos][i]))
                # print('temp2 cost: '+str(temp2.cost))

                temp2.incCost(graph[temp.pos][i])
                
                # print('dirty: '+str(temp2.dirty))
                if temp2.pos in visited:
                    if visited[temp2.pos]==temp2.cost:
                        continue

                queue.insert(temp2)

                del temp2
        del temp


dirty1 = ['b', 'i', 'o']
start1 = 'g'
dirty2 = ['b', 'f', 'i', 'm']
start2 = 'l'



time1 = time.time()
uct(dirty1, start1)
print('Numgen: '+str(numgen))
print('Numexp: '+str(numexp))
numgen = 0
numexp = 0

time2 = time.time()
uct(dirty2, start2)
time3 = time.time()

print('Room 1 time: '+str(time2-time1))
print('Room 2 time: '+str(time3-time2))
print('Numgen: '+str(numgen))
print('Numexp: '+str(numexp))