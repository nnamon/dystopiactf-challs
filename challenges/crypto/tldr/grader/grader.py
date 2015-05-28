def grade(arg, key):
    if "flag{THISISTHEFLAGNOSPACESBUTADDTHEFLAGBRACES}".lower() == key.lower():
        return True, "Awesome, you read it!"
    else:
        return False, "NO PLEASE READ"
