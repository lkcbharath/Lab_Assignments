class adjlist:

	def __init__(self,size):
		self.adjlist = [[] for i in range(0,size)]
		self.color = ["White" for i in range(0,size)]
		self.size = size

	def insert(self,i,j):
		# if self.adjlist[i] == None:
			# self.adjlist[i] = []
		self.adjlist[i].append(j)

	def delete(self,i,j):
		self.adjlist[i].remove(j)

	def search(self,i,j):
		n_i = len(self.adjlist[i])
		ret = False
		if j in self.adjlist[i]:
			ret = True
		return ret

	def contents(self):
		for i in range(0,self.size):
			print(self.adjlist[i], sep = ' ', end = '\n')

	def dfs_color(self,v):
		# https://stackoverflow.com/questions/2869647/why-dfs-and-not-bfs-for-finding-cycle-in-graphs
		# Reference for why DFS over BFS
		self.color[v] = "Gray"

		for i in self.adjlist[v]:
			if self.color[i] == "Gray":
				return True
			elif self.color[i] == "White" and self.dfs_color(i) == True:
				return True

		self.color[u] == "Black"
		return False

	def is_cycle(self):
		
		for i in range(0,self.size):
			if self.color[i] == "White":
				if self.dfs_color(i) == True:
					return True

		return False

def main():
	n = int(input("Enter the number of vertices: "))
	l = adjlist(n)

	n = int(input("Enter the number of edges: "))

	print("Enter vertices b/w which there is a directed edge, seperated by a space:")
	for it in range(0,n):
		strx = str(input()).split()
		i = int(strx[0])
		j = int(strx[1])
		l.insert(i,j)
	
	cycle = l.is_cycle()

	if cycle==True:
		print("There is a cycle in the graph")
	else:
		print("There is no cycle in the graph")


if __name__ == '__main__':
	main()