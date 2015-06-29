def grade(arg, key):
    if "flag{Y0u_4r3_RNG_G0d}".lower() == key.lower():
        return True, "What a really lame lottery."
    else:
        return False, "..."
