from avl import *
from bst import *
import time

def main():
	myTree = AVL_Tree()
	root = None 

	myTree2 = BST_Tree()
	r = None

	
	print("AVLNode")
	start_time = time.time()

	for i in range (0,100001):
		root = myTree.insert(root, int(i)) 
	print("­­­ %s seconds ­­­" % str(time.time() - start_time))

	start_time = time.time()
	myTree.search(root,100000)
	print("­­­ %s seconds ­­­" % str(time.time() - start_time))

	start_time = time.time()
	for i in range (0,100001):
		myTree.delete(root,int(i))
	print("­­­ %s seconds ­­­" % str(time.time() - start_time))

	
	print("BSTNode")
	start_time = time.time()

	for i in range (0,100001):
		r = myTree2.insert(r,int(i))
	print("­­­ %s seconds ­­­" % str(time.time() - start_time))

	start_time = time.time()
	myTree2.search(r,100000)
	print("­­­ %s seconds ­­­" % str(time.time() - start_time))

	start_time = time.time()
	for i in range (100000,0,-1):
		myTree2.delete(r,int(i))
	print("­­­ %s seconds ­­­" % str(time.time() - start_time))


	

if __name__ == '__main__':
	main()