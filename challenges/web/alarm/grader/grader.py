def grade(arg, key):
    if "flag{P1lgr1m_h4nDs_D0_t0uch}".lower() == key.lower():
        return True, "The alarm was raised"
    else:
        return False, "..."
