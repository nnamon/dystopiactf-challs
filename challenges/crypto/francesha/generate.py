import itertools
import random

message = "veryundateable"
imessage = range(len(message))
ms = set()
count = 0
print "\documentclass[a4paper,12pt]{article}\n\\begin{document}\n\n"
print "flag\{" + "".join("x_{%d}" % i for i in imessage) + "\} \\\\"

for i in itertools.combinations(imessage, (len(message)-3)):
    if count % len(message) == 0:
        ms.add(i)
    count = count + 1
mr = []
for i in ms:
    r = list(i)
    random.shuffle(r)
    mr.append(r)

for i in mr:
    x = 0
    for j in i:
        x = x ^ j
    l = " \oplus ".join("x_{%d}" % z for z in i)
    print l + " = " + str(x) + "\\\\"

print "\n\n\end{document}"