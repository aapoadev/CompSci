year = int(input('please give year to check: '))

leap = False

if year % 4 == 0: 
    leap = True
if leap:
    print(' on leappi')
else:
    print('ei oo')