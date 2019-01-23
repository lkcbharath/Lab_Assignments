#include <stdio.h>

int main( void ) {
	char *argv[3] = {"Command-line", ".", NULL};

	int pid = fork();

	if ( pid == 0 ) {
		execvp( "ls", argv );
		printf("pid %d ppid %d ",getpid(),getppid());
	}
	// wait for child to finish
	wait( 2 );

	printf( "Finished executing the parent process\n"
	        " - the child won't get here\nyou will only see this once\n" );

	return 0;
}
