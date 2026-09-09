def interleave(a, b):
    return zip(a, b)
    for (x,y) in zip(a, b):
        flattened.append(x)
        flattened.append(y)
    return flattened


print(list(interleave([1, 2, 3], [4,5,6])))