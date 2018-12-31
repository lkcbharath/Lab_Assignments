from hash_table import HashTable

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
	a = input("Enter your word:\n")
	filename = "small.dict"
	with suppress_stdout():
		file = open(filename,"r")
		lines = [line.rstrip('\n') for line in file]
		for line in lines:
			H.inserthash(str(line))
		file.close()

	print(H.searchhash(str(a)))

if __name__ == '__main__':
    main()
        

