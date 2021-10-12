#Consistency
#Creativity
#Problem_sloving
#Responsibility
#Teamwork
#Dedication
# import random
# # file = open("log","r")
# # # folder = list()
# # # for info in file:
# # #     line = info.strip()
# # #     folder.append(line)
# # # print(folder)
# # folder = [info.strip() for info in file]
# # print(folder)
# random.seed(125)
# lent = 7
# line_count = lent
# i  = 0
# file = [1,2,3,4,5,6,7]
# names= ["John","Mark","James","Mattew","Peter","Raynald","Chorson"]
# while i < (line_count*5):
#     x = random.randint(0,(lent-1))
#     y = random.randint(0,(lent-1))
#     place,holder = names[x],names[y]
#     names[y],names[x] = place,holder
#     _place,_holder = file[x],file[y]
#     file[x],file[y] = _holder,_place
#     i+=1
# print(names)
# print(file)
# decrypted = list()
# line = file.index(3)
#
# j = 1
#
# while j<= len(names):
#     """
#     In order to get the correct index
#     I looped through the number list
#     and used it to append the value at the
#     index of the place.
#     """
#     pos = file.index(j)
#     decrypted.append(names[pos])
#
#     j+=1
# print(decrypted)

# file = [1,2,3,4,5,6,7]
# names= ["John","Jark","James","Mattew","Peter","Raynald","Jhorson"]
# # the all the basic list functions.
#
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
# date = [("Benjin",49),("tokyo",12)]
# # understand how it works
# var = lambda date:(date[0],date[1]+10)
# temp = list(map(var,date))
# name = "jane"
# amount = 120000
#Use it to learn how to use it for decimal places
#print(f"You are the first man-made,and her name was {name} and the amount was ${amount:,d}")
# A = [1,3]
# B = ["x","y"]
# calc = [(x_1,y_1) for x_1 in A for y_1 in B]
# print(calc)
# first_name = input("Enter your first name:\t")
# second_name = input("Enter your second name:\t")

# _combine = lambda first_name,second_name : first_name.strip().title()+ " " + second_name.strip().title()
# print(_combine(first_name,second_name))

# year = 2021
# month = 10
# print(calendar.month(year,month))

user= 5
# j = 0
# i = 1
# while i <= user:
#     if j ==0:
#         print(i)
#     elif j ==1:
#         print(j,i)
#     elif j ==2:
#         print(j-1,j,i)
#     elif j ==3:
#         print(j-2,j-1,j,i)
#     elif j ==4:
#         print(j-3,j-2,j-1,j,i)
#
#     i+=1
#     j+=1
# user = 2
# i = 1
# while i<= user:
#     j = 1
#     while j <= i:
#         print(j,end = " ")
#         j+=1
#     print("\r")
#     i+=1
# user = 5
# i = 1
# while user >= i:
#     j =1
#     while j <=user:
#         print(j,end= " ")
#
#         j+=1
#     print("\r")
#     user-=1

# numbers = [1,2,3,4]
# result = numbers.__add__([5,6,7,8,9])
# print(result)
# for i in range (5,0,-1):
#     j =0
#     for j in range(1,i+1):
#         print(j, end= " ")
#         j+=1
#     print("\r")
# for i in range(0,6):
#     j = i
#     for e in range(0,j):
#         print(j,end= " ")
#     print("\r")
from captcha.image import ImageCaptcha
# how the internet stores data especiall facebook
#make assurance of thier data is safe
# user_width = int(input("Enter your preferred width:\t"))
# user_height = int(input("Enter your preferred height:\t"))
# text = input("Enter your text to be Captched and the name of the file with a space:\t").split()
# print("Hint: End your file name with '.png'")
# screen = ImageCaptcha(width=user_width,height=user_height)
# data = screen.generate(text[0])
# screen.wr e(text[0],text[1])
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(list(arr))
#     print(n)

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     _set = set(arr)
#     print(list(_set))
# numbers = [3,4,5,6,7,8,8]
# _new = []
# [_new.append(x) for x in numbers if x not in _new]
# print(_new)
  # This program displays step-by-step instructions
  # for disassembling an Acme dryer.
  # The main function performs the program's main logic.
# scores = []
# if __name__ == '__main__':
#     for _ in range(int(input("First Enter the number of people you want to register and press Enter: "))):
#
#         name = input("Enter the name and press Enter: ")
#         score = float(input("Enter the score and press Enter!: "))
#         print()
#         names.append([name,score])
#     for i in range(1,len(names)):
#         if names[i][1]== names[i-1][1]:
#             print(names[i])
# print(names)
# This program first asks the user the number of employers
# to enter their data for testing
# It then asks the user to type in the names of the employees
# and their list of rankings

