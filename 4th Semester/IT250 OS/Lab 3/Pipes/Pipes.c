// C program to illustrate 
// pipe system call in C 
// shared by Parent and Child 
#include <stdio.h> 
#include <unistd.h> 
#define MSGSIZE 16 
char* msg1 = "hello, world #1"; 
char* msg2 = "hello, world #2"; 
char* msg3 = "hello, world #3";

int main() 
{ 
	char inbuf[MSGSIZE]; 
	int p[2], q[2], pid, nbytes; 

	if (pipe(p) < 0) 
		exit(1); 
	
	if (pipe(q) < 0) 
		exit(1);

	/* continued */
	if ((pid = fork()) > 0) { 
		printf("Parent Process\n");
		write(p[1], msg1, MSGSIZE); 
		write(p[1], msg2, MSGSIZE);
		write(p[1], msg3, MSGSIZE);
		printf("Finished writing in Parent Process\n");
		// Adding this line will 
		// not hang the program 
		close(p[1]); 
		close(q[1]);
		
		// wait(NULL); 
		while ((nbytes = read(q[0], inbuf, MSGSIZE)) > 0) 
			printf("Message from child: % s\n", inbuf); 
		if (nbytes != 0) 
			exit(2); 
		 
		printf("Finished reading in Parent Process\n");
	} 

	else { 
		printf("Child Process\n");
		// Adding this line will 
		// not hang the program
		write(q[1], msg1, MSGSIZE); 
		write(q[1], msg2, MSGSIZE);
		write(q[1], msg3, MSGSIZE); 
		printf("Finished writing in Child Process\n");
		close(q[1]); 
		close(p[1]); 
		while ((nbytes = read(p[0], inbuf, MSGSIZE)) > 0) 
			printf("Message from parent:% s\n", inbuf); 
		if (nbytes != 0) 
			exit(2); 
		printf("Finished reading in Child Process\n");
		 
	} 
	return 0; 
} 
