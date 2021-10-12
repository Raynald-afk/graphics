import matplotlib.pyplot as plt
"""
This program reads in a file containing 
percentage of the total phones sales world
wide and draws them on a pie chart
"""
# opening the file
file = open("results","r")
my_dic = {}
#reading the file content into a dictionary
#phone names as keys and percentage as values
for info in file:
    content = info.strip().split()
    if content[0] not in my_dic:
        my_dic[content[0]] = int(content[1])
#list comprenhesions of the phone names and percentages
phone_names = [key for key,value in my_dic.items()]
phone_percentage = [value for key,value in my_dic.items()]
#this draws the pie chart
plt.pie(phone_percentage,labels=phone_names)
plt.title("Pie Chart Of Phones Sales World Wide👌🎴")
plt.show()