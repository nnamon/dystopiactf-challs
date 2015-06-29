def grade(arg, key):
    if "flag{Willi_Ninja_is_DeepInVogue}".lower() == key.lower():
        return True, "Great, now idle on IRC for hints!"
    else:
        return False, "...what the foozle?"
