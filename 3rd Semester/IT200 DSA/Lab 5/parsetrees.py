from bst import *
from prefixEval import *
from mystack import *


def main():
	str = input("Enter parathentized expression")
	l = str.split()
	curr = BSTNode('x') #temporary
	#choices: (,+-*/,0-9,)

	for x in l:
		
		if x == '(':
			curr.left = BSTNode('y')
			curr.left.parent = curr
			curr = curr.left

		elif x in ['+','-','*','/','%']:
			curr.value = x
			curr.right = BSTNode('z')
			curr.right.parent = curr
			curr = curr.right

		elif x in ['0','1','2','3','4','5','6','7','8','9']:
			curr.value = x
			curr = curr.parent

		elif x == ')':
			if curr.parent != None:
				curr = curr.parent

	print("Pre-order Traversal:")
	curr.preOrder(curr)
	print("Post-order Traversal:")
	curr.postOrder(curr)

	print("Value of expression is:", eval_prefix(curr._pre(curr)))

if __name__ == '__main__':
	main()