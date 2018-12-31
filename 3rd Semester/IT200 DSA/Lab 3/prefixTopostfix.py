from mystack import Stack

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
	return False


def pre_to_post(strs):
	strs = reverse(strs)
	s = strs.split()
	St = Stack()
	final = ""

	for value in s:
		
		if value in ['+','-','*','/','%']:

			a = St.Pop()
			b = St.Pop()
			final = str(a) + " " + str(b) + " " + str(value)
			St.Push(final)
			
		elif value.isalpha():
			St.Push(value)

		elif is_number(value):
			St.Push(value)

		else:
			print("Error")
			exit(0)

	return St.Top()


    
def main():
	expr = input('Enter the prefix expression: ')
	print('The equivalent postfix expression is',pre_to_post(expr))

if __name__ == '__main__':
    main()

