def grade(arg, key):
    if "flag{B4s1c_wytch3s_w3ar_th4t_sh33t_s0_1_d0nt_3ven_b0th3r}".lower() in key.lower():
        return True, "Awesome, you've stopped World Destruction!"
    else:
        return False, "The world is doomed. Because of you. Yep."
