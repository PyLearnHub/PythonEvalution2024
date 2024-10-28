def jug(x, y, target):
    if target == x:
        return True
    elif target == y:
        return True

    if x > y:
        x = target
    else:
        y = target

