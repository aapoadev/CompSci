def abs_value(x):
    if x < 0:
        return -x
    else:
        return x

for x in [-5.6, 2, -6, 0,3]:
    print(x, abs_value(x))
abs_value(x)