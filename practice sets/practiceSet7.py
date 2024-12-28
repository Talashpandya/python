# n = int (input("enter the number : "))
# for i in range (1,11):
#     print (f"{i} x {n} : ",i*n)

# n = ['Gello','Hii','Byyy']
# for i in n:
#     if (i.startswith("H")):
#         print (i)

# n = int (input("enter the number : "))
# i=0
# while (i<11) :
#     print (f"{n}x{i}: ",(n*i))
#     i+=1

# # prime number code 
# n = int(input())
# for i in range (2,n):
#     if (n%i==0):
#         print ("not prime")
#         break
# else:   
#         print ("prime")    
        

# PPRINTING PATTERNS

# n = int(input()) 
# for i in range (1,n+1):
#         print (" "*(n-i),end="")
#         print ("*"*(2*i-1),end="")
#         print("")


n = int(input()) 
for i in range (1,n+1):
        for j in range (1,n+1):
                if (i==1 or j==1 or i==n or j==n):
                        print("*",end="")
                else:
                        print(" ", end="")
        print("")        






# n = int(input("Enter the size of the square: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or j == 1 or i == n or j == n:  # Logical OR
#             print("*", end="")
#         else:
#             print(" ", end="")  # Print spaces inside the square
#     print("")  # Move to the next line




        
