def grade(arg, key):
    if "flag{Y0ur_m0th3r_w4s_4_t3rr1bly_4ttr4ct1v3_w0m4n}".lower() in key.lower():
        return True, "Uh... I don't have over 9000 million dollars but you can have mad credz instead!"
    else:
        return False, "You are boring."
