#pattern programs

#triangle
# num=int(input("enter number"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

#triangle pattern using numbers
# num=int(input("enter number"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


#reverse triangle
# num=int(input("enter number"))
# for i in range(num,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

#reverse triangle using numbers
# num=int(input("enter number"))
# for i in range(num,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


#pyramid
# num=int(input("enter number"))
# for i in range(1,num+1):
#     for j in range(num-i-1,0,-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("* ",end="")
#     print()

#calculator


# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# choice=int(input("\n 1.add \n 2.sub \n 3.multiply \n 4.division \n 5.power"))
# if(choice==1):
#     print(num1+num2)
# elif(choice==2):
#     print(num1-num2)
# elif(choice==3):
#     print(num1*num2)
# elif(choice==4):
#     print(num1/num2)
# elif(choice==5):
#     print(num1**num2)
# else:
#     print("choose correct one")


# num=int(input("enter:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#        print(j*i,end="")
#     print()

# num=int(input("enter:"))
# count=0
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(count*num,end=" ")
#         count+=1
#     print()

num=int(input("enter:"))
for i in range(1,num+1):

    for j in range(1,i+1):
        if(i%j==0):
            print(j,end=" ")
    print()

