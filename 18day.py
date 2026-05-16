# #module
# #------A module is a file containing python code such as:
# #variable,functions,classes

# #modules helps us in:
# #reuse of code
# #reduce code reusability

# #types of modules
# #userdefined modules

# # import modules

# # print(modules.multiplication(6,7))
# # print(modules.div(4,2))
# # print(modules.power(2,3))
# # print(modules.add(3,4))
# # print(modules.sub(9,4))

# #built in modules
# #built in modules are os,math,sys
# #to use all this modules ,we have to import with module name

# #math module
# # import math
# # print(math.sqrt(25))
# # print(math.factorial(5))
# # print(math.pi)

# #sys module
# #-----------------
# #sys module is system specific parameter and functions.

# # import sys
# # print(sys.version)
# # print(sys.path)


# #ways to import modules
# #--------------------------
# #1.using alias name

# import modules1 as mod
# print(mod.greet())
# print(mod.greet2())


# #2.import entire module
# #3.import all functions
# # from math import *
# # print(sqrt(81))
# # print(pow(4,2))

# #4import specific function
# # from math import sqrt
# # print(sqrt(25))


# # import random
# # otp=random.randint(1000,9999)
# # print(otp)
# # num=int(input("enter:"))
# # count=0
# # for i in range(1,num+1):
# #     for j in range(1,num+1):
# #         print(count*num,end=" ")
# #         count+=1
# #     print()

def fibonacci(num):
    n1=0
    n2=1
  
    for i in range(0,num+1):
        sum=n1+n2
        print(n1,end=" ")
        n2=sum
        n1=n2
num=int(input("enter"))
fibonacci(num)
