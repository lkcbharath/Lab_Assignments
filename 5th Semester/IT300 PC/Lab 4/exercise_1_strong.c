/*
**  PROGRAM: Matrix Multiplicatin
**
**  PURPOSE: This is a simple program to calculate the nth Fibonacci number. 
**           Each number in the Fibonacci series is the sum of the two previous numbers before it.
**			 The first two numbers in the series are 0 and 1.
**           Example of the first 10 numbers in the Fibonacci series:
**
**                0,1,1,2,3,5,8,13,21,34
**
**           We use a recursive function to find the previous two elements, taking n as input. 
**           If n goes below 2, then we return n.
**           Else, we return the sum of the values returned by the functions taking n-1 and n-2 as input.
**
**  USAGE:   Run the program and enter an integer in the command line when prompted.
**
**  HISTORY: Written by Bharath Adikar, Aug 2019
*/
#include <omp.h>
#include <stdio.h>
#define N 800

int main()
{
    int m = N,n = N,p = N,q = N,i,j,k;
    int a[N][N],b[N][N],c[N][N];
    double start_time, end_time;

    // Some initial values
    for(i=0;i<N;++i) {
        for(j = 0;j < N;j++) {
            b[i][j]=i;
            c[i][j]=j;
        }
    }

    for(int itr=1;itr<=16;++itr){
        omp_set_num_threads(itr);

        start_time = omp_get_wtime();

        #pragma omp parallel shared(a,b,c) private(i,j,k) 
        {
            #pragma omp for schedule(static)
            for (i=0;i<m;++i) {
                for (j=0;j<n;++j) {
                    a[i][j]=0;
                    for (k=0;k<p;++k)
                        a[i][j] += b[i][k]*c[k][j];
                }
            }
        }
        
        end_time = omp_get_wtime();

        printf("Time taken for matrix multiplication with %d threads = %lf s\n",itr,end_time - start_time);
        
    }
    

    return 0;
}