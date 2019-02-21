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
		self.printSets
		x_set = self.array[x]

		if x_set.parent!=x_set.value:
			
			y = self.findSet(x_set.parent)
			x_set.parent = y.value
			return y
		
		return x_set

	def union(self,x,y):

		rx = self.findSet(x)
		ry = self.findSet(y)

		if (rx.rank > ry.rank):
			ry.parent = rx.value
		elif (rx.rank < ry.rank):
			rx.parent = ry.value
		else:
			ry.parent = rx.value
			rx.rank += 1


	def printSets(self):
		for i in range(self.size):
			print(self.array[i].parent, end = ' ')
		print("")

def main():
	ds = DisjointSet(5)
	ds.makeSet(1,2)
	ds.makeSet(0,2)
	ds.makeSet(2,2)
	ds.makeSet(3,4)
	ds.makeSet(4,4)
	ds.union(2,3)
	ds.printSets()

if __name__ == '__main__':
	main()