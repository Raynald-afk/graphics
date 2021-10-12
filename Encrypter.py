import random

def encryption():
    """
    This function opens the sample file to be
    encrypted. I used list comprenshions to apppend
    the contents of the sample text into a list
    as well as it's index into a list after that I appended
    them into two saparate file, encrypteed file and
    index file respectively
    :return:
    """

    file = open("sample.txt","r")
    file_content =[info.strip("\n") for info in file]
    index_key_list = [i+1 for i in range(len(file_content))]
    i = 0
    while i <= len(file_content)*5:
        random_int_x = random.randint(0,len(file_content)-1)
        random_int_y = random.randint(0,len(file_content)-1)
        swap_1,swap_2 = file_content[random_int_x],file_content[random_int_y]
        file_content[random_int_x],file_content[random_int_y]= swap_2,swap_1
        swap_3,swap_4 = index_key_list[random_int_x],index_key_list[random_int_y]
        index_key_list[random_int_x],index_key_list[random_int_y] = swap_4,swap_3
        i +=1
    info = open("index.txt","a")
    file = open("encrypted file.txt","a")
    for element in file_content:
        file.write(element + "\n")
        file.close
    for numbers in index_key_list:
        info.write(str(numbers)+"\n")
        file.close

def main():
    random.seed(125)
    encryption()

main()