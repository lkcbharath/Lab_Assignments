/*
**  PROGRAM: Matrix Multiplicatin
**
**  PURPOSE: This is a simple program to multiply two matrices. 
**           It contains both serial and parallel versions.
**           
**			 The first two numbers in the series are 0 and 1.
**           Example of the first 10 numbers in the Fibonacci series:
**
**                0,1,1,2,3,5,8,13,21,34
**
**           We use a recursive function to find the previous two elements, taking n as input. 
**           If n goes below 2, then we return n.
**           Else, we return the sum of the values returned by the functions taking n-1 and n-2 as input.
**
**  USAGE:   Run the program and enter an integer in the command line when prompted, where the integer is the size of the array.
**
**  HISTORY: Written by Bharath Adikar, Sep 2019
*/
#include <omp.h>
#include <stdio.h>
#define N 500

int main()
{
    int m = N,n = N,p = N,q = N,i,j,k;
    int a[N][N],b[N][N],c[N][N];
    double start_time_s,time_taken_s,start_time_p, time_taken_p;
    FILE *fp;
    fp = fopen ("output.txt","w");

    // Some initial values
    start_time_s = omp_get_wtime();

    for(i=0;i<N;++i) {
        for(j = 0;j < N;j++) {
            b[i][j]=i;
            c[i][j]=j;
        }
    }
    time_taken_s = omp_get_wtime() - start_time_s;

    printf("Serialised part = %lf s\n",time_taken_s);

    start_time_p = omp_get_wtime();
    for (i=0;i<m;++i) {
        for (j=0;j<n;++j) {
            a[i][j]=0;
            for (k=0;k<p;++k)
                a[i][j] += b[i][k]*c[k][j];
        }
    }
    time_taken_p = omp_get_wtime() - start_time_p;

    printf("Time taken for serial matrix multiplication = %lf s\n",time_taken_p);
    

    for(int itr=1;itr<=16;++itr){
        omp_set_num_threads(itr);

        start_time_s = omp_get_wtime();
        for (i=0;i<m;++i) {
            for (j=0;j<n;++j) {
                a[i][j]=0;
                for (k=0;k<p;++k)
                    a[i][j] += b[i][k]*c[k][j];
            }
        }
        time_taken_s = omp_get_wtime() - start_time_s;

        start_time_p = omp_get_wtime();

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
        
        time_taken_p = omp_get_wtime()-start_time_p;

        printf("Time taken for parallel matrix multiplication with %d threads = %lf s\n",itr,time_taken_p);
        fprintf (fp, "This is line %d\n",itr + 1);
    }
    
    fclose(fp);
    return 0;
}