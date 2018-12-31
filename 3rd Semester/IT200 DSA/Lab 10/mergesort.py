A = [3,5,6,8,1,2,4,7]

def mergeSort(low,high):
	
	if low >= high:
		return

	mid = int((low+high)*0.5)

	mergeSort(low,mid-1)
	mergeSort(mid,high)

	mergeFunction(low,mid,high)

def mergeFunction(low,mid,high):
	L = []
	R = []
	i = low
	l = 0
	r = 0
	for i in range(low,mid+1):
		L.append(A[i])
	for i in range(mid+1,high):
		R.append(A[i])

	l = 0
	r = 0
	i = low

	while (l<len(L)) and (r<len(R)):
		if L[l] <= R[r]:
			A[i] = L[l]
			l = l + 1
		else:
			A[i] = R[r]
			r = r + 1
		i = i + 1

	while (l<len(L)):
		A[i] = L[l]
		i = i + 1
		l = l + 1

	while (r<len(R)):
		A[i] = R[r]
		i = i + 1
		r = r + 1



def main():
	mergeSort(0,len(A))
	print(A)

	

if __name__ == '__main__':
	main()