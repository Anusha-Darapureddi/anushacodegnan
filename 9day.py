#elif statement
#this statement gives more options to get the result of that program
# marks=int(input("enter your marks"))
# if marks>=90:
#     print("A+")
# elif marks>=80:
#     print("A")
# elif marks>=70:
#     print("B+")
# elif marks>=60:
#     print("B") 
# elif marks>=50:
#     print("C+")
# else:
#     print("failed")
    

#nested if statement
#----->if statement in side another if statement is called nested if  statement

# pin={"atm pin":"7125"}
# user_pin=(input("enter four digit pin"))
# if len(user_pin)==4:
#     if (user_pin in pin["atm pin"]):
#         print("welcome to sbi bank")
#     else:
#         print("please enter correct pin")
# else:
#     print("please enter four digit pin")
    
#for loop
# a for statement is used to iterate over items like(string,list,tuple )with fixed number of iterations

# any=[2,4,3]
# for j in any: 
#     print(j)

# else statement in for
#--------
# after completing all iterations this else staement will execute

# any=[2,4,3]
# for j in any: 
#     print(j)
# else:
#     print("loop finished")


# so="hello"
# empty=""
# for j in so:
#     empty=j+empty
# if(empty==so):
#     print("palidrome")
# else:
#     print("not a palindrome")


# num=int(input("enter a number"))
# if(num%3==0 and num%5==0):
#     print("fizz buzz")
# elif(num %3==0):
#     print("fizz")
# elif(num%5==0):
#     print("buzz")

# else:
#     print(f"{num}")

# a=input("enter char")
# if(a.isupper()):
#     print("upper")
# elif(a.islower()):
#     print("lower")
# elif(a.isdigit()):
#     print("digit")
# else:
#     print("special character")

# a={"username":"admin",
#    "password":"1234"
#    }
# username=input("enter username:")
# password=input("enter password:")
# if username in a["username"] and password in a["password"]:
#     print("you are in")
# else:
#     print("invalid login")

# username=input("enter username")
# password=int(input("enter password"))
# if(username=="admin" and password==1234):
#     print("you are in")
# else:
#     print("invalid login")

# electricity_=int(input("enter elecrticity:"))
# if(electricity_<=100):
#     print(f"{electricity_*5}")
# elif(101<=electricity_<=200):
#     print(f"{electricity_*7}")
# elif(electricity_>200):
#     print(f"{electricity_*10}")
# else:
#     print("please enter valid units")

salary_=int(input("enter your salary"))
if(salary_<=20000):
    print(f" you salary is:{((salary_*10)/100)+salary_}")
elif(20000<salary_<=50000):
    print(f"you salary is:{(salary_*7/100)+salary_}")
elif(salary_>50000):
    print(f"your salary is {(salary_*5/100)+salary_}")
else:
    print("please enter valid amount")