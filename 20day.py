#oops

#class
#--------class is  blueprint of an object
# class Student:
#     def display(self):
#         print("Hello")

#object
#---------
#object is the instance of class

# class Car:
#     def brand(self):
#         print("i have marathi suzuki car")
# car1=Car()
# car1.brand()

#constructor
#----------
#A constructor is special method that executes automatically when the object is created
#__ init __

# class Car:
#     def __init__(self,color,brand):
#         self.color=color
#         self.brand=brand
#     def car_brand(self):
#         print(f"brand is{self.brand}")
#     def car_color(self):
#         print(f"color is {self.color}")
# car1=Car("red","BMW")
# car1.car_brand()
# car1.car_color()


#self keyword
#--------------
#this self refers to the current object
# class student:
#     def __init__(self,name,age,gender,year):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.year=year
#     def student_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.year)
#     def student_year(self):
#         print(self.year)
# stu_1=student("anusha",21,"female",2026)
# stu_1.student_details()
# stu_1.student_year()


# name=input("")
# class Animal:
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
#     def cat(self):
#         print(f"name of animal is {self.name}")
#         print(f"sound is {self.sound}")
#     def dog(self):
#         print(f"name of animal is {self.name}")
#         print(f"sound is {self.sound}")

# animal_1=Animal(name,"meow meow")
# animal_2=Animal("Dog","bow bow")
# animal_1.cat()
# animal_2.dog()


#encapsulation
#--------------------
#this means binding data and the methods that works on the data inside the class,while limiting direct access to the internal state.
#aadhar is protected,means internal use only
#pan is private,this makes direct access hard


# class bank:
#     def __init__(self,name,aadhar,pan):
#         self.name=name
#         self._aadhar=aadhar
#         self.__pan=pan
#     def aadhar(self):
#         print(self._aadhar)
#     def pan(self):
#         print(self.__pan)
# bank_1=bank("anusha",234523453243,"ABCP0867G")
# bank_1.aadhar()