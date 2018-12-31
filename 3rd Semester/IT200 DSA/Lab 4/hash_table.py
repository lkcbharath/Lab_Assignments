from linked_list import *

class HashTable:

	#attributes = list of mod 30 elements, store each value
	def __init__(self):
		self.T = [None for i in range(30)]
		
	#insert string into hash table
	def inserthash(self,strs):
		l = list(strs)
		n = len(l)

		a = 33 #prime number for min. collision
		p = ord(l[n-1])
		j = n-2

		while j >= 0:
			p = p*a + ord(l[j])
			j = j-1
			
		i = p%30


		if self.T[i] == None:
			self.T[i] = LinkedList()
			temp = self.T[i].head
			self.T[i].insertLL(strs, temp)

		else:
			temp = self.T[i].head
			# while temp.next!=None:
			# 	temp = temp.next
			self.T[i].insertLL(strs,temp)

	def searchhash(self,strs):
		l = list(strs)
		n = len(l)

		a = 33 #prime number for min. collision
		p = ord(l[n-1])
		j = n-2

		while j >= 0:
			p = p*a + ord(l[j])
			j = j-1
			
		i = p%30


		temp = self.T[i]
		x = temp.searchLL(strs)
		if (x == "Found"):
			return "Found"

		return "Not Found"

	def displayhash(self,strs):
		l = list(strs)
		n = len(l)

		a = 33 #prime number for min. collision
		p = ord(l[n-1])
		j = n-2

		while j >= 0:
			p = p*a + ord(l[j])
			j = j-1
			
		i = p%30

		result2 = []

		for i in range(0,30):
			if self.T[i] != None:
				temp = self.T[i]
				result = list(temp.searchLLHash(strs))
				for word in result:
					if word!=[]:
						result2.append(word)
		return result2


	def keys(self):
		count = 0;
		l = []

		for i in range(0,30):
			if self.T[i] != None:
				l.append(i)

		return l


# def main():
# 	H = HashTable()
# 	H.inserthash("Please")
# 	H.inserthash("Testing")
# 	H.inserthash("Python")
# 	print(H.keys())
# 	H.searchhash("Please")
# 	H.searchhash("Test")
# 	H.searchhash("Testing")

# if __name__ == '__main__':
#     main()

        


