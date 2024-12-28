from random import randint
n=randint(1,100)
noofguess =0
a=-1
while (a!=n):
    a = int(input("enter your guessed number "))
    if (a > n):
        print ("think lower one")
        noofguess +=1
    elif (a<n):
        print ("think the higher one ")
        noofguess+=1
print (f"you have guessed the correct number {n} in {noofguess} guesses")        