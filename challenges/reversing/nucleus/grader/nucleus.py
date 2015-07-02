from binascii import hexlify
from collections import Counter
from heapq import heappush, heappop, heapify
from sys import argv, exit, stdin, stdout

expanded = ''

def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def print_banner():
    write('''
 _|      _|  _|    _|    _|_|_|  _|        _|_|_|_|  _|    _|    _|_|_|
 _|_|    _|  _|    _|  _|        _|        _|        _|    _|  _|
 _|  _|  _|  _|    _|  _|        _|        _|_|_|    _|    _|    _|_|
 _|    _|_|  _|    _|  _|        _|        _|        _|    _|        _|
 _|      _|    _|_|      _|_|_|  _|_|_|_|  _|_|_|_|    _|_|    _|_|_|

***********************************************************************
* Welcome to Nucleus! The best file compression service in the world! *
***********************************************************************

NOTE: (TRIAL VERSION) MAX SIZE 50KB. INPUT STOPS ON EOF.

''')

def write(data):
    stdout.write(data)
    stdout.flush()

print_banner()

data = stdin.read(50002)

if len(data) > 50000:
    write('[-] ERROR: TRIAL VERSION ONLY ALLOWS FILES UP TO 50KB')
    exit(0)

data = hexlify(data)
huffman = {i[0]:i[1] for i in encode(Counter(data))}

for i in data:
    expanded += huffman[i]

write(expanded)
