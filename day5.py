
#list data type

#List is a collection of different datatypes and it is represented by[],separated by commas

#mutable
li=[1,2,3]
li.append(6)
print(li)

#immutable
str="python is a language"
print(str.replace("python","java"))
print(str)


any=[1,"python",[2,"this is 5th class",3],56]
print(any)
print(type(any))


print(any[2])
print(any[2][1])
print(any[2][1][10])


any2=[1,"python is a language",7,68,[34,["this is python class"],78,"i'm looking for good bat"],[2,"this is 5th class",3],56]
print(any2[4])
print(any2[4][1])
print(any2[4][1][0][14])

#methods

#1.append()

#this method is used to add new item into list but it will add in the last index position
#syntax---->variable_name.append(item)

li=[1,2,3]
li.append(6)
print(li)
li.append([4,5])
print(li)


#2.extend()

#-->this method is also used to add new item into list ,but this extend add as each position to each index in the list.extend only takes iterables
#syntax-->variable_name.extend(item(iterables))

li=[1,2,3]
li.extend("python")
li.extend([4,5])
print(li)

#3.pop()

#-->this is used to delete an item from the list.pop() removes the value based on index position mentioned in the parameters.
#-->if nothing is mentioned in the parameters ,it will remove last index position value.
#syntax-->variable_name.pop(index_position)

any=[1,4,5,2,6]
any.pop(3)
print(any)

#4.remove()
#-->this is also used to deleter item from the list,but remove()method will delete direct value.
#syntax-->variable_name.remove(value)

any=[4,5,2,6]
any.remove(5)
print(any)

#5.index()

#6.insert()
#7.count()


#slicing

#-->this is used to useto get the particular part of the list,string or tuple
#-->this works based on index position
#syntax-->varible_name[starting_index:ending index]

any=[1,2,3,4,5,6]
print(any[2:5])

len()

#-->len()method is used to find the number of items present in the list
#syntax-->len(variable_name)

any=[1,2,3,4,5,6]
str="python is a language"
print(len(any))
print(len(str))

