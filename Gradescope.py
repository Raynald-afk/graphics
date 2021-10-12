def file_load():
    """
    This code returns the numbers of the longest element and the word
    from the file
    """
    words_list = []
    main_word = []
    numbers_list =[]
    with open("testfile.txt", "r") as file:
        for info in file:
            line = info.strip().split("\n")
            words_list.append(line)

    for maxin in words_list:
       for element in maxin:
           numbers_list.append(len(element))
    return max(numbers_list), words_list,


def user():
    user_list = []
    grade_list = []
    with open("gradescope.txt","r") as file_name:
        for word in file_name:
            line = word.strip().split("\n")
            for element in line:
                user_list.append(element)

    with open("testfile.txt", "r") as file:
        for words in file:
            lines = words.strip().split("\n")
            for elements in lines:
                grade_list.append(elements)

    return user_list, grade_list
def board():
    """"
    This functions helps the output of
    both the user's work and computers's
    required output
    """
    maximum, words, = file_load()
    lenght = maximum +3

    user_list, grade_list = user()
    i = 0
    while i <= len(user_list)-1:
        var = lenght - len(user_list[i])
        if user_list[i]== grade_list[i]:
            print(" ",user_list[i],var*" "+"|",grade_list[i])
        elif user_list[i]!= grade_list[i]:
            print(">",user_list[i], var * " " + "|", grade_list[i])
        i+=1
def main():
    print(58*" ","------- Text-base Gradescope ------")
    print()
    board()


main()