

# transiction=[]
# append(deposit,withdraw)

#list comprehension
#--------------------
#----> this list comprehension offers shorter syntax when we want to create a new list based on values of old list of an existing list.
#syntax=[expression loop condition]

# old_li=[1,4,3,2]
# new_li=[i for i in old_li]
# print(new_li)

# old_li=[1,4,2,5]
# new_li=[i for i in old_li if i%2==0]
# print(new_li)

# old_li=[2,4,3,5]
# new_li=[i if i%2==0 else "odd" for i in old_li]
# print(new_li)

# old_li=[2,4,3,5]
# new_li=[i if i%2!=0 else "even" for i in old_li]
# print(new_li)


#dictionary comprehension
# dictionary comprehension offers shorter syntax when we want to create a new dict based on the values of an exisiting dict


a={"name":"anusha","age":21,"degree":"btech"}
result={x:y for (x,y) in a.items()}
print(result)

b={"a":2,"b":4,"c":5}
result={x:y for (x,y) in b.items() if(y%2==0)}
print(result) 