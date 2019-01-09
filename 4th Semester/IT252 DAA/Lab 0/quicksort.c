#include <stdio.h>

void printArray(int arr[],int n){

	for (int i = 0; i<n; ++i){
		printf("%d ", arr[i]);
	}
	printf("\n");
}

int partition(int arr[], int low, int high){
	int pivot = arr[low];
	int temp,i = (low-1),j;
	printArray(arr,5);

	for (j=low+1; j<high; ++j){
		if (arr[j] <= pivot){
			
			//swap
			i++;
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			
		}

	}
	//swap
	temp = arr[i-1];
	arr[i-1] = arr[low];
	arr[low] = temp;

	// printArray(arr,5);
	// printf("i+1 - %d\n",i+1);

	return i;

}


void quickSort(int arr[], int low, int high){
	if (low<high){
		
		int pi = partition(arr,low,high);

		quickSort(arr,low,pi-1);
		quickSort(arr,pi+1,high);

	}
}

int main(){

	int arr[] = {5,1,2,4,3};
	int n = sizeof(arr)/sizeof(arr[0]);

	printArray(arr,n);


	quickSort(arr,0,4);

	printArray(arr,n);

	return 0;
}

