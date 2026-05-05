# li=eval(input("enter the list:"))
# empty=[]
# for i in li:
#     if i not in empty:
#         empty.append(i)
# print(empty)


num=[10,4,45,54]
max_1=0
max_2=0
for i in num:
    if i>max_1:
       max_2=max_1
       max_1=i
print(max_2)