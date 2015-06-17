#!/usr/bin/python

import timeit
import time

FLAG = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PASSWORD = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    print("So you've finally gotten your hands on this briefcase, have you?")
    print("There are %d characters in the password." % len(PASSWORD))
    print("What's the password to unlock it?")

    global user_pass
    user_pass = raw_input()

    print("\nTook %.4fs to validate." % timeit.timeit("validate()", "from __main__ import validate", number=1))

def validate():
    global user_pass
    for i in range(len(user_pass)):
        if user_pass[i] != PASSWORD[i]:
            print("Sorry your password is incorrect!")
            return
        time.sleep(0.05)
    if PASSWORD == user_pass:
        print("Your password is correct!")
        print("Here is your flag: %s" % FLAG)
    else:
        print("Sorry your password is incorrect!")

if __name__ == "__main__":
    main()
