# password: WTF15th1s!

password = raw_input("Password: ")
phrase = "EpicPhrase"
checkc = [18, 36, 47, 82, 101, 28, 26, 80, 0, 68]

first = ""
second = ""

for i in range(len(phrase)):
    if (ord(password[i]) ^ ord(phrase[i])) != checkc[i]:
        print "Wrong."
        exit()

eflag = "18'VN9XC\x1e\x119'\x19GF+,C\x06F-)"
flag = ""
for i in range(len(eflag)):
    flag = flag + chr(ord(eflag[i]) ^ ord(password[i % len(password)]))

print flag
