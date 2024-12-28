a1 = int(input (':'))
a2 = int(input (':'))
a3 = int(input (':'))
a4 = int(input (':'))
if (a1>a2 & a1>a3 & a1>a4):
    print(a1)
elif (a2>a1 & a2>a3 & a2>a4):
    print(a2)
elif (a3>a2 & a3>a1 & a3>a4):
    print(a3)
else :
    print(a4)