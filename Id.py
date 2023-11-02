def ids():
    i = 0
    def ids_func():
        nonlocal i
        i += 1
        return i
    return ids_func

counts = ids()