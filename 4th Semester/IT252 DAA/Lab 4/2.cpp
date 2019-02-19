#include <bits/stdc++.h>

using namespace std;

int FindMost(int *A, int startIndex, int endIndex)
{  // input array A
	int x,y;

	if (startIndex == endIndex)  // base case
	        return A[startIndex]; 
	
	x = FindMost(A, startIndex, (startIndex + endIndex - 1)/2);
	y = FindMost(A, (startIndex + endIndex - 1)/2 + 1, endIndex);

	if (x == -1 && y == -1) 
	    return -1;
	else if (x == -1 && y != -1) 
	    return y;
	else if (x != -1 && y == -1) 
	    return x;
	else if (x != y) 
	    return -1;
	else 
		return x;

}

int main(){

	int n, i;

	n = 8;

	int a[] = {1,1,3,1,2,3,1,23	};

	int result = FindMost(a,0,n-1);

	cout << result << endl;

	return 0;
}