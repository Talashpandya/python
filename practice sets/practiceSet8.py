# def sum (n):
    
#     if (n==1):
#         return 1
    
#     return n + sum (n-1)


# n = int(input())
# print (sum (n))


def patternprint (n) :
    if (n==0): return
    print ("*"*(n))
    patternprint(n-1)

patternprint (3)    