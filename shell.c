#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char **argv)
{
	setuid(0);
	execlp( "sudo", "sudo", "sh", NULL );
	return 1;
}
