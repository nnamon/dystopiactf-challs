def grade(arg, key):
    if "flag{J0sephRemingt0nIsTheRea1Culprit}".lower() == key.lower():
        return True, "You're right!"
    else:
        return False, "Nope."
