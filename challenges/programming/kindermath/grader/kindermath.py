#!/usr/bin/python
# socat -T 20 TCP-LISTEN:6000,fork EXEC:./kindermath.py

import random
import itertools
import sys
import math

FLAG = "flag{0n3_s0n6_Gl0ry_@_h15_f33t}"

def main():
    banner = """
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ___  ____   | || |     _____    | || | ____  _____  | || |  ________    | || |  _________   | || |  _______     | |
| | |_  ||_  _|  | || |    |_   _|   | || ||_   \|_   _| | || | |_   ___ `.  | || | |_   ___  |  | || | |_   __ \    | |
| |   | |_/ /    | || |      | |     | || |  |   \ | |   | || |   | |   `. \ | || |   | |_  \_|  | || |   | |__) |   | |
| |   |  __'.    | || |      | |     | || |  | |\ \| |   | || |   | |    | | | || |   |  _|  _   | || |   |  __ /    | |
| |  _| |  \ \_  | || |     _| |_    | || | _| |_\   |_  | || |  _| |___.' / | || |  _| |___/ |  | || |  _| |  \ \_  | |
| | |____||____| | || |    |_____|   | || ||_____|\____| | || | |________.'  | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 .----------------.  .----------------.  .----------------.  .----------------.                                         
| .--------------. || .--------------. || .--------------. || .--------------. |                                        
| | ____    ____ | || |      __      | || |  _________   | || |  ____  ____  | |                                        
| ||_   \  /   _|| || |     /  \     | || | |  _   _  |  | || | |_   ||   _| | |                                        
| |  |   \/   |  | || |    / /\ \    | || | |_/ | | \_|  | || |   | |__| |   | |                                        
| |  | |\  /| |  | || |   / ____ \   | || |     | |      | || |   |  __  |   | |                                        
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |    _| |_     | || |  _| |  | |_  | |                                        
| ||_____||_____|| || ||____|  |____|| || |   |_____|    | || | |____||____| | |                                        
| |              | || |              | || |              | || |              | |                                        
| '--------------' || '--------------' || '--------------' || '--------------' |                                        
 '----------------'  '----------------'  '----------------'  '----------------' 

 Welcome to KinderMath Grade 0! If you want your reward, please solve these very easy equations for me!
 You will need to solve about a hundred of them :)
 """
    write(banner)

    # Easiest stage
    test_them(10, 3, ["+"], 2)

    # Easy Stage
    test_them(10, 3, ["+"], 3)

    # Not So Easy Stage
    test_them(10, 10, ["+", "-"], 4)

    # Less Easy Stage
    test_them(10, 250, ["+", "-"], 4)

    # Medium Stage
    test_them(10, 250, ["+", "-", "*"], 4)

    # Mediumer Stage
    test_them(10, 1000, ["+", "-", "*", "%"], 6)

    # Hard Stage
    test_them(10, 10000, ["+", "-", "*", "%"], 8)

    # Harder Stage
    test_them(10, 10, ["+", "-", "*", "%"], 8)

    # Super Hard Haha
    test_them(10, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, ["+", "-"], 8)

    # Uber Hard
    test_them(10, 10000000000, ["+", "-", "*"], 200)

    write("CONGRATULATIONS, YOU CAN COUNT. YOUR FLAG: %s" % FLAG)

def quit_game():
    write("THAT WAS INCORRECT. YOU ARE A FAILURE. NO REWARDS FOR FAILURES")
    exit()

def test_them(numeq, maxint, ops, numargs):
    for i in range(numeq):
        eq = generate_equation(maxint, ops, numargs)
        write("%s = ?" % eq[0])
        write("Answer: ", newline="")
        resp = sys.stdin.readline().strip()
        try:
            resp = int(resp)
        except:
            quit_game()
        if resp == eq[1]:
            write("That is CORRECTOMUNDO!")
            continue
        else:
            quit_game()

def write(data, newline = "\n"):
    sys.stdout.write(data + newline)
    sys.stdout.flush()

def generate_equation(maxint, ops, numargs):
    n = []
    o = []    
    for i in range(numargs):
        n.append(str(random.randint(1, maxint)))
        o.append(random.choice(ops))
    e = list(itertools.chain.from_iterable(zip(n, o)))
    e.pop()
    eq = " ".join(e)
    ans = eval(eq)
    return (eq, ans)




if __name__ == "__main__":
    main()