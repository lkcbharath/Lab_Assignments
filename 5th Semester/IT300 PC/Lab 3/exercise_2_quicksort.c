/* C implementation QuickSort */
#include <omp.h>
#include <stdio.h> 
#include <stdlib.h>

// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
	int t = *a; 
	*a = *b; 
	*b = t; 
} 

/* This function takes last element as pivot, places 
the pivot element at its correct position in sorted 
	array, and places all smaller (smaller than pivot) 
to left of pivot and all greater elements to right 
of pivot */
int partition (int arr[], int low, int high) 
{ 
	int pivot = arr[high]; // pivot 
	int i = (low - 1); // Index of smaller element 

	for (int j = low; j <= high- 1; j++) 
	{ 
		// If current element is smaller than the pivot 
		if (arr[j] < pivot) 
		{ 
			i++; // increment index of smaller element 
			swap(&arr[i], &arr[j]); 
		} 
	} 
	swap(&arr[i + 1], &arr[high]); 
	return (i + 1); 
} 

/* The main function that implements QuickSort 
arr[] --> Array to be sorted, 
low --> Starting index, 
high --> Ending index */
void quickSort(int arr[], int low, int high) 
{ 
	if (low < high) 
	{ 
		/* pi is partitioning index, arr[p] is now 
		at right place */
		int pi = partition(arr, low, high); 

		// Separately sort elements before 
		// partition and after partition 
		quickSort(arr, low, pi - 1); 
		quickSort(arr, pi + 1, high); 
	} 
} 

/* The main function that implements QuickSort 
arr[] --> Array to be sorted, 
low --> Starting index, 
high --> Ending index */
void quickSortP(int arr[], int low, int high) 
{ 
	if (low < high) 
	{ 
		/* pi is partitioning index, arr[p] is now 
		at right place */
		int pi;
		#pragma omp task shared(pi)
		pi = partition(arr, low, high); 

		// Separately sort elements before 
		// partition and after partition 
		#pragma omp taskwait
		quickSortP(arr, low, pi - 1); 

		#pragma omp taskwait
		quickSortP(arr, pi + 1, high); 
	} 
} 

/* Function to print an array */
void printArray(int arr[], int size) 
{ 
	int i; 
	for (i=0; i < size; i++) 
		printf("%d ", arr[i]); 
	printf("\n"); 
} 

// Driver program to test above functions 
int main() 
{ 
	double start_time,time_taken;
	int i,n;
	printf("Enter array size:");
	scanf("%d",&n);
	int arr[n],arr2[n];
	// printf("Enter array elements one by one");

	for(i=0;i<n;++i){
		arr[i] = n-i;
		arr2[i] = n-i;
	}

	start_time = omp_get_wtime();
	quickSort(arr, 0, n-1); 
	time_taken = omp_get_wtime()-start_time;

	printf("Sorted array: "); 
	// printArray(arr, n); 
	printf("Time taken for serial approach is %lf s\n",time_taken);

	start_time = omp_get_wtime(); 
	quickSortP(arr2, 0, n-1); 
	time_taken = omp_get_wtime()-start_time;
	printf("Sorted array: "); 
	// printArray(arr2, n); 
	printf("Time taken for parallel approach is %lf s\n",time_taken);
	return 0; 
} 
