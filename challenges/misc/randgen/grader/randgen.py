#!/usr/bin/python

# socat -T 20 TCP-LISTEN:6001,fork EXEC:./randgen.py,pty,ctty,echo=0

import random
import sys
import time

FLAG = "flag{Ju5t_l1k3_4_J0y_4ft3r_He4r1ng_4_Ch1lds_L4ught3r}"
# Define our own random list because sometimes we want things a little less random
RAND_LIST = [11, 35, 61, 50, 23, 63, 12, 49, 89, 49, 
    71, 73, 96, 42, 40, 25, 88, 2, 47, 72, 3, 6, 73, 
    46, 23, 57, 78, 92, 26, 33, 14, 51, 30, 13, 79, 
    92, 57, 30, 1, 83, 48, 8, 57, 76, 27, 35, 26, 48, 71, 80]

def get_random_numbers(howmany):
    which = random.randint(0, len(RAND_LIST)-1)
    res = []
    for i in range(howmany):
        res.append(RAND_LIST[(which+i) % len(RAND_LIST)])
    return res

def main():
    waiting = random.randint(8, 12)
    nums = get_random_numbers(waiting)
    write("[      WELCOME TO THE BAD GAMBLING SERVICE!     ]")
    write("--> WHERE YOU ARE ASSURED TO LOSE YOUR MONEY! <--")
    write("SIMPLY GUESS THE RIGHT NUMBER BETWEEN 1 and 100 TO WIN!\n")
    write("You are currently: Position %d on the waiting list!" % waiting)
    write("You can watch while others play first though!\n")
    time.sleep(0.5)
    for i in range(waiting-1):
        guess = random.randint(1, 100)
        write("%d. Anonymous Player No. %d guesses %d!" % (i+1, random.randint(0, 9999), guess))
        time.sleep(0.5)
        if guess == nums[i]:
            write("The correct number was %d so %se was correct and wins!\n" % (nums[i], random.choice(["h", "sh"])))
        else:
            write("The correct number was %d so %se was wrong and loses! No money, No game!\n" % (nums[i], random.choice(["h", "sh"])))
    write("It is now your turn! What number would you like to guess?")
    player_guess = sys.stdin.readline()
    try:
        player_guess = int(player_guess)
    except:
        write("Sorry, that is invalid.")
        exit()
    if player_guess == nums[waiting-1]:
        write("Correct! Here is your flag: %s!" % FLAG)
    else:
        write("Wrong! Get out of here!")

def write(data, newline = "\n"):
    sys.stdout.write(data + newline)
    sys.stdout.flush()

if __name__ == "__main__":
    main()


