class maxheap:
	def __init__(self,array):
		if array==None:
			self.elements = []
			self.capacity = 0
		else:
			self.elements = array
			self.capacity = len(array)

		
	def left(self,i):
		return int((2*i)+1)
	def right(self,i):
		return int((2*i)+2)
	def parent(self,i):
		return int(0.5*i)
	def maximum(self):
		return self.elements[0]

	def swap(self,i,j):
		temp = self.elements[i]
		self.elements[i] = self.elements[j]
		self.elements[j] = temp

	def insert(self,x):
		self.elements.append(int(x))
		self.capacity = self.capacity + 1

		i = self.capacity - 1
		j = self.parent(i)
		
		while self.elements[i] > self.elements[j]:
			self.swap(i,j)
			i = j
			j = self.parent(i)

		print(self.elements,self.capacity)

	def delete(self):
		# self.elements[0] = self.elements[self.capacity-1]
		self.elements[0] = self.elements.pop()
		self.capacity = self.capacity - 1
		# print(self.elements,self.capacity)
		i = 0
		j = self.left(i)
		k = self.right(i)

		n = self.capacity
		while i<n:
			if j<n and self.elements[i] < self.elements[j]:
				self.swap(i,j)
				i = j
				j = self.left(i)
				k = self.right(i)
			elif k<n and self.elements[i] < self.elements[k]:
				self.swap(i,k)
				i = k
				j = self.left(i)
				k = self.right(i)
			else:
				break

	def heapify(self,n,i):
		#start from i, keep going down until heap condition satisfied
		largest = i
		l = self.left(i)
		r = self.right(i)
		if l < n and self.elements[i] < self.elements[l]: 
			largest = l 
		if r < n and self.elements[largest] < self.elements[r]: 
			largest = r
		if largest != i: 
			self.swap(i,largest)
			self.heapify(n,largest) 

	def buildheap(self):
		#examine from the bottom row, make them all heaps
		n = self.capacity

		for i in (int(0.5*n)-1,-1,-1):
			self.heapify(i)

	def heapsort(self):
		n = self.capacity
		#1. Build a max heap from the input data. 
		for i in range(n-1, -1, -1): 
			self.heapify(n,i) 
		#2. Largest item is root. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
		#3. Repeat above steps while size of heap is greater than 1.
		for i in range(n-1, 0, -1): 
			self.swap(i,0)
			self.heapify(i,0) 


	def extractmax(self):
		maxi = self.elements[0]
		self.elements[0] = self.elements.pop()
		self.capacity = self.capacity - 1
		self.heapify(0)
		return maxi

	def __str__(self):
		strs = ""
		for i in range(0,self.capacity):
			strs = strs + str(self.elements[i]) + " "
		return strs

# BUILD-MAX-HEAP(A)
#   A.heapsize = A.length
#   for i = A.length/2 downto 1
#      MAX-HEAPIFY(A,i)


# HEAPSORT(A)
#   BUILD-MAX-HEAP(A)
#   for i = A.length downto 2
#      exchange A[1] with A[i]
#      A.heapsize = A.heapsize - 1
#      MAX-HEAPIFY(A,1)

def main():
	H = maxheap([i for i in range (100,0,-1)])
	H.heapsort()
	print(H)

if __name__ == '__main__':
	main()

