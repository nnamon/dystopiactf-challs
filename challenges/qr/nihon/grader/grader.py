def grade(arg, key):
    if "flag{QR_c0des_are_fixable}".lower() in key.lower():
        return True, "Bet you didn't know that!"
    else:
        return False, "no."
