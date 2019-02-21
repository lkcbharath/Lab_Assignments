class Set:
	def __init__(self,value,parent):
		self.value = value
		self.rank = 0
		self.parent = parent

class DisjointSet:

	def __init__(self,n):
		
		self.array = [-1 for i in range(n)]
		self.size = n

	def makeSet(self,value,parent):
		InsertSet = Set(value,parent)
		self.array[value] = InsertSet

	def findSet(self,x):
		if x.parent!=x:
			y = findSet(x.parent)
			x.parent = y
			return y
		return x

	def union(self,x,y):

		rx = self.findSet(x)
		ry = self.findSet(y)

		if (rx.rank > ry.rank):
			ry.parent = rx
		elif (rx.rank < ry.rank):
			rx.parent = ry
		else:
			ry.parent = rx
			rx.rank += 1


	def printSets(self):
		for i in range(self.size):
			print(self.array[i].parent)

def main():
	ds = DisjointSet(1)
	ds.makeSet(0,0)
	ds.printSets()

if __name__ == '__main__':
	main()