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

	def contents(self):
		for i in range(0,self.size):
			print(self.adjlist[i], sep = ' ', end = '\n')

	def bfs(self,v):
		q = []
		distance = [[i,0] for i in range(0,self.size)]
		result = []
		visited = [False for i in range(0,self.size)]
		
		q.append(v)
		visited[v] = True
		
		while q!=[]:
			s = q.pop(0)
			dist = distance[s][1]
			result.append([s,dist])

			for i in self.adjlist[s]:
				if visited[i] == False:
					visited[i] = True
					distance[i][1] = dist + 1
					q.append(i)

		return result

def main():
	n = int(input("Enter the number of vertices: "))
	l = adjlist(n)

	n = int(input("Enter the number of edges: "))

	print("Enter vertices b/w which there is an edge, seperated by a space")
	for it in range(0,n):
		strx = str(input()).split()
		i = int(strx[0])
		j = int(strx[1])
		l.insert(i,j)
	
	v = int(input("Enter vertice to perform Breadth-First Search on: "))
	s = l.bfs(v)
	# str1 = ' '.join(str(j) for j in s)
	print("Breadth-First Search on vertex yields: (vertex,distance from source)")
	for i in s:
		str1 = ','.join(str(j) for j in i)
		print(str1)

if __name__ == '__main__':
	main()