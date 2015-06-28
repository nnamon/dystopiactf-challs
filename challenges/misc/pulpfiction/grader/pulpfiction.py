#!/usr/bin/python

import timeit
import time
import sys

FLAG = "flag{3v3n_1f_5h3s_4l1v3_5h3s_d34d}"
PASSWORD = "I_didn't_say_it_went_perfectly_at_all"

def main():
    safeprint("So you've finally gotten your hands on this briefcase, have you?")
    safeprint("There are %d characters in the password." % len(PASSWORD))
    safeprint("What's the password to unlock it?")

    global user_pass
    user_pass = raw_input()

    safeprint("\nTook %.4fs to validate." % timeit.timeit("validate()", "from __main__ import validate", number=1))

def validate():
    global user_pass
    for i in range(len(user_pass)):
        if user_pass[i] != PASSWORD[i]:
            safeprint("Sorry your password is incorrect!")
            return
        time.sleep(0.05)
    if PASSWORD == user_pass:
        safeprint("Your password is correct!")
        safeprint("Here is your flag: %s" % FLAG)
    else:
        safeprint("Sorry your password is incorrect!")

def safeprint(data):
    sys.stdout.write(data+"\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
