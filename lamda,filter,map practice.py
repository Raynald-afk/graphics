# x = 100
# y =20
#
# # def bigger(x,y):
# #     if x> y:
# #         return True
# #     return False
# # validity = bigger(x,y)
# #
# # if validity is  True:
# #     print("x is greater than y")
# # else: print("y is greater x ")
#
# validity = lambda x,y: x if x >y else y
# vas = validity(x,y)
# if vas is x :
#     print("x is greater than y")
# else:
#     print("y is greater than x")
import math
# names = ["Kwadwo","Kwabena","Yaw","Kofi"]
# _day = ["Sunday","Tuesday","Thursday","Friday"]
#
# # contiune to learn with the map,filter and Lambda
# #Also learn the second to third video of the graphic # also download freecode tkinter lesson
# l_1= [1,2,3,4,5,6]
# l_2 = [1,2,3,4,5,6]
# even = [i for i in range(2,41)]
# # learn how lambda cnnects with map
# value = list(filter(lambda  x: x% 2 ==0 ,even))
# print(value)
#
# # def calc(l_1,l_2):
# #     new = list()
# #     for i in range (len(l_1)):
# #         total = l_1[i] + l_2[i]
# #         new.append(total)
# #     print(new)
# # calc(l_1,l_2)

# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]
# owners = [
#     {'Name': 'Jack Becker', 'age': 35, 'salary': 70000},
#     {'Name': 'Alex Forson', 'age': 32, 'salary': 40000},
#     {'Name': 'James Cmeroon', 'age': 28, 'salary': 10000},
#     {'Name': 'Kia havertz', 'age': 20, 'salary': 1000},
# ]
# for i in range(len(employees)):
#     print(employees[i].get("Name"))
# import csv
# print(dir(csv))

# for names in employees:
#     print(names)
# looper = iter(employees)
# while True:
#     try:
#         print(next(looper))
#     except StopIteration:
#         print("Iterating is Done !!!")
#         break
i = 0
x =[[1,2,3],
    [4,5,6],
    [7,8,9]]

y =[[9,8,7],
    [6,5,4],
    [3,2,1]]
# have to learn how to use lambda to do it
matrix = lambda x,y : x + y
total = []

# print((map(matrix,x,y)))
for i in range(len(x)):
    count = []
    for e in range(len(y)):
        if len(count)!=3:
            count.append(x[i][e]+y[i][e])
        if len(count) ==3:
            total.append(count)


print(total)

