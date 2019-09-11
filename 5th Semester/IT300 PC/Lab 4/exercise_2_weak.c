#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

static long num_steps = 10000000;
double step;

int main() {

    int i;
    double x,pi,sum,aux,start_time_s,time_taken_s,start_time_p,time_taken_p;
    long num_steps = 10000000;

    start_time_s = omp_get_wtime();

    x=0;
    sum = 0.0;
    step = 1.0/(double)num_steps;

    printf("Serialised part = %lf s\n",time_taken_s);

    time_taken_s = omp_get_wtime() - start_time_s;

    start_time_p = omp_get_wtime();

    for (i=0; i<num_steps; i=i+1){

        x=(i+0.5)*step;
        aux=4.0/(1.0+x*x);
    
        sum = sum + aux;
    }
    pi=step*sum;

    time_taken_p = omp_get_wtime() - start_time_p;
    
    printf("Value of pi: %lf. Time taken for serial calculation: %lf s\n",pi,time_taken_p);  


    for(int itr=1;itr<=16;++itr){
        omp_set_num_threads(itr);
        x=0;
        sum = 0.0;
        step = 1.0/(double)num_steps;
        
        start_time_p = omp_get_wtime();

        #pragma omp parallel private(i,x,aux) shared(sum) 
        {
            #pragma omp for schedule(static) 
                for (i=0; i<num_steps; i=i+1){

                    x=(i+0.5)*step;
                    aux=4.0/(1.0+x*x);
                
                #pragma omp atomic
                    sum = sum + aux;
                }
        }
        pi=step*sum;

        time_taken_p = omp_get_wtime() - start_time_p;
        
        printf("Value of pi: %lf. Time taken for parallel calculation using %d threads: %lf s\n",pi,itr,time_taken_p);  
    }

    return 0;
}