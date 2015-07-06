import random
import itertools
import sys
import socket
import libnum

LAUNCH_CODE = file("flag.txt").read()

if not 100 < len(LAUNCH_CODE) < 256:
    print("Sorry your message is bad.")
    exit(0)

def generate_random_prime(n):
    def isProbablePrime(n, t = 7):
        def isComposite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True

        assert n > 0
        if n < 3:
            return [False, False, True][n]
        elif not n & 1:
            return False
        else:
            s, d = 0, n - 1
            while not d & 1:
                s += 1
                d >>= 1
        for _ in itertools.repeat(None, t):
            if isComposite(random.randrange(2, n)):
                return False
        return True

    p = random.getrandbits(n)
    while not isProbablePrime(p):
        p = random.getrandbits(n)
    return p

def encrypt(message, key):
    m = int(message.encode("hex"), 16)
    n = key[0]*key[1]
    print "m:",m
    c = pow(m, 3, n)
    return c

def decrypt(ciph, key):
    n = key[0] * key[1]
    tn = (key[0]-1)*(key[1]-1)
    print "key1:", key[0]
    print "key2:", key[1]
    print "tn:", tn
    d = libnum.invmod(3, tn)
    m = pow(ciph, d, n)
    print "m:", m
    return m

def check_valid(key):
    n = key[0] * key[1]
    tn = (key[0]-1)*(key[1]-1)
    return True
    if libnum.gcd(3, tn) == 1:
        return True
    else:
        return False

def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])

    while True:
        print("Generating the primes and the keys and the public modulus")
        key = (generate_random_prime(1024), generate_random_prime(1024))
        if check_valid(key):
            mod = key[0]*key[1]
            break
    

    print("Encrypting the launch code for more securitays")
    cip = encrypt(LAUNCH_CODE, key)
    ciphertxt = hex(cip)[2:-1] + ":" + hex(mod)[2:-1]
    decrypt(cip, key)

    print("Sending encrypted launch code")
    s = socket.socket()
    s.connect((ip, port))
    s.sendall(ciphertxt)
    s.close()


if __name__ == "__main__":
    main()
