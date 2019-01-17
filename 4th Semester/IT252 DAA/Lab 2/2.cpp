#include <bits/stdc++.h>
using namespace std;

int find_peak(int arr[], int l, int h){
	
	if(h-l==0){
		return arr[h];
	}

	if (h-l==1){
		if (arr[l]>arr[h])
			return arr[l];
		return arr[h];
	}

	int m = (l+h)/2;
	int mid = arr[m];
	int left = arr[m-1];
	int right = arr[m+1];

	if (left<mid && mid<right)
		return find_peak(arr,m,h);

	if (right<mid && mid<left)
		return find_peak(arr,l,m);

	return mid;

}


int main(){
	int i;
	int arr[] = {10,12,8,4,-3,-15};
	int n = sizeof(arr)/sizeof(arr[0]);

	int result = find_peak(arr,0,n-1);
	cout << result;
	return 0;
}