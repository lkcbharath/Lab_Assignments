#include <bits/stdc++.h>
using namespace std;


void maxSubArray(int* a, int n){
	int start=0,end=0,curr_max=0,prev_max=0,start_o=0,i;
	prev_max = a[0];

    for(i=0; i<n; i++){
        curr_max += a[i];

        if(curr_max < 0){
            start = i+1;
            curr_max = 0;
        }

        else if(curr_max > prev_max){
            end = i;
            start_o = start;
            prev_max = curr_max;
        }

    }

    printf("%d %d \n",start_o,end);
}

int main(){
	int i;
	int arr[] = {3,2,-1,100};
	int n = sizeof(arr)/sizeof(arr[0]);
	int sum[n];
	maxSubArray(arr,n);

	return 0;
}