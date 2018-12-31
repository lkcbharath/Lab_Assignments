class BSTNode:
	def __init__(self,value):
		self.parent = None
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.value)


class BST_Tree:

	def insert(self,root,x):

		insert = BSTNode(x)

		if not root:
			return insert
		temp = root

		if temp.right == None:
			if x > temp.value:
				temp.right = insert
				temp.right.parent = temp
		elif temp.left == None:
			if x <= temp.value:
				temp.left = insert
				temp.left.parent = temp


		while temp!=None:
			if x > temp.value:
				if temp.right == None:
					temp.right = insert
					temp.right.parent = temp
					break
				else:
					temp = temp.right
			else:
				if temp.left == None:
					temp.left = insert
					temp.left.parent = temp
					break
				else:
					temp = temp.left



		return root

	def search(self,root,key): 
		if(root==None):
			# print("It does not exist")
			return None
		while root!=None:
			if(root.value<key):
  				root=root.right
			elif(root.value>key):
  				root=root.left
			elif(root.value==key):
				# print("Found")
				return root
		return None

	def minimum(self,root):
		temp = root

		while (temp.left!=None):
			temp = temp.left

		return temp

	def maximum(self,root):
		temp = root

		while (temp.right!=None):
			temp = temp.right

		return temp
	def successor(self,root):
		key=root
		if key.right is not None:
			return self.minimum(key.right)
		else:
			y = key.parent
			# print(y)
			while y is not None and key==y.right:
				key = y
				y = y.parent
			return y

	def predecessor(self,root):
		key=root
		if key.left is not None:
			return self.minimum(key.left)
		else:
			y = key.parent
			# print(y)
			while y is not None and key==y.left:
				key = y
				y = y.parent
			return y

	def delete(self,root,key): 
	  	temp = self.search(root,key)
	  	y = temp.parent

	  	#leaf

	  	if temp.left==None and temp.right == None:
	  		if y.left == temp:
	  			y.left = None
	  		else:
	  			y.right = None

	  	elif temp.left == None:
	  		right = temp.right
	  		if y.left == temp:
	  			y.left = right
	  		else:
	  			y.right = right
	  		right.parent = y

	  	elif temp.right == None:
	  		left = temp.left
	  		if y.right == temp:
	  			y.right = left
	  		else:
	  			y.left = left
	  		left.parent = y

	  	else:
	  		z = self.successor(temp)
	  		y = z.value
	  		self.delete(z,y)
	  		z.parent = temp.parent

	  		if temp.parent is not None:
	  			if temp.parent.right ==temp:
	  				temp.parent.right = z

	  			elif temp.parent.left == temp:
	  				temp.parent.left = z

	  		if temp.parent is None:
	  			temp.value = y

	  		z.right = temp.right
	  		z.left = temp.left

	  	# return root

	def inOrder(self,root): 
  
	    if root: 
	        self.inOrder(root.left) 
	        print(root.value)
	        self.inOrder(root.right) 

	def preOrder(self,root): 
  
	    if root:
	        print(root.value)
	        self.preOrder(root.left)
	        self.preOrder(root.right) 

	def postOrder(self,root): 
	    if root: 
	        self.postOrder(root.left) 
	        self.postOrder(root.right)
	        print(root.value)

	def _pre(self, root):
	    if root is None:
	        return ''

	    if root is not None:
	        left = self._pre(root.left)
	        right = self._pre(root.right)
	        return str(root.value) + ' ' + left + ' ' + right

	def __str__(self):
		return str(self.value)

def main():
	myTree = BST_Tree()
	r = None
	r = myTree.insert(r,5)
	r = myTree.insert(r,12)
	r = myTree.insert(r,8)
	r = myTree.insert(r,11)


	print("Maximum value:",myTree.maximum(r));
	print("Minimum value:",myTree.minimum(r));

	print("Predecessor of 8:",myTree.predecessor(myTree.search(r,11)))

	print("Successor of 8:",myTree.successor(myTree.search(r,11)))

	print("Inorder Traversal:")
	myTree.inOrder(r)
	print("Preorder Traversal:")
	myTree.preOrder(r)
	print("Postorder Traversal:")
	myTree.postOrder(r)

	print("Deleting 8")
	myTree.delete(r,8)

	print("Inorder Traversal:")
	myTree.inOrder(r)
	print("Preorder Traversal:")
	myTree.preOrder(r)
	print("Postorder Traversal:")
	myTree.postOrder(r)






if __name__ == '__main__':
	main()
	         

			



