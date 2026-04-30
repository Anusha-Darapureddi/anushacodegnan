# #user input
# #------
# # int datatype
# # an=int(input("enter the number:"))
# # print(type(an))

# #passing two values
# # a,b=map(int,input("enter two numbers").split())
# # print(a)
# # print(b)


# #string datatype
# # str=input("enter the word")
# # print(len(str))
# # print(type(str))


# #list data type
# # cv=list(map(int,input("enter the numbers").split()))
# # print(cv)


# #tuple data type
# # cv=tuple(map(int,input("enter the numbers").split()))
# # print(cv)

# #fstring
# # a=89
# # b=2
# # print("addition of a and b is",a+b)
# # print(f"addition of a and b is{a+b}")

# #eval
# #---------eval takes string and performs mathematical operations

# # a=eval(input("enter"))
# # print(type(a))

# # a=2
# # b=3
# # print(eval("a+b"))


# #statements are three types
# #condition
# #control
# #loops

# #condition
# #------------

# #if statement--->this is used to check condition is true or not
# # an=9
# # if(an==9):
# #     print(f"an is equal to 9")
    
# #else statement----->else is an fallback statement,incase if statement becomes false then it enter into else

# # an=9
# # if(an>9):
# #     print(f"an is greater than 9")
# # else:
# #     print(f"an is not greater than 9")


# # a,b=map(int,input("enter two numbers").split())
# # if(a>b):
# #     print(f"{a} is greater than {b}")
# # else:
# #     print(f"{b} is greater than {a}")

# # a,b=map(int,input("enter two numbers").split())
# # if(a==b):
# #     print("a is equal to b")
# # else:
# #     print("a is not equal to b")


# # age=int(input("enter your age"))
# # if(age>=18):
# #     print("you are eligible to vote")
# # else:
# #     print(f" you have to wait for {18-age} more years")
    
    
# # marks=int(input("enter marks"))
# # if(marks>=35):
# #     print("tou are pass")
# # else:
# #     print("you are fail")

# # num=int(input("enter a number"))
# # if(num%5==0):
# #     print(f"{num} is divisible by 5")
# # else:
# #     print(f"{num} is not divisible by 5")

# # leap=int(input("enter a year"))
# # if(leap%4==0 and leap%100!=0) or (leap%400==0):
# #     print(f"{leap} is a leap year")
# # else:
# #     print(f"{leap} is not a leap year")


# # num=int(input("enter a number"))
# # if(num>0):
# #     print(f"{num} is postive number")
# # else:
# #     print(f"{num} is negative number")

# # char=input("enter char")
# # vowels="aeiou"
# # if(char in vowels):
# #     print("vowels")
# # else:
# #     print("consonent")

# # num=int(input("enter a number"))
# # if(num%2==0):
# #     print("even")
# # else:
# #     print("odd")


# # num=int(input("enter a number"))
# # if(10<num<50):
# #     print("it is in range")
# # else:
# #     print("it is not in range")

num = list(map(eval,input("enter: ").split()))
print(num)