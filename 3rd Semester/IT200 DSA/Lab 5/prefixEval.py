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

def eval_prefix(strs):
	strs = reverse(strs)
	s = strs.split()
	St = Stack()
	count = 0
	
	for value in s:
		
		value = reverse(value)

		if value in ['+','-','*','/','%']:

			b = St.Pop()
			a = St.Pop()

			if value == '+':
				result = a+b
				St.Push(float(result))

			elif value == '-':
				result = a-b
				St.Push(float(result))

			elif value == '/':
				result = a/b
				St.Push(float(result))

			elif value == '*':
				result = a*b
				St.Push(float(result))

			elif value == '%':
				result = a%b
				St.Push(float(result))


		elif is_number(value):
			St.Push(float(value))

		else:
			print("Error")


	return St.Top()


def main():
	expr = input('Enter the prefix expression: ')
	print('The value of the expression is',eval_prefix(expr))

if __name__ == '__main__':
    main()

