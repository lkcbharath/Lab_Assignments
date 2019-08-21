#include <omp.h>
#include <stdio.h>
#define N 500

int main()
{
    int m = N,n = N,p = N,q = N,i,j,k;
    int a[N][N],b[N][N],c[N][N];
    double start_time, end_time;

    // Some initial values
    for(i=0;i<N;++i) {
        for(j = 0;j < N;j++) {
            a[i][j]=i;
            b[i][j]=j;
        }
    }

    start_time = omp_get_wtime();

    #pragma omp parallel shared(a,b,c) private(i,j,k) 
    {
        #pragma omp for  schedule(static)
        for (i=0;i<m;++i) {
            for (j=0;j<n;++j) {
                a[i][j]=0;
                for (k=0;k<p;++k)
                    a[i][j] += b[i][k]*c[k][j];
            }
        }
    }
    
    end_time = omp_get_wtime();

    printf("Time taken for parallel approach = %lf s\n", end_time - start_time);

    return 0;
}