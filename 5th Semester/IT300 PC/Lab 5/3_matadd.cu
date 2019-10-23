#include<stdio.h>
#define N 1280
#define BLOCK_DIM 16

__global__ void matrixAdd (int *a, int *b, int *c);
void printArray(int a[N][N], int b[N][N], int c[N][N]);

int main() {
    int a[N][N], b[N][N], c[N][N];
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            a[i][j] = i+j;
            b[i][j] = i-j;
            c[i][j] = 0;
        }
    }
    int *dev_a, *dev_b, *dev_c;
    int size = N * N * sizeof(int);
    clock_t t;
	double time_taken;

    FILE *fp;
    fp = fopen ("output.txt","a");

    t = clock();

    // initialize a and b with real values (NOT SHOWN)
    cudaMalloc((void**) &dev_a, size);
    cudaMalloc((void**) &dev_b, size);
    cudaMalloc((void**) &dev_c, size);

    cudaMemcpy (dev_a, a, size, cudaMemcpyHostToDevice) ;
    cudaMemcpy (dev_b, b, size, cudaMemcpyHostToDevice) ;
    
    dim3 dimBlock(BLOCK_DIM, BLOCK_DIM) ;
    dim3 dimGrid( (int) ceil (N/dimBlock.x) , (int) ceil (N/dimBlock.y));
    
    matrixAdd<<<dimGrid, dimBlock>>> (dev_a,dev_b,dev_c);
    
    cudaMemcpy(c, dev_c, size, cudaMemcpyDeviceToHost);
    cudaFree(dev_a); 
    cudaFree(dev_b); 
    cudaFree(dev_c);

    t = clock() - t;
	time_taken = ((double)t)/CLOCKS_PER_SEC;
	printf("fun() took %lf seconds to execute \n", time_taken); 

	fprintf (fp, "%d %lf\n", N, time_taken);

    // printArray(a,b,c);

    fclose(fp);

    exit (0);
}

__global__ void matrixAdd (int *a, int *b, int *e) {
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int index = col + row * N;
    if (col < N && row < N) {
        e[index] = a[index] + b[index] ;
        //printf("a[i][j] = %d, b[i][j] = %d, i,j = %d,%d\n", a[i][j], b[i][j], i, j);
    }
}

void printArray(int a[N][N], int b[N][N], int c[N][N]) {

    printf("Array a:\n");
	for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    printf("\n\nArray b:\n");
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }
    printf("\n\nArray c:\n");
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
    printf("\n");

}
