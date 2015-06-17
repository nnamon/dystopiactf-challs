#!/usr/bin/python

import timeit
import time
import md5

FLAG = "xxxxxxxxxxxxxxxxxxxxxxxx"
PASSWORD = md5.md5("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").hexdigest()

def main():
    print("But what's really in the briefcase?")
    print("There are %d characters in the password." % len(PASSWORD))
    print("What's the password to unlock it?")

    user_pass = raw_input()

    print("\nTook %.4fs to validate." % timeit.timeit("validate('%s')" % user_pass, "from __main__ import validate", number=1))

def validate(user_pass):
    for i in range(len(user_pass)):
        if user_pass[i] != PASSWORD[i]:
            print("Sorry your password is incorrect!")
            return
        time.sleep(5.0)
    if PASSWORD == user_pass:
        print("Your password is correct!")
        print("Here is your flag: %s" % FLAG)
    else:
        print("Sorry your password is incorrect!")

if __name__ == "__main__":
    main()
