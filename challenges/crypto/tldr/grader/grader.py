def grade(arg, key):
    if "THISISTHEFLAGNOSPACESBUTADDTHEFLAGBRACES".lower() in key.lower():
        return True, "Awesome, you read it!"
    else:
        return False, "NO PLEASE READ"
