lst = list(range(10))
print(lst)

lst2 = []
for x in range(10):
    lst2.append(x**2)
print(lst2)

lst3 = [f'val {x}' for x in range(10) if x % 3 ==0]
print(lst3)