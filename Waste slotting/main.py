import os
x = 50
y = 50

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{x},{y}"

import pgzrun
import random

WIDTH = 1000
HEIGHT = 700
message ="Slot the waste into the corrects bins"
final_level = 5
start_speed = 7
game_over = False
game_complete = False
current_level = 1
ITEMS = [("banana_peel","3"),("battery_waste","2"),("broken_ceramics","4"),("eggshells","3"),("pizza_box","4"),("plastic_bottle","1"),("soda_can","1"),("syringe","2")]
items = []
centre = (WIDTH//2,HEIGHT//2)

recycle_bin = Actor("recycle_bin")
recycle_bin.pos = (100,600)
hazardous_waste_bin = Actor("hazardous_waste")
hazardous_waste_bin.pos = (350,600)
organic_food_bin = Actor("organic_food_bin")
organic_food_bin.pos = (600,600)
general_waste = Actor("general_waste")
general_waste.pos = (850,600)

bins = {"1":recycle_bin,"2":hazardous_waste_bin,"3":organic_food_bin,"4":general_waste}


def trash_items():
    for i in range(current_level+1):
        random_number = random.randint(1,8)
        random_image = ITEMS[random.number][0]
        waste = Actor(random_image)


def draw():
    screen.fill("light blue")
    recycle_bin.draw()
    hazardous_waste_bin.draw()
    organic_food_bin.draw()
    general_waste.draw()


pgzrun.go()

