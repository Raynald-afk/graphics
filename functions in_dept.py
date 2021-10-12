"""
1. keywords arguments
def numbers(odd,even)

numbers(even =2,odd =3)
this matches the arguments
correctly with its parameter
ignoring the positions

2.functions have optional arguments eg
def num(name, class = Csc110)

num(name) the class parameter has now
become an optional argument

3. def set(*num)

set(1,2,3,4,5) output = tuples(1,2,3,4,5)

4. def dictionary(**num)
the function above when placed
in arguments returns a dictionary
as the arguments been placed
as the keys and the values to which
it is assigned to.
dictionary(id = "1",name = "Smith",class ="Csc420")
returns
{id : 1,name :smith, class:Csc420}

"""

# def info(name,room ="Csc 110"):
#     """
#
#     :param name: gets the name of the user
#     :param room: gets the class of the user
#     :return: it returns nothing hence it is a void function
#     """
#     print(f"Welcome {name}, we are happy to have you in {room} class!😊")
#
# user = ""
# count = 1
# while user != "stop!":
#     """
#     This program asked the user the name and class
#     and prints out a welcoming message
#     """
#     print("If you do not have a class yet enter 'none' for the class name")
#     user = input(f"{count}. Please Enter only your first name and class:\t").split()
#     if user[1] =="none":
#         info(user[0])
#     else:
#         info(user[0],user[1])
#     count+=1
#     print()

def fizzBuzz(_input):
    """

    :param input: get an input from the user to get
    whether the int is a FizzBuzz or not
    :return: returns FizzBuzz or the integer when not
    hence it is a value-returning functions
    """
    if int(_input) % 3 == 0 and int(_input) % 5 ==0:
        return "FizzBuzz"
    elif int(_input) % 3 ==0:
        return "Fizz"
    elif int(_input) % 5 == 0:
        return "Buzz"
    return  int(_input)


count = 1
while True:
    """
    This is a loop that asks the user for an integer 
    until the user types stop
    the try and execpt get for valueerror messages and 
    asks the user to type an int 
    """
    try:
        user = (input(f"{count}. Enter a number or type 'stop! to end the program':\n"))
        if user =="stop!":
            break
        print(f"The number {user} is a {fizzBuzz(user)}!!")
        var = input("Please Press Enter or type stop to end the program: ")
        if var == "stop":
            break
    except ValueError:
        user = int(input(f"{count}. Enter a number again: "))
        print(fizzBuzz(user))


    count+=1