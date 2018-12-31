class adjlist:

	def __init__(self,size):
		self.adjlist = [[] for i in range(0,size)]
		self.size = size
		self.color = ["White" for i in range(0,size)]
		self.time = 0
		self.discovery = []
		self.start_time = [0 for i in range(0,size)]
		self.end_time = [0 for i in range(0,size)]

	def insert(self,i,j):
		self.adjlist[i].append(j)
		self.adjlist[j].append(i)

	def contents(self):
		for i in range(0,self.size):
			print(self.adjlist[i], sep = ' ', end = '\n')

	def dfs(self,v):
		self.color[v] = "Gray"
		self.discovery.append(v)

		self.time = self.time + 1
		self.start_time[v] = self.time

		for j in self.adjlist[v]:
			if self.color[j] == "White":
				self.dfs(j)

		self.color[v] = "Black"

		self.time = self.time + 1
		self.end_time[v] = self.time

	def contents_time(self):
		for i in range(0,self.size):
			v = self.discovery[i]
			str1 = str(v) + " | Timing: " + str(self.start_time[v]) + " " + str(self.end_time[v])
			print(str1) 


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
	
	v = int(input("Enter vertice to perform Depth-First Search on: "))
	# s = l.bfs(v)
	# str1 = ' '.join(str(j) for j in s)
	print("Depth-First Search on vertex yields:")
	l.dfs(v)
	l.contents_time()

if __name__ == '__main__':
	main()