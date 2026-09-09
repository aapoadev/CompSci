
while not ( 1 <=(day:= int(input(' please give day of week (1-7): ')) <= 7):
    print('please provide a valid day of week')

while (vacation := input('is James on vacation (yes/no):')):
    pass    

print(vacation == 'yes' or day > 5)