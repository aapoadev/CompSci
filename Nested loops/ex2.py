flights = ['BO11', 'MM12', 'SU55']
airlines = ['MO11', 'UU22', 'KK88']

print('flights;', flights)
print('airlines:', airlines)

for a in airlines:
    print(f'{a}:', end=' ')
    for f in flights:
        if f.startswith(a):
            print(f, end=' ')
    print()