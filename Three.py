from graphics import graphics
import random
def main():
    """
    This short program displays three shapes
    at a random location eveytime the shapes
    comes off the canvas
    :return:
    """
    gui = graphics(600, 650, "Three Shapes")
    gui.rectangle(-50, -50, 700, 700, "white")
    i = -300
    rectangle_y = 50
    triangle_y = random.randint(200,600)
    middle = triangle_y-80
    circle_y = 220
    while True:
        gui.clear()
        gui.rectangle(-50, -50, 700, 700, "white")
        gui.rectangle(200+i,rectangle_y,70,70,"green2")
        gui.ellipse(235+i,circle_y,70,70,"yellow2")
        gui.triangle(190+i,triangle_y,230+i,middle,270+i,triangle_y,"blue1")
        if i == 470:
           rectangle_y = random.randint(100, 600)
           circle_y = random.randint(50,600)
           triangle_y = random.randint(200,600)
           middle = triangle_y-80
           i= -300
        i+=5

        gui.update_frame(60)
    gui.primary.mainloop()
main()