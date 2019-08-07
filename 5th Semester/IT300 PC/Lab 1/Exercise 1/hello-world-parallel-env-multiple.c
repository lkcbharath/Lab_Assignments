#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
    int id;

    #pragma omp parallel 
    {
        id = omp_get_thread_num();
        printf("Hello World! from %3d\n",id);
    }

    return 0;
}