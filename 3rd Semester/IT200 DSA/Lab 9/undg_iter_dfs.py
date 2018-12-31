class adjlist:

	def __init__(self,size):
		self.adjlist = [[] for i in range(0,size)]
		self.size = size
		self.color = ["White" for i in range(0,size)]
		self.discovery = []
		self.time = 0
		self.start_time = [0 for i in range(0,size)]
		self.end_time = [0 for i in range(0,size)]


	def insert(self,i,j):
		self.adjlist[i].append(j)
		self.adjlist[j].append(i)

	def contents(self):
		for i in range(0,self.size):
			print(self.adjlist[i], sep = ' ', end = '\n')

	def dfs(self,v):
		#discovery acts as a stack
		self.discovery.append(v)
		strx = ""

		while self.discovery != []:
			s = self.discovery.pop(0)

			if (self.color[s]=="White"):
				self.color[s]="Black"
				strx = strx + str(s) + " "


			for j in self.adjlist[s]:
				if self.color[j] == "White":
					self.discovery.insert(0,j)
		print(strx)

def main():
	n = int(input("Enter the number of vertices: "))
	l = adjlist(n)
	n_v = n

	n = int(input("Enter the number of edges: "))

	print("Enter vertices b/w which there is an edge, seperated by a space")
	for it in range(0,n):
		strx = str(input()).split()
		i = int(strx[0])
		j = int(strx[1])
		if (i<0) or (j<0):
			print("Graph cannot have negative edge weights!")
			exit()
		elif (i>=n_v) or (j>=n_v):
			print("Vertices are indexed only from 0 to " + str(n_v))
			exit()
		l.insert(i,j)
	
	v = int(input("Enter vertice to perform Depth-First Search on: "))
	print("Depth-First Search on vertex yields:")
	l.dfs(v)

if __name__ == '__main__':
	main()