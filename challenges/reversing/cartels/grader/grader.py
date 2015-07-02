def grade(arg, key):
    if "flag{M0rm0ns_vs_Drugz}".lower() == key.lower():
        return True, "Congratulations. I'm going to go hide now."
    else:
        return False, "Shhh... that was wrong."
