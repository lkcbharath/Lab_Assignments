from linked_list import LinkedList
from linked_list import ListNode

class HashTableComp:

	#attributes = list of mod 30 elements, store each value
	def __init__(self):
		self.T = [None for i in range(30)]
		
	#insert string into hash table
	def inserthash(self,strs):
		l = list(strs)
		n = len(l)
		hashvalue=0

		for j in range(0,n):
			x = ord(str(l[j]))
			hashvalue = hashvalue + x

		i = hashvalue%30

		if self.T[i] == None:

			self.T[i] = LinkedList()
			temp = self.T[i].head
			self.T[i].insertLL(strs, temp)
			self.T[i].printLL()

		else:
			temp = self.T[i].head
			while temp.next!=None:
				temp = temp.next
			self.T[i].insertLL(strs,temp)



	def searchhash(self,strs):
		l = list(strs)
		n = len(l)

		hashvalue=0
		for j in range(0,n):
			x = ord(l[j])
			hashvalue += x
			
		i = hashvalue%30

		for i in range(0,30):
			if self.T[i] != None:
				temp = self.T[i]
				x = temp.searchLL(strs)
				if (x == "Found"):
					print(x)
					return
		print(x)
		return

	def keys(self):
		count = 0;
		l = []

		for i in range(0,30):
			if self.T[i] != None:
				l.append(i)

		return l


def main():
	H = HashTableComp()
	H.inserthash("Please")
	H.inserthash("Testing")
	H.inserthash("Python")
	print(H.keys())
	H.searchhash("Please")
	H.searchhash("Test")
	H.searchhash("Testing")

if __name__ == '__main__':
    main()

        

