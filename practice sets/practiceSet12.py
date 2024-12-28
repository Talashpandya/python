# try :
#     with open ("file.txt") as f :
#         print (f.read())
# except Exception as e :
#         print (e)
# try :
#     with open ("file2.txt","r") as f :
#         print (f.read())
# except Exception as e :
#     print (e)
# try :   
#     with open ("file3.txt") as f :
#         print (f.read())
# except Exception as e :
#     print (e)
# print ('hello program run correctly')    



# problem 2



# l = [1,2,3,4,5,6,7,8,9,0]
# for i,item in enumerate (l) :
#     if (i==4 or i==5 or i==7):
#         print (item-1)







# # problem 3 table 
# n = int(input("enter the number :"))
# table = [n*i for i in range(1,11) ]
# print (table)


# # problem 4
# try:
#     a = int (input ("1:"))
#     b = int (input ("2:"))
#     print (a/b)
# except ZeroDivisionError as v :
#     print ("infinite")



# # problem 5

# n = int(input("enter the number :"))
# table = [n*i for i in range(1,11) ]
# with open ("file1.txt","a") as f :
#     f.write (f"{str(table)} \n")
    
    
    