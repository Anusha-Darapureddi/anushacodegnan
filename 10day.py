#while statement
#-----------
#this while statement will keep on executing until unless condtion becomes true
# v=1
# while v<=5:
#     print(v)
#     v+=1


# range()
#-------------- this range() will generate sequence numbers upto limit
#syntax--->range(starting,ending,step(optional))

# num=int(input("enter the limit"))
# for i in range(0,num):
#     print(i)

#step
# num=int(input("enter a number"))
# for j in range(1,20,2):
#     print(j)

# for i in range(2,101):
#     if(i%2==0):
#         print(f"{i} is even number")
#     else:
#         print(f"{i} is odd number")


#break
#------>this break statement will exit if the condition becomes true.and never enters the next loops

# li=[32,34,22,35,67]
# for i in li:
#     if(i==22):
#         print("i found")
#         break
#     print(i)
    
#continue
#------>this statement will skip that particular iteration and goes to next
# li=[32,43,2,13]
# for i in li:
#     if(i==2):
#         continue
#     print(i)

#pass
#------->pass is a space holder ,holds the space not to get any error
# for i in range(1,10):
#     pass

# num=int(input("enter a number"))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count+=1
# if(count==2):
#     print("prime")
# else:
#     print("not a prime")
    

#nested loop
#------>a loop inside the loop is called nested loop
for i in range(2,100):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
           
    if(count==2):
        print(f"{j} is prime")
    else:
        print(f"{j}not a prime ")
        