import random
userInput  = input ()
compvalue = random.choice([1,0,-1])
dictonary = {"s":1, "w": -1, "g":0}


if (userInput=="s" or userInput=="w" or userInput == "g"):
    uservalue = dictonary[userInput]
    
    if uservalue == compvalue : print ("draw")
    else:
        if uservalue ==1 and compvalue == -1  : print ("you win ")
        elif uservalue == 1 and compvalue == 0 : print ("comp wins")
        elif uservalue == -1 and compvalue == 0 : print("you wins")
        elif uservalue == -1 and compvalue == 1 : print ("comp wins")
        elif uservalue == 0 and compvalue == 1 : print (" you win ")
        else: print("comp wins")
else : print ("invalid input from user")