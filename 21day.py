#inheritance
class parent:
    pass
class child(parent):
    pass

#single inheritance
#---------------
# A child class inherits from one base class
# class animal:
#     def sound(self):
#         print("animals make sounds")
# class dog(animal):
#     def bark(self):
#         print("dog bark")
# d=dog()
# d.sound()
# d.bark()

#multiple inheritance
#---------------
#a child class inherits more than one class is called multiple inheritance.
# class father:
#     def skills(self):
#         print("driving")
# class mother:
#     def skill_2(self):
#         print("cooking")
# class child(father,mother):
#     def all_skills(self):
#         print("coding")
# c=child()
# c.skills()
# c.skill_2()
# c.all_skills()

# class father:
#     def face(self):
#         print("hair")
# class child(father):
#     def body(self):
#         print("hands")
# b=child()
# b.body()
# b.face()

# class aptitude:
#     def skills_1(self):
#         print("i have aptitude skills")
# class python:
#     def skills_2(self):
#         print("i have python skills")
# class dsa:
#     def skills_3(self):
#         print("i have dsa skills")
# class student(aptitude,python,dsa):
#     def skills_4(self):
#         print("i have soft skills")
# s=student()
# s.skills_1()
# s.skills_2()
# s.skills_3()
# s.skills_4()


#multilevel inheritance
#------------------inherits from another another child class
# class grandfather:
#     def house(self):
#         print("grandfather's house")
# class father(grandfather):
#     def land(self):
#         print("father's land")
# class child(father):
#     def flat(self):
#         print("my land")
# s=child()
# s.house()
# s.land()
# s.flat()


#hierarchical inheritance
#----------multiple child classes from one base class
# class father:
#     def property(self):
#         print("fathers property")
# class child_1(father):
#     def car(self):
#         print("first child car")
# class child_2(father):
#     def bike(self):
#         print("second child bike")
# c1=child_1()
# c2=child_2()
# c1.car()
# c2.bike()
# c1.property()
# c2.property()


#hybrid inheritance

# class A:
#     def methodA(self):
#         print("class A")
# class B(A):
#     def methodB(self):
#         print("class B")
# class C(A):
#     def methodC(self):
#         print("class c")
# class D(B,C):
#     def methodD(self):
#         print("class D")
# d=D()
# d.methodA()
# d.methodB()
# d.methodC()
# d.methodD()

#super()method
#----------------
class parent:
    def __init__(self):
        print("parent constructor")
class child(parent):
    def __init__(self):
        # super().__init__()
        print("child constructor")
c=child()



























