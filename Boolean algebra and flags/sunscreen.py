paistaako = input('paistaako aurinko Y/N ')
aika = int(input('paljon kello on '))

if paistaako == ('Y') and aika in range (10,16):
    print('ya better oil up')
else:
    print('selviit ilman täl kertaa')
