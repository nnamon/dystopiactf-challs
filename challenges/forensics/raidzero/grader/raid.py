#! /usr/bin/python

from itertools import izip_longest, izip, cycle
from sys import argv

DISKS = 16
KEY = 'CAFEBABE'

with open(argv[1], 'rb') as f:
    data = f.read()

data = [''.join(i) for i in izip_longest(*[iter(data)]*16, fillvalue="\x00")]

chunks = [i for i in izip(cycle(range(DISKS)), data)]

for i, (n, d) in enumerate(chunks):
    print '[+] Writing data chunk {} of {}'.format(i+1, len(chunks))
    with open('{0}.{1:0>3}'.format(argv[1], n+1), 'ab') as f:
        f.write(''.join(chr(ord(m)^ord(k)) for m, k in izip(d, cycle(KEY))))
