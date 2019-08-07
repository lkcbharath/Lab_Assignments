#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
    int num_threadz;
    omp_set_num_threads(10);
    #pragma omp parallel 
    {
        if(omp_get_thread_num()==0) {
            num_threadz = omp_get_num_threads();
            printf("Number of threads is %3d\n",num_threadz);
        }
    }

    return 0;
}