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
		component = []
		visited = [False for i in range(0,self.size)]
		visited[v] = True
		q.append(v)

		while q!=[]:
			s = q.pop(0)
			component.append(s)
			for i in self.adjlist[s]:
				if visited[i] == False:
					visited[i] = True
					q.append(i)

		return component

def main():
	n = int(input("Enter the number of vertices: "))
	l = adjlist(n)

	n = int(input("Enter the number of edges: "))

	print("Enter vertices b/w which there is an edge, seperated by a space:")
	for it in range(0,n):
		strx = str(input()).split()
		i = int(strx[0])
		j = int(strx[1])
		l.insert(i,j)

	component_list = [0 for i in range(0,l.size)]
	component_seperated = []

	for i in range(0,len(component_list)):
		if component_list[i]==0:
			component = l.bfs(i)
			
			for j in component:
				component_list[j] = 1

			component_seperated.append(component)

	print("Number of connected components:",len(component_seperated))
	print("Vertices in each component:")
	for k in component_seperated:
		str1 = ' '.join(str(l) for l in k)
		print(str1)

if __name__ == '__main__':
	main()