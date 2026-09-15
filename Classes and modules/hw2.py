
def date_of_birth(ssn):
    day = int(ssn[:2])
    month=int(ssn[2:4])
    year = ssn[4:6]
    century = (ssn[6])
    if century == '+':
        year == ('18'+year)
    elif century == '-':
        year == ('19'+year)
    else: year == ('20'+year)
    print(year, month, day)
    return (day, month, year)
    print(year, month, day)
date_of_birth('140598+abcd')
