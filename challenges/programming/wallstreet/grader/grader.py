def grade(arg, key):
    if "flag{w3ird_g1fs_lol}".lower() == key.lower():
        return True, "Wow, that was a lot of QR codes wasn't it!"
    else:
        return False, "Non!"
