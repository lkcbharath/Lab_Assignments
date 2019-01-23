#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{	
	int n,i,p=1;
	int pid;
	printf("Enter the number: ");
	scanf("%d",&n);
	for(i=n;i>0;i--)
	{
		pid = fork();	
		p=p*i;
		if (pid==0)
			return 0;
	}

	
	printf("%d\n",p);
	
	return 0;
}
