#include <omp.h>
#include <stdio.h>
#define N 327000

int main(){
    long int i,n=N;
    long int a[N];
    double b[N];
    double start_time,end_time; 

    for(i=0;i<N;++i){
        a[i] = i; 
    } 
    
    start_time = omp_get_wtime();
    
    #pragma omp parallel
    {
        #pragma omp for schedule(guided,1000)
        for(i=0; i<n-1;i++) {
            b[i]=(a[i]+a[i+1])/2.0;
        }
    }

    end_time = omp_get_wtime();

    printf("Time taken for parallel guided scheduling approach = %lf s\n", end_time - start_time);

    return 0;
}