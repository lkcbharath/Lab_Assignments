#define N 1024
#define T 256 // max threads per block

#include <stdio.h>

__global__ void vecAdd (int *a, int *b, int *c);
void printArray(int a[], int b[], int c[]);

int main() {
	int a[N], b[N], c[N];
	int *dev_a, *dev_b, *dev_c;
	clock_t t;
	double time_taken;

	FILE *fp;
    fp = fopen ("output.txt","a");

	// initialize a and b with real values (NOT SHOWN)
	int size = N * sizeof(int);
	for (int i = 0; i < N; i++) {
		a[i] = i;
		b[i] = i/2;
	}

	t = clock();

	cudaMalloc((void**)&dev_a, size);
	cudaMalloc((void**)&dev_b, size);
	cudaMalloc((void**)&dev_c, size);

	cudaMemcpy(dev_a, a, size,cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, b, size,cudaMemcpyHostToDevice);

	vecAdd<<<(int)ceil(N/T),T>>>(dev_a,dev_b,dev_c);

	cudaMemcpy(c, dev_c, size,cudaMemcpyDeviceToHost);

	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);
	
	t = clock() - t;
	time_taken = ((double)t)/CLOCKS_PER_SEC;
	printf("Vector addition with 256 threads per block and padding for array of length %d took %lf seconds to execute \n", N, time_taken); 

	fprintf (fp, "%d %lf\n", N, time_taken);

	// printArray(a,b,c);

	fclose(fp);

	exit (0);
}

__global__ void vecAdd (int *a, int *b, int *c) {
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	if (i < N) {
		c[i] = a[i] + b[i];
	}
}

void printArray(int a[], int b[], int c[]) {

	printf("Array a:\n");
	for(int i = 0; i < N; i++){
		printf("%d ", a[i]);
    }
    printf("\n\nArray b:\n");
    for(int i = 0; i < N; i++){
		printf("%d ", b[i]);
    }
    printf("\n\nArray c:\n");
    for(int i = 0; i < N; i++){
		printf("%d ", c[i]);
	}
	printf("\n");
}
