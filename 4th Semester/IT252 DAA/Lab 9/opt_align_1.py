def choice(c_1,c_2,c_3):
    if c_1<=c_2 and c_1<=c_3:
        return 1
    if c_2<=c_1 and c_2<=c_3:
        return 2
    if c_3<=c_1 and c_3<=c_2:
        return 3

class EditDistance:

    def __init__(self,x,y):
        self.T = [[None for i in range(len(y))] for j in range(len(x))]
        self.align = []
        self.x = x
        self.y = y

    def diff(self,i,j):
        if self.x[i]==self.y[j]:
            return 0
        return 1
    
    def alignment(self,i,j,choice):
        if choice==1:
            self.align.append([self.x[i],self.y[j]])
        elif choice==2:
            self.align.append([self.x[i-1],self.y[j]])
        elif choice==3:
            self.align.append([self.x[i],self.y[j-1]])

    def edit_distance(self,i,j):
        print(i,j,self.T[i][j])

        if j==0:
            self.T[i][j] = i
            return i
        if i==0:
            self.T[i][j] = j
            return j

        if self.T[i][j]:
            return self.T[i][j]
        
        c_1 = self.diff(i,j) + self.edit_distance(i-1,j-1)
        c_2 = 1 + self.edit_distance(i-1,j)
        c_3 = 1 + self.edit_distance(i,j-1)

        print('alignment calls')
        self.alignment(i,j,choice(c_1,c_2,c_3))

        self.T[i][j] = min(c_1,c_2,c_3)
        
        return self.T[i][j]
    
    def print_alignment(self):
        for x in self.align:
            print(x)

        # for i in range(len(self.align)):
            # print(self.align[i],self.T[i][i])

def main():
    x = input("Enter String 1")
    y = input("Enter String 2")

    E = EditDistance(x,y)
    
    n_x = len(x)-1
    n_y = len(y)-1

    n = E.edit_distance(n_x,n_y)

    
    print("Edit distance is",n)
    E.print_alignment()
    pass

if __name__ == '__main__':
    main()