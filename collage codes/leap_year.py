
n = int (input ("enter your number : "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print (f"{n}  is a leap year")
    
else :
    print ("it is not a leap year")
    
