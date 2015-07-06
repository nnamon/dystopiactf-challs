def grade(arg, key):
    if "flag{B4by_c4n_y0u_s33_thr0ugh_th3_t34rs}".lower() in key.lower():
        return True, "Awesome, you've stopped World Destruction AGAIN!"
    else:
        return False, "The world is still doomed. Because of you. Yep."
