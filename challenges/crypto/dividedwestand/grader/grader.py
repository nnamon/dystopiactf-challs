def grade(arg, key):
    if "flag{th3_C4l4b1_y4u_m0d3l}".lower() in key.lower():
        return True, "Great, you can GCD!"
    else:
        return False, "no."
