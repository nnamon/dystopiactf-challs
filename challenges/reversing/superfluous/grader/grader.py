def grade(arg, key):
    if "flag{rottingTextIsEasyStuff}".lower() == key.lower():
        return True, "Nice one. You managed to ignore the crap."
    else:
        return False, "Nope. Perhaps you should try harder, this is really easy."
