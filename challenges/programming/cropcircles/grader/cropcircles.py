#! /usr/bin/python

from itertools import izip_longest
from sys import argv

with open(argv[1], 'rb') as f:
    data = f.read()

chunks = [''.join(i) for i in izip_longest(*[iter(data)]*8, fillvalue="\x00")]
no_chunks = len(chunks)

streams = ['', '', '', '', '']

for i, chunk in enumerate(chunks):
    print '[+] Computing chunk {} of {}'.format(i+1, no_chunks)
    streams[0] += chunk[2]
    streams[1] += (chunk[1] + chunk[3])
    streams[2] += (chunk[0] + chunk[4])
    streams[3] += (chunk[7] + chunk[5])
    streams[4] += chunk[6]

with open(argv[1] + '.enc', 'wb') as f:
    f.write(''.join(streams))
