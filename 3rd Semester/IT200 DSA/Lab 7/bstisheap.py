class BSTNode:

	def __init__(self,value):
		self.parent = None
		self.value = value
		self.left = None
		self.right = None

	def insert(self,root,x):
		temp = BSTNode(x)

		if root == None:
			root = temp
			return

		if (x>root.value):
			if (root.right == None):
				temp.parent = root
				root.right = temp
			else:
				self.insert(root.right,x)
		else:
			if (root.left == None):
				temp.parent = root
				root.left = temp
			else:
				self.insert(root.left,x)


	def search(self,root,key): 
	    if root is None or root.value == key: 
	        return root 

	    if root.value < key: 
	        return self.search(root.right,key) 
	    return self.search(root.left,key) 


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

	def successor(self,node):
		temp = node
		if temp.right != None:
			return self.minimum(temp.right)

		y = temp.parent

		while y!=None and y.right==temp:
			temp = y
			y = y.parent

		return temp

	def predecessor(self,node):
		temp = node
		if temp.left != None:
			return self.maximum(temp.left)

		y = temp.parent

		while y!=None and y.right==temp:
			temp = y
			y = y.parent

		return y
	def delete(self,root,key): 
	  	# works for only root, will implement positional
	    # Base Case 
	    if root is None: 
	        return root  
	  
	    if key < root.value: 
	        root.left = self.delete(root.left, key) 
	  
	    elif(key > root.value): 
	        root.right = self.delete(root.right, key) 
	  
	    # If key is same as root's key, then this is the node 
	    # to be deleted 
	    else: 
	          
	        if root.left is None: 
	            temp = root.right  
	            root = None 
	            return temp  
	              
	        elif root.right is None: 
	            temp = root.left  
	            root = None
	            return temp 
	  
	        # Node with two children: Get the inorder successor 
	        # (smallest in the right subtree) 
	        temp = self.successor(root.right) 
	  
	        # Copy the inorder successor's content to this node 
	        root.value = temp.value 
	  
	        # Delete the inorder successor 
	        root.right = delete(root.right , temp.value) 
	  
	  
	    return root

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


	def isBinaryHeap(self,root):
		left = root.left
		right = root.right
		ret = True

		while left!=None and right!=None:
			ret = self.isBinaryHeap(left)
			ret = self.isBinaryHeap(right)
			if root.value < left.value or root.value < right.value:
				return False
				break

		return ret

				


def main():
	r = BSTNode(10)
	r.insert(r,5)
	r.insert(r,6)
	r.insert(r,8)
	r.insert(r,12)

	print(r.isBinaryHeap(r))


if __name__ == '__main__':
	main()
	         

			



