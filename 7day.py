# set
# -------
# set is a collection of unordered elements or unique elements.unlike list or tuple ,sets doesnt allow duplicate values
#set is mutable
# sn={1,2,4,3,3}
# print(sn)

# methods
# ----------
# add()
#this method is used to add new item in set
#syntax:variable_name.add(item)
# sn={1,2,7,4,3}
# sn.add(5)
# print(sn)


#remove()

#this method is used to delete an item in the set
#syntax==variable_name.remove(value)

# sn={3,4,42,32}
# sn.remove(32)
# print(sn)

#pop()
# -------this is also used to delete the element in the set,
# but we cannot specify the element(cannot give index value)
#syntax-->variable_name.pop(no arguments)
# sn={1,3,4,5,2}
# sn.pop()
# print(sn)


#clear()
#clear method is used to delete all the elements in the set
#syntax--variable_name.clear()
sn={1,3,4,3,2}
sn.clear()
print(sn)


#update()
#-----this method is used to add new item in set,
#but this method add more than one element
#syntax-->variable_name.update([elements])

# sn1={2,4,2,1}
# sn1.update([3,2,5])
# print(sn1)

#union()
#-------this method will return a set with all elements from both sets but it ignores the duplicates
#syntax-->variable_name1.union(variable_name2) or variable_name1 | variable_name_2

# sn1={2,3,4,5}
# sn2={5,3,6,7}
# print(sn1.union(sn2))
# print(sn1 | sn2)

#intersection()
#-----this method gives common elements from both the setss
#syntax--->variable_name.intersection(varibale_name2)  or  variable_name &variable_name2

# sn1={2,3,4,5}
# sn2={5,3,6,7}
# print(sn1.intersection(sn2))
# print(sn1 & sn2)


#difference()
#------this method is used to get the different elements from both sets
#syntax--->variabble_name.difference(variabble_name2) or variabble_name - variabble_name2
# sn1={2,3,4,2}
# sn2={4,2,2,1}
# print(sn1.difference(sn2))
# print(sn1-sn2)

#type convertions
#----
# converting one data type into another data type
#int----->string and float
a=8
b=str(a)
c=float(a)
print(type(b))
print(c)

#float---->int and string
c=34.53
d=int(c)
e=str(c)
print(d)
print(type(e))

#string--->int and float and list
c="67"
print(int(c))

d="67.8"
print(float(d))
print(list(d))

f="[1,4,5]"
print(list(f))

c="64"
i=tuple(c)
print(i)

#list to str
li=[1,2]
print(str(li))
print(type(li))

#list to tup
li2=[1,2]
u=(tuple(li2))
print(type(u))
