# class Employee:
#     a = 1
    
#     @classmethod
#     def show(clss):
#         print(f"The class attribute of a is {clss.a}")

#     @property 
#     def name(self):
#         return f"{self.fname}{self.lname}"
    
#     @name.setter
#     def name (self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.a = 45

# e.name = "Harry Khan"
# print(e.fname, e.lname)

# e.show()










# class Person:
#     def __init__(self, age):
#         self._age = age  # Use an internal attribute

#     @property  # Getter
#     def age(self):
#         print("Getter called")
#         return self._age

#     @age.setter  # Setter
#     def age(self, value):
#         print("Setter called")
#         if value >= 0:
#             self._age = value
#         else:
#             print("Age cannot be negative!")

# person = Person(30)

# # Call Getter
# # print(person.age)  # Output: Getter called \n 30

# # # Call Setter
# # person.age = 35  # Output: Setter called






# # checking 
# class Counter:
#     count = 0  # Class attribute

#     def increment(self):
#         Counter.count += 1  # Access and modify the class attribute directly
#         print(f"Count is now {Counter.count}")

# # Create an instance of Counter
# counter_instance = Counter()
# counter_instance.increment()  # Output: Count is now 1
# counter_instance.increment() 
# counter_instance.increment() 
# Counter.count = 7
# # Create another instance
# another_instance = Counter()
# another_instance.increment()  # Output: Count is now 2

# # Access the class attribute directly
# print(f"Final count: {Counter.count}")  # Output: Final count: 2



















# # problem 1

# class twodvector :
#     def __init__(self,i,j):
#         self.i = i 
#         self.j = j
#     def show (self):
#         print (f"the 2d vector {self.i} + {self.j}")
# class threedvector (twodvector):
#     def __init__(self, i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         print (f"       the threedvector is {self.i}+{self.j}+{self.k}")
# vec1 = twodvector(1,2)
# vec2 = threedvector(2,5,6)
# vec1.show ()
# vec2.show ()








# # problem 3
# class employee :
#     salary  = 200
#     _increment = 20
#     def salaryafterincrement(self):
#         return self.salary + (self.salary*self.increment/100)
#     @property    
#     def increment (self):
#         return self._increment
#     @increment.setter
#     def increment (self,newsalary):
#         self._increment  = ((newsalary/self.salary)-1)*100

    

# e1 = employee()
# print (e1.salaryafterincrement())
# e1._increment =300 
# print (f"{e1.increment}")





# class complex :
    
#     def __init__(self,r,i):
#         self.r = r 
#         self.i = i
#     def __add__ (c1,c2):
#         return complex(c1.r + c2.r,c1.i+c2.i)
#     def __mul__(c1,c2):
#         real = (c1.r*c2.r)- (c1.i*c2.i)
#         imaginary = (c1.r*c2.i)+(c1.i*c2.r)
#         return complex (real,imaginary)
#     def __str__(self):
#         return f"{self.r} + {self.i}"
# c1 = complex(1,2)
# c2 = complex(3,4)
# c3 = c1+c2
# print (c3)
# c4 = c1*c2
# print (c4)




