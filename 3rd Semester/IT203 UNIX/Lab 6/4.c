#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
	pid_t pid[3];
	printf("Initializing fork:\n\n");
	int count = 0;

	pid[0] = fork();
	pid[1] = fork();
	pid[2] = fork();
	printf("Current process id before execution %d\n",getpid());
	printf("Process id of child 1 %d\n",pid[0]);
	printf("Process id of child 2 %d\n",pid[1]);
	printf("Process id of child 3 %d\n",pid[2]);
	printf("Current process id after execution %d\n\n",getpid());
	for(int i =0;i<3;++i){
		// printf("count = %d\n",count++);
		
		// if (pid[i]==0)
		// 	printf("child %d \n",i);
		// else if (pid[i]>0)
		// 	printf("parent %d \n",i);
		// else
		// 	printf("fork %d failed\n",i);
	}

	return 0;
}