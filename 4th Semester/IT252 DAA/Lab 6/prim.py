from collections import defaultdict
import sys
import heapq

class Graph:
    def __init__(self,n):
        self.vertices = [Node(i) for i in range(n)]
        self.adjlist = defaultdict(list)
    
    def addEdge(self,u,v,w):
        self.adjlist[u].append([v,w])

    def printMST(self):
        pass

    def prims(self):
        # pass
        x = self.vertices[0]
        x.cost = 0
        H = [x]
        while H:
            u = heapq.heappop(H)
            for v in self.adjlist[u]:
                if u.cost > v[1]:
                    u.cost = v[1]
                    u.prev = v[0]
                    update_priority(H,u)


class Node:
    def __init__(self,i):
        self.value = i
        self.cost = sys.maxsize
        self.prev = None

def update_priority(H,u):
    pass
    


def main():
    pass

if __name__ == '__main__':
    main()