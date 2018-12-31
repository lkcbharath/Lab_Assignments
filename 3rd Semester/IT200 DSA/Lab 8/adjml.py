class adjlist:
	
	def __init__(self,size):
		self.adjlist = [[] for i in range(0,size)]
		self.size = size

	def insert(self,i,j):
		if self.adjlist[i] == None:
			self.adjlist[i] = []
		self.adjlist[i].append(j)

		if self.adjlist[j] == None:
			self.adjlist[j] = []
		self.adjlist[j].append(i)

	def delete(self,i,j):
		self.adjlist[i].remove(j)
		self.adjlist[j].remove(i)

	def search(self,i,j):
		n_i = len(self.adjlist[i])
		n_j = len(self.adjlist[j])

		ret = False
		if n_i<=n_j and j in self.adjlist[i]:
			ret = True
		elif i in self.adjlist[j]:
			ret = True

		return ret
	def contents(self):
		for i in range(0,self.size):
			str1 = ','.join(str(j) for j in self.adjlist[i])
			print("Vertex " + str(i) + ": " + str1)
			
class adjmatrix:

	def __init__(self,size):
		self.matrix = [[0 for i in range(0,size)] for i in range(0,size)]
		self.size = size
	def insert(self,i,j):
		self.matrix[i][j] = 1
		self.matrix[j][i] = 1
	def delete(self,i,j):
		self.matrix[i][j] = 0
		self.matrix[j][i] = 0
	def search(self,i,j):
		if self.matrix[i][j]:
			return True
		return False
	def contents(self):
		for i in range(0,self.size):
			str1 = ' '.join(str(j) for j in self.matrix[i])
			print(str1)

def main():
	n = int(input("Enter the number of vertices: "))
	m = adjmatrix(n)
	l = adjlist(n)

	n = int(input("Enter the number of edges :"))
	print("Enter vertices b/w which there is an edge, seperated by a space")
	for it in range(0,n):
		strx = str(input()).split()
		i = int(strx[0])
		j = int(strx[1])
		m.insert(i,j)
		l.insert(i,j)

	print("The adjacency matrix is:")
	m.contents()
	print("The adjacency list is:")
	l.contents()

if __name__ == '__main__':
	main()