import heapq as hq

class Node:

    def __init__(self,f,s,l,r):
        self.freq = f
        self.symb = s
        self.left = l
        self.right = r

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __str__(self):
        l = None
        r = None
        if self.left!=None:
            l = self.left.symb
        if self.right!=None:
            r = self.right.symb
        str_ = "Frequency:" + str(self.freq) + ",Symbol:" + str(self.symb) 
        str_ += ",Left Symb:" + str(l) + ",Right Symb:" + str(r) 
        return str_
    
    def print_encoding(self,code):
        if self.left:
            self.left.print_encoding(code + '0')
        if self.right:
            self.right.print_encoding(code + '1')
        else:
            print("Symbol:",self.symb,"Frequency:",self.freq,"Encoding:",code)
            # file=open('code.txt','a+')
            # file.write(code + self.symb + '\n')
            # file.close()

def prettyprint(list_):
    listx = []
    for i in list_:
        l = None
        r = None
        if i.left!=None:
            l = i.left.symb
        if i.right!=None:
            r = i.right.symb
        listx.append((i.freq,i.symb,l,r))
    print(listx)

def Huffman(S,F,n):
    leaves = []
    H = []
    for i in range(n):
        node = Node(F[i],S[i],None,None)
        leaves.append(node)
    
    hq.heapify(leaves)

    for i in range(n-1):
        # prettyprint(leaves)
        t1 = hq.heappop(leaves)
        t2 = hq.heappop(leaves)
        node = Node((t1.freq + t2.freq),'I_N',t1,t2)
        hq.heappush(leaves,node)
        
    root = leaves[0]
    print("Total file size in bits =",root.freq)
    root.print_encoding('')

def main():
    # file = open('code.txt','w+')
    # file.write('')
    # file.close()

    Symbols = ['a','b','c','d','e','f']
    Frequencies = [20,12,10,8,4,3]
    Huffman(Symbols,Frequencies,6)

if __name__ == '__main__':
    main()