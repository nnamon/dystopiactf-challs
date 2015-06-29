from sys import argv

with open(argv[1], 'r') as f:
    data = f.read()

data = [''.join(x) for x in map(None, *([iter(data * 8)] * 4))]

a, b, magic = data, data, 1

for i, x in enumerate(a[::~magic+magic][::magic+magic]):
    if (int(str(bin(i))[~magic+magic]) ^ magic):
        b[i] = ''.join([j.encode('hex') for j in x[::-magic]])
    else:
        a[i] = ''.join([j.encode('hex') for j in x])

c = list()

for i in range(len(a)/2):
    c.append(b[i] if i % 4 else a[i])

with open(argv[1]+'.crypt', 'wb') as f:
    f.write(''.join(c))
