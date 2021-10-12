from graphics import graphics
OFFSET = 35

def mountains_view(gui,grass_x,grass_y):
    #the sun
    sun_x = gui.mouse_x/OFFSET
    sun_y = gui.mouse_y/OFFSET
    gui.ellipse(sun_x+590,sun_y+80,80,80,"yellow1")
    # the mountains drawing
    mountain_x = gui.mouse_x / OFFSET
    mountain_y = gui.mouse_y / OFFSET
    gui.triangle(mountain_x + 350, mountain_y + 160,
                 mountain_x + 200, mountain_y + 450,
                 mountain_x + 500, mountain_y + 450, "pink3")
    #left mountain drawing

    gui.triangle(mountain_x +150,mountain_y +180,mountain_x -100,
                 mountain_y +450,mountain_x +420,mountain_y +450,"RoyalBlue1")

    # right triangle

    gui.triangle(mountain_x +540,mountain_y +180,mountain_x +800,
                 mountain_y +450,mountain_x +300,mountain_y +450,"papaya whip")
    #writing a loop for the grass
    grass_x = gui.mouse_x/OFFSET
    grass_y = gui.mouse_y /OFFSET
    x_chord = -100
    while x_chord <=750:
        gui.line( grass_x+x_chord, grass_y+430,grass_x+x_chord, grass_y+450, "lime green", 1)
        x_chord+=5
    gui.rectangle(grass_x - 100, grass_y + 450, grass_x + 800, grass_y + 300, "spring green")
    gui.rectangle(grass_x + 441, grass_y + 445, 20, 50, "brown4")
    gui.ellipse(grass_x + 450.5, grass_y + 405, 60, 90, "green4")


def main():
    gui = graphics(700,550,"Landscape")
    grass_x = gui.mouse_x / OFFSET
    grass_y = gui.mouse_y / OFFSET

    counter = 0
    first_bird = 0
    second_bird = 0
    third_bird = 0
    fourth_bird = 0
    fifth_bird = 0

    while True:
        x = gui.mouse_x
        y = gui.mouse_y
        gui.clear()
        gui.rectangle(-10,-10,1000,1000,"light blue")
        mountains_view(gui,grass_x,grass_y)
        # the birds loop
        gui.line(grass_x + 90+first_bird, grass_y + 100, grass_x + 115 +first_bird, grass_y + 110, "black", 3)
        gui.line(grass_x + 160+second_bird , grass_y + 120, grass_x + 185+second_bird , grass_y + 130, "black", 3)
        gui.line(grass_x + 230+third_bird , grass_y + 140, grass_x + 255+third_bird , grass_y + 150, "black", 3)
        gui.line(grass_x + 300+fourth_bird , grass_y + 160, grass_x + 325 + fourth_bird , grass_y + 170, "black", 3)
        gui.line(grass_x + 370+fifth_bird , grass_y + 180, grass_x + 395 +fifth_bird , grass_y + 190, "black", 3)

        gui.line(grass_x + 140 +first_bird , grass_y + 100, grass_x + 115+first_bird, grass_y + 110, "black", 3)
        gui.line(grass_x + 210+second_bird , grass_y + 120, grass_x + 185 +second_bird, grass_y + 130, "black", 3)
        gui.line(grass_x + 280+third_bird , grass_y + 140, grass_x+third_bird + 255 , grass_y + 150, "black", 3)
        gui.line(grass_x + 350+fourth_bird , grass_y + 160, grass_x + 325+fourth_bird , grass_y + 170, "black", 3)
        gui.line(grass_x + 420 +fifth_bird, grass_y + 180, grass_x + 395+fifth_bird , grass_y + 190, "black", 3)
        # conditional statements for the flying birds
        if fifth_bird ==400:
            fifth_bird = -450
        if fourth_bird ==400:
            fourth_bird = -450
        if third_bird ==480:
            third_bird = -370
        if second_bird == 540:
            second_bird = -310
        if first_bird ==620:
            first_bird =-230


        # this controls the loop of the flying birds
        first_bird += 2
        second_bird += 2
        third_bird += 2
        fourth_bird += 2
        fifth_bird += 2

        gui.update_frame(60)
    gui.primary.mainloop()

main()