#!/usr/bin/python

import random
import sys

FLAG = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    suitable_primes = get_all_primes_between(20, 1500000)

    prime_main = random.choice(suitable_primes)
    prime_jack = random.choice(suitable_primes)
    prime_jill = random.choice(suitable_primes)
    prime_you  = random.choice(suitable_primes)

    password_jack = prime_main * prime_jack
    password_jill = prime_main * prime_jill
    password_you  = prime_main * prime_you

    write("Welcome to the Beanstalk Flag Retrieval System.\n")
    write("In this system, we generate a really large prime that will serve as the master prime.")
    write("I will generate more primes to create your unique passwords.")
    write("We are so confident you cannot break this crypto, that we will give you the password of Jack and Jill!\n")
    write("Here are your passwords:")
    write("Jack: %d" % password_jack)
    write("Jill: %d" % password_jill)
    write("Yours: UNKNOWN ERROR OCCURED (MASTER PRIME: XXX, YOUR PRIME: %d)\n" % prime_you)
    write("Please enter your password to retrieve your flag: ", newline="")

    password_given = sys.stdin.readline().strip()
    try:
        password_given = int(password_given)
    except:
        write("Not a number. Sorry.")
        exit()
    if password_given == password_jack:
        write("You are not Jack.")
    elif password_given == password_jill:
        write("Jill doesn't actually exist.")
    elif password_given == password_you:
        write("Here is your flag: %s" % FLAG)
    else:
        write("You are not allowed here.")

### You don't really need to understand the below ###

def get_all_primes_between(start, end):
    primes = []
    for i in gen_primes():
        if i > end:
            break
        if i >= start:
            primes.append(i)
    return primes


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def write(data, newline = "\n"):
    sys.stdout.write(data + newline)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
