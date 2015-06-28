#!/usr/bin/python

import timeit
import time
import md5
import sys

FLAG = "flag{tw0_b4tt3r13s_4nd_4_bulb}"
PASSWORD = md5.md5("I don't know. That's a good question.").hexdigest()

def main():
    safeprint("But what's really in the briefcase?")
    safeprint("There are %d characters in the password." % len(PASSWORD))
    safeprint("What's the password to unlock it?")

    user_pass = raw_input()

    safeprint("\nTook %.4fs to validate." % timeit.timeit("validate('%s')" % user_pass, "from __main__ import validate", number=1))

def validate(user_pass):
    for i in range(len(user_pass)):
        if user_pass[i] != PASSWORD[i]:
            safeprint("Sorry your password is incorrect!")
            return
        time.sleep(5.0)
    if PASSWORD == user_pass:
        safeprint("Your password is correct!")
        safeprint("Here is your flag: %s" % FLAG)
    else:
        safeprint("Sorry your password is incorrect!")

def safeprint(data):
    sys.stdout.write(data + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
