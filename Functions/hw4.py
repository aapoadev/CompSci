a = [range (10)]
b = [range(5,15)]


def share(a, b):
    same_numbers = False
    if a in b:
     same_numbers = True
    return (same_numbers)

print(share(a, b))