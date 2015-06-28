def grade(arg, key):
    if "flag{passion_patience_resonate}".lower() == key.lower():
        return True, "You're right!"
    else:
        return False, "Nope."
