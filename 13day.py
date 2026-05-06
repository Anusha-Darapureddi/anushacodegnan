# function
#----------- this is a block of code that can be reusable 
#function can only run when it is called
#def is a keyword used to define the function 
#def function_name(parameters):
#     -------
#     -------
#     -------
#function_name(arguments)


# def even_odd(num):
#     if(num%2==0):
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")
# even_odd(5)


#required arguments
#---------- a function must called with correct number of arguments that means function expects two arguments,we have to call function with 2 arguments not less or not more

# def even_odd(n1,n2):
#     print(n1+n2)
# even_odd(2,3)


#there will be error because more arguments
# def even_odd(n1,n2):
#     print(n1+n2)
# even_odd(2,3,6)



#default arguments
#-------------------

#--by default value is taken from calling function
# def age(age="21"):
#     print(f"your age is{age}:")
# age(22)
# age()


# num=9
# def even_odd(num_2):
#     print(num_2)
# even_odd(num)


#keyword arguments
#----------
#here we can send arguments with key=value syntax.by this the order of arguments does not matter

# def even_odd(n1,n2,n3):
#     print(n1+n2+n3)
# even_odd(n2=9,n1=3,n3=4)

#variable length argument
#------>adding a star(*) before the parameters name in the function ,recieve a tuple of arguments and can be access items with indexes

# def greet(*name):
#     print(name[1])
# greet("anu","sujji","prassu")