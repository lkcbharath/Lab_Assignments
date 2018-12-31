from mystack import Stack

def isMatched(expr):
    """Checks if the expression 'expr' has matching opening/closing symbols."""
    S = Stack()
    n = len(expr)

    for i in range (0,n):
    	symb = expr[i] #next symbol
    	# print(symb)

    	if symb in ['{','(','[']:
    		S.Push(symb)

    	elif symb in ['}',')',']']:

    		if S.isEmpty():
    			return False
    		if S.Top() == '{' and symb == '}':
    			S.Pop()
    		elif S.Top() == '(' and symb == ')':
    			S.Pop()
    		elif S.Top() == '[' and symb == ']':
    			S.Pop()

    	else:
    		continue

    if S.isEmpty():
    	return True
    else:
    	return False

    # 	elif symb in range(48,58):
    # 		continue

    # 	elif symb in ['+','-','*','/','%']:
    # 		continue

    # 	else:
    # 		print("Error") 
    # 		return 0




    
def main():
	expr = list(input('Enter the expression: '))
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()

