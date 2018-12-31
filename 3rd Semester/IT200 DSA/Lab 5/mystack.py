class Stack:
	"""Define the Stack class here.
	   Write a constructor and implement the push, pop and isEmpty functions
	   using Python lists."""
	def __init__(self):
		self.elements = []
		self.top = -1

	def Push(self, x):
		self.top = self.top + 1
		self.elements.append(x)

	def Pop(self):
		if (self.top>=0):
			x = self.elements[self.top]
			self.top = self.top - 1
			self.elements.pop()
			return x

		else:
			print("Stack is empty")
	
	def Top(self):

		if (self.top>=0):
			return self.elements[self.top]
		else:
			print("Stack is empty")

	def isEmpty(self):
		if (self.top>=0):
			return False
		return True


	
