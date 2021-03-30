// getenv.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
seed@ubuntu:~$ export MYSHELL=/bin/sh
seed@ubuntu:~$ gcc -o getenv getenv.c 
seed@ubuntu:~$ ./getenv MYSHELL ./vuln
MYSHELL will be at 0xbffffe8a*/

int main(int argc, char const *argv[])
{
    char *ptr;
    if(argc < 3)
    {
        printf("Usage: %s <environment var> <target program name>\n", argv[0]);
        exit(0);
    }
    ptr = getenv(argv[1]);
    ptr += (strlen(argv[0]) - strlen(argv[2])) * 2;
    printf("%s will be at %p\n", argv[1], ptr);
    return 0;
}