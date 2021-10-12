# write comments and test it with gradscope
def Hat_style(direction):
    """
    This function prints out Hat style direction
    it can be either decided by the user all a custom output

    """
    if direction == "right":
        print("        ~-~")
        print("      /-~-~-\\")
        print("     /_______\___")
    elif direction == "left":
        print("       ~-~ ")
        print("     /-~-~-\\")
        print(" ___/_______\\")
    elif direction == "both":
        print("        ~-~")
        print("      /-~-~-\\")
        print("  ___/_______\___")
    elif direction =="front":
        print("        ~-~ ")
        print("      /-~-~-\\")
        print("     /_______\\")

def Hair(hair,eye_shape):
    """
        This function prints out Hair style direction
        it can be either decided by the user all a custom output
        it is only determined by true and false
        the eye shape is also determined by the user or by custom
        """
    if hair =="True":
        print('    "|"""""""|"')
        print('    "| ' + eye_shape + '   ' + eye_shape + ' |"')
        print('    "|   V   |"')
        print('    "|  ~~~  |" ')
        print("      \_____/")
    if hair =="False":
        print("     |'''''''|")
        print("     | " + eye_shape + "   " + eye_shape + " |")
        print("     |   V   |")
        print("     |  ~~~  |")
        print("      \_____/")

def torso_length(torso_height):
    """
    This function represents the torso length of the avatar.
    the lenght is controlled by a while loop
    :param torso_height:
    :return:
    """
    i = 1
    while i <= torso_height:
        print("       |-X-|")
        i+=1

def leg_length(height):
    """
    This function prints ot the leg length of he avatar
    while loop is also used to print the length of the avatar
    :param height:
    :return:
    """
    i = 0
    front = "///"
    back = "\\\\\\"
    lenght = 6
    j = 1
    print(lenght * " " + " HHHHH")
    while i <= (height)-1:
        space = lenght - i
        print(space * " " + front + j * " " + back)
        j += 2
        i += 1

def Arm_style(arm_style):
    """
    This function prints out the arm style of the avatar.
    The haracter printed out is determined by the use or
    customally printed out
    :param arm_style:
    :return:
    """
    i =1
    body_portion = "|---|"
    print("  ",end="")
    while i <= 11:

        if i == 1 or i == 11:
            print("0", end="")
        elif i == 6:
            print(body_portion,end="")
        else:
            print(arm_style,end="")

        i += 1
    print("\n",end="")


def Custom(direction,hair,eye_shape,arm_style,torso_height,height,user_choose):
    """
    This functiom prints out the avatar to the console
    it holds all the functions except the main function
    :param direction:
    :param hair:
    :param eye_shape:
    :param arm_style:
    :param torso_height:
    :param height:
    :param user_choose:
    :return:
    """
    Hat_style(direction)
    Hair(hair,eye_shape)
    if user_choose =="Jeff" or user_choose =="Chris":
        print("       |-X-|")
    Arm_style(arm_style)
    torso_length(torso_height)
    leg_length(height)



def main():
    # watch and download all Ato keys covers

    print("----- AVATAR -----")
    print("Select an Avatar or create your own:")
    user = input()
    if user =="Avatar":
        print("Choose from one of the pre-defined avatars")
        user_choose = input()
        if user_choose =="Jeff":
            direction = "both"
            hair = "False"
            eye_shape = "0"
            arm_style = "="
            torso_height = 4
            height =2
            Custom(direction,hair,eye_shape,arm_style,torso_height,height,user_choose)
            shoe = "#HHH#        #HHH#"
            print(shoe)
        elif user_choose == "Jane":
            direction = "right"
            hair = "True"
            eye_shape = "*"
            arm_style = "T"
            torso_height = 2
            height = 3
            Custom(direction, hair, eye_shape, arm_style, torso_height, height,user_choose)
            shoe = " <|||>       <|||>"
            print(shoe)
        elif user_choose =="Chris":
            direction = "front"
            hair = "False"
            eye_shape = "U"
            arm_style = "W"
            torso_height = 2
            height = 4
            Custom(direction, hair, eye_shape, arm_style, torso_height, height, user_choose)
            shoe = " <>-<>        <>-<>"
            print(shoe)
    elif user =="Custom":
        print("Answer the following questions to create a custom avatar")
        direction = input("Hat style ?\n")
        eye_shape = input("Character for eyes ?\n")
        hair = input("Long hair (True/False) ?\n")
        arm_style = input("Arm style ?\n")
        torso_height = int(input("Torso length ?\n"))
        height = int(input("Leg length (1-4) ?\n"))
        shoe = input("Shoe look ?\n")
        Custom(direction, hair, eye_shape, arm_style, torso_height, height,user)
        print(" "+shoe+7*" "+shoe)

main()