# import random
# def game ():
#     score = random.randint(1,300)
#     with open("c:/Users/talas/OneDrive/Desktop/python/practice sets/hiscore.txt", "r") as f :
#         hiscore = f.read()
#         if hiscore == "" :
#             hiscore=0
#         else :
#             hiscore = int(hiscore)
        
#     if score > hiscore :
#         with open("c:/Users/talas/OneDrive/Desktop/python/practice sets/hiscore.txt", "w") as f:
#             f.write(str(score))
#             print (hiscore)    
#     else : print ("nothing to change")    
        
# game ()        
        
        
        
    
        
        
        
#         if hiscore =="": hiscore = 0
#         else : 
#             if (score > int(hiscore)):
#                 with open("hiscore.txt","w") as f:
#                     f.write(score)  
# game()    












# def table (n):#table folder is created for its output
    
#     content =""
#     for i in range (1,11):
#         content += f"{n} x {i} = {n*i}\n"
                
#     with open(f"c:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/content_{n}.txt", "w") as f:
#         f.write(content)


# for i in range (2,21):
#     table (i) 










# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","r" )as f :
#     content = f.read()
#     newcontet = content.replace("donkey","####@###")
# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","w") as f :
#     f.write(newcontet)   








# words = ["donkey","ganda","bad"]
# with open("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","r") as f:
#     content = f.read()
    
# for i in words :
#     content = content.replace(i,"#"*len(i))
# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","w") as f :
#     f.write(content)       












# with open("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","r") as f :
#     content = f.read()
# if "python" in content : print ("python is present ")
# else : print("not present")


# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","r") as f :
#     line  = f.readlines()
    
# lineno = 1
# for i in line :
#     if "python" in i :
#         print(f"yes python is present {lineno}")
#         break
#     lineno +=1
    
# else : print ("python is not present")    












# # contnent copy
# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","r") as f :
#     content = f.read()
# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey_copy.txt","w") as f :
#     f.write (content)    




















# # contnent copy
# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey.txt","r") as f :
#     content1 = f.read()
# with open ("C:/Users/talas/OneDrive/Desktop/python/practice sets/fileFolderps9/donkey_copy.txt","r") as f :
#     content2 = f.read()    
    
# if content1 == content2 :print ("this files have same content")
# else : print ("different content")






















