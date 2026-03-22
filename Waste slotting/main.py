import os
x = 50
y = 50

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{x},{y}"

import pgzrun
import random

WIDTH = 1000
HEIGHT = 700
message ="Slot the waste into the corrects bins"

recycle_bin = Actor("recycle_bin")
recycle_bin.pos = (100,600)
hazardous_waste_bin = Actor("hazardous_waste")
hazardous_waste_bin.pos = (350,600)
organic_food_bin = Actor("organic_food_bin")
organic_food_bin.pos = (600,600)



def draw():
    screen.fill("light blue")
    recycle_bin.draw()
    hazardous_waste_bin.draw()
    organic_food_bin.draw()


pgzrun.go()
