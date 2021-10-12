"""
This program prints out a hit_string in a form of a traget practice
To be used as graphics and proper graphing tool
"""
hit_string = input("Hit string:\n")

while len(hit_string)< 4 or len(hit_string) % 4 != 0:
    hit_string = input("Please provide a valid hit string:\n")
marker = input("Marker:\n")
while len(marker)!= 1:
    marker = input("Please provide a valid marker:\n")
i = 0
current_x= int(hit_string[i]+hit_string[i + 1])
current_y = int(hit_string[i + 2]+hit_string[i + 3])
index_row = 5
while index_row >=-5: # iterates as a row from positive 5 to negative 5
    index_col = -7
    current_x = int(hit_string[i] + hit_string[i + 1]) # gets the current x_postion
    current_y = int(hit_string[i + 2] + hit_string[i + 3])# gets the current y_position
    while index_col <= 7: # iterates fro negative 7 to positive 7 as the column
        if index_row == current_y and index_col == current_x:
            print(marker, end="")
            if int(hit_string[-2]+ hit_string[-1]) !=current_y: i+=4

        elif index_col == 0:print("|", end="")

        elif index_row ==0:print("-",end= "")

        else:print(" ",end ="")


        index_col+=1
    print("\n",end="")


    index_row-=1