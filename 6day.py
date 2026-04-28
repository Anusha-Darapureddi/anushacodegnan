#tuples
#-->tuple is a collection of different datatypes that are represented by () and the items in the tuple is separated by comma .
#tuple is immutable


# so=(1,"python",[7,8],(5,0))
# print(so)
# print(so[1])

# tup1=(1,3,5)
# tup2=(6,7,8)
# tup=tup1+tup2
# print(tup)


#Dictionaries
#dict is a collection of key :value pair ,where keys are immutable such as (string,integer,tuple) and values are any data type .
#this is represented by {}

#methods
#-------

# keys()
# -----> this method is used to access the only keys in the dictionary 
# syntax-->dict.keys()

# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# print(dict.keys())

# values()
#-->this is used to access only values in the dictionary 
#syntax-->dict.values()

# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# print(dict.values())


# items()
# ----> this method is used to access key value pair in the dictionary
# syntax-->dict.items()

# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# print(dict.items())
# print("anusha" in dict["name"])


#clear()
# ---->this clear method is used to delete all the items in the dict
# syntax-->dict.clear()

# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# (dict.clear())
# print(dict)


#update 
# -->this method is used to add new item (key:value) into the dictionary
# syntax-->dict.update({key:value})



# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# dict.update({"role":"python developer"})
# print(dict)
# new_dict={}
# for key , value in dict.items():
#       if key=="name":
#           new_dict["stream"]="ece"
#       else:
#           new_dict[key]=value
# print(new_dict)


# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# print("anusha" in dict.values())

# dict={"name":"anusha",
#       "age":21,
#       "edu":"btech"}
# key=list(dict.keys())
# print(key[0])
# print(dict["name"])


