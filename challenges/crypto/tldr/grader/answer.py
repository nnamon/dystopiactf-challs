def get_indexes(line, d):
    res = []
    for i in range(len(line)):
        if line[i] == d:
            res.append(i)

a=file("./tldr.txt").readlines()
b = []
for i in range(0, len(a)-1):
    b += [a[i+1][j] for j in get_indexes(a[i], ".")]
print "".join(b)
