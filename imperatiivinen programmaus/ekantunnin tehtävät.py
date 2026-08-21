a=3
b=2
print(a,b)
print (a-b)
print(a/b)
print((3*a)%(2*b))
c=sum(range (6,17))
print(c)

#joku flowchart
mark = int(input('anna pisteet '))
if mark >= 90:
    grade = 10
elif mark >= 70:
    grade = 9
else:
    grade = 8
print('numero on', grade)
#factorial
n = int(input('anna posi kokonaisnumero--> '))
if n > 0:
    p = 1
    while n > 1:
        p *= n #p = p*n
        n -=1 #n = n -1
    print (f'{n}!={p}')
else:
    print('ERROR!!!!!!!!!!!')

# joku tämmöne

v = 9
while v <= 65 :
    print(v, end = ' ')
    v += 4
print()

k = 3
for x in range (13):
    print(k, end = ' ')
    k *= 2
print()

for y in range (1,41):
    m = y
    if y % 4 == 0:
        m= -1
    print(m, end = ' ')
print()

#smallest largest
smallest = 0
largest = 0
for n in range (51):
    value = n*(n-30)*(n-50)
    if value < smallest:
        smallest = value
    if value > largest:
        largest = value
    print(smallest,largest)

#blackjack
import random

first_card = random.randint(1, 10)
second_card = random.randint(1,10)
third_card = random.randint(1,110)
x = (first_card + second_card)
if (x) < 17:
    print(f' dealer sai {first_card+second_card+third_card}')
elif 16<x<22:
    print (f'dealer sai {x}') 
else:
    print('dealer bustas')

#homework 6
w = int(input(' mikä on w goy '))

if w <= 2:
    p = 3
elif w == 3:
    p = 5
elif w == 4:
    p = 7
elif w == 5:
    p = 8
elif w > 5:
    p = 8 + (w-5)*2
print (p)

# hw 8

a = int(input('anna ei nega kokonaisnro '))
vastaus = 1
for b in range (a):
    vastaus *= 3
print(vastaus)

b = int(input('anna b'))
a = int(input ('anna a ei neg'))

vastaus = 1
for q in range (a):
    vastaus *= b
print(vastaus)