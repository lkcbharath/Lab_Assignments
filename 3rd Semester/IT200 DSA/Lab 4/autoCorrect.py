from hash_table import HashTable
from string import ascii_lowercase
from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def main():

	H = HashTable()
	#change to ispell after initial test
	filename = "ispell.dict"
	with suppress_stdout():
		file = open(filename,"r")
		lines = [line.rstrip('\n') for line in file]
		for line in lines:
			H.inserthash(str(line))
		file.close()

	str1 = input("Enter a word\n")


	if H.searchhash(str1)=="Found":
		print("Word is correct")
	else:
		print("Suggestions:")
		count=0
		printed=[]
		for i in range(len(str1)):
			for j in range(26):
				st=str1[:i]+chr(j+97)+str1[i+1:] # each letter replaced at i
				s1=str1[:i]+chr(j+97)+str1[i:] # letter inserted at i
				s2=str1[:i]+str1[i+1:] #letter deleted at i

				#st not in printed: to check if word already exists in result

				if st not in printed and H.searchhash(st)=="Found":
					print(st)
					printed.append(st)
					count=count+1
				if s1 not in printed and H.searchhash(s1)=="Found":
					print(s1)
					printed.append(s1)
					count=count+1
				if s2 not in printed and H.searchhash(s2)=="Found":
					print(s2)
					printed.append(s2)
					count=count+1
		if count==0:
			print("No Suggestions")


	#--------------------------------------------

	# print("Word suggestions:")
	# n = len(str1)
	# displaylist = []
	# result = []

	# #i is position of bad letter
	# for i in range(0,n):
	# 	#reset list to check
	# 	list_str = list(str1)

	# 	#loop through alphabets
	# 	for c in ascii_lowercase:
	# 		list_str[i] = c
	# 		str2 = ''.join(list_str)
	# 		res = H.displayhash(str2)
	# 		if res != []:
	# 			displaylist.append(res)

	# for word in displaylist:
	# 	result += word

	# result2 = list(set(result))
	# for word in result2:
	# 	print(word)

	#-------------------------------------

	# print("Extended suggestions:")

	# if n > 1:
	# 	for i in range(0,n):
	# 		list_str = list(str1)
	# 		for c in ascii_lowercase:
	# 			list_str[i] = c
	# 			str2 = ''.join(list_str)
	# 			res = H.displayhash(str2)
	# 			if res != []:
	# 				displaylist.append(res)

	# for word in displaylist:
	# 	result += word

	# result3 = list(set(result))
	# for word in result3:
	# 	if word not in result2:
	# 		print(word)

	#add a single letter

		

if __name__ == '__main__':
    main()
        

