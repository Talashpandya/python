import random
import string
def generate_password (length):
        if (length <1):
            print ("password length showld be greater than one")
            return
        all_caharactor = string.__all__
        password = ''.join(random.choice(all_caharactor) for _ in range(length))
        return password
            





length = int(input("which length of password do you want : "))
password  = generate_password(length)
print (f"{password}")