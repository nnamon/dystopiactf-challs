def grade(arg, key):
    if "flag{3v3n_1f_5h3s_4l1v3_5h3s_d34d}".lower() == key.lower():
        return True, "It is open."
    else:
        return False, "..."
