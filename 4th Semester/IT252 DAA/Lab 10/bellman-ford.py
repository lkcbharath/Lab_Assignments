from collections import defaultdict
import sys

# map i to S,A,B,C

class Graph:
    def __init__(self,n):
        self.vertices = [i for i in range(n)]
        self.adjlist = [[] for i in range(n)]
        self.revlist = [[] for i in range(n)]
        self.dist_table = [[] for i in range(n)]
        self.dist_table[0].append(0)
        for i in range(1,len(self.dist_table)):
            self.dist_table[i].append(sys.maxsize)
    
    def addEdge(self,u,v,w):
        self.adjlist[u].append([v,w])
        self.revlist[v].append([u,w])

    def bellman_ford(self):
        # step 1: preprocessing by filling values
        for k in range(1,len(self.vertices)):
            for u in range(1,len(self.vertices)):
                self.calc_shortest_path(u,k)

        # # step 2: relax
        # for k in range(1,len(self.vertices)):
        #     for v in range(len(self.adjlist)):
        #         for u in self.adjlist[v]:
        #             self.relax(u[0],v,u[1])
    
    # def relax(self,u,v,w):
    #     if self.dist_table[v][-1] > self.dist_table[]

    
    def calc_shortest_path(self,v,k):

        if k < len(self.dist_table[v]):
            return self.dist_table[v][k]

        min = sys.maxsize
        for u in self.revlist[v]:
            u_sp = self.calc_shortest_path(u[0],k-1)
            if u_sp != sys.maxsize and min > u_sp + u[1]:
                min = self.calc_shortest_path(u[0],k-1) + u[1]
        
        # self.dist_table[v][k] = min
        self.dist_table[v].append(min)
        return min
    
    def __str__(self):
        for i in self.dist_table:
            print(i)
        return ""
    
def main():
    # n_e = 1
    n_v = 8
    
    G = Graph(n_v)
    G.addEdge(0,1,10)
    G.addEdge(0,7,8)
    G.addEdge(1,5,2)
    G.addEdge(2,1,1)
    G.addEdge(2,3,1)
    G.addEdge(3,4,3)
    G.addEdge(4,5,-1)
    G.addEdge(5,2,-2)
    G.addEdge(6,1,-4)
    G.addEdge(6,5,-1)
    G.addEdge(7,6,1)

    # for e in range(n_e):
    #     str_ = input()
    #     list_ = str_.split()
    #     G.addEdge(int(list_[0]),int(list_[1]),int(list_[2]))
    
    G.bellman_ford()
    
    print(G)


if __name__ == '__main__':
    main()
