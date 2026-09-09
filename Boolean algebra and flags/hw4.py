a_and_b = [1,2]

n=0
laskettu=False

while laskettu == False:
    n +=1
    for i in a_and_b:
        if not n % i == 0:
            laskettu == False
            break
        else:
            laskettu == True

print(laskettu)
