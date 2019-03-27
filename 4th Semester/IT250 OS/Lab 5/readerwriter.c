#include<pthread.h>
#include<semaphore.h>
#include<stdio.h>
#include<stdlib.h>

pthread_mutex_t x,wsem;
pthread_t tid;
int readcount;

void intialize()
{
    pthread_mutex_init(&x,NULL);
    pthread_mutex_init(&wsem,NULL);
    readcount=0;
}

void * reader (void * param)
{
    int waittime;
    int i = (int)param;
    waittime = rand() % 5;
    printf("\nReader %d is trying to enter",i);
    pthread_mutex_lock(&x);
    readcount++;
    if(readcount==1)
        pthread_mutex_lock(&wsem);
    printf("\n%d reader(s) are inside",readcount);
    pthread_mutex_unlock(&x);
    sleep(waittime);
    pthread_mutex_lock(&x);
    readcount--;
    if(readcount==0)
        pthread_mutex_unlock(&wsem);
    pthread_mutex_unlock(&x);
    printf("\nReader %d is Leaving",i);
}   

void * writer (void * param)
{
    int waittime;
    int i = (int)param;
    waittime=rand() % 3;
    printf("\nWriter %d is trying to enter",i);
    pthread_mutex_lock(&wsem);
    printf("\nWriter %d has entered",i);
    sleep(waittime);
    pthread_mutex_unlock(&wsem);    
    printf("\nWriter %d is leaving",i);
    sleep(30);
    exit(0);
}

int main()
{
    int n1,n2,i;    
    printf("\nEnter the no of readers: ");
    scanf("%d",&n1);
    printf("\nEnter the no of writers: ");
    scanf("%d",&n2);
    for(i=0;i<n1;i++)
        pthread_create(&tid,NULL,reader,(void *)i);  
    for(i=0;i<n2;i++)
        pthread_create(&tid,NULL,writer,(void *)i);
    sleep(30);
    exit(0);
}