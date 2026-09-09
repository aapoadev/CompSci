def fun(x):
    flag = True
    i = 2
    while flag and i < len(x):
        if x[i] - x[x-1] != x[i-1] - x[i-2]:
            flag = False
        else:
            i += 1
    return flag