
"""
Learn how to  convert midi to video or audio
with only the keyboard to midi and then download midiculous
"""

def computer():
    """
    This code is responsible for the correct programing
    it returns the required specs to be tested with the
    user's input
    """
    word_lst = []
    with open("gradescope.txt","r") as file:
        for line in file:
            lines =line.rstrip("\n")
            word_lst.append(lines)
    return word_lst

def user():
    """
    This code retrives the user's output from a file
    into a list  and returns it to the main
    board to be compared with the required input

    """
    lst =[]
    with open("testfile.txt","r") as info:
        for word in info:
            words = word.rstrip("\n")
            lst.append(words)
    return lst
def board():
    """
    This function is responsible for printing out both the
    required out and compares it with the user's output to
    check for it's authenticity and then detects with an arrow
    if some line of the output do not match with the required
    output


    """
    total = 20
    lst = user()
    word_lst = computer()
    for i in range (0,len(lst)):
        length = total- len(word_lst[i])
        if (word_lst[i]) == (lst[i]):
            print(" "+word_lst[i]+length*" "+"|",lst[i])
        else: print(">"+word_lst[i]+length*" "+"|",lst[i])

def main():
    print(58 * " ", "------- Text-base Gradescope ------")
    print()
    board()
main()

