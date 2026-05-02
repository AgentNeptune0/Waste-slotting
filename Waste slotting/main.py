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
start_speed = 1
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



def create_trash_items():
    #removing old trash items
    items.clear() 

    for i in range(current_level+1):
        #randomly picking trash item images from ITEMS
        image,bin_number = random.choice(ITEMS)
        #print(image)
        waste = Actor(image)

        #Setting a random x axis position
        waste.x = random.randint(100,WIDTH-100)

        #Setting y axis from the top of the window
        waste.y = 0
        
        #Storing correct bin number for the actor 
        waste.correct_bin = bin_number

        #Adding waste to the items list
        items.append(waste)

create_trash_items()

def draw():
    screen.fill("light blue")
    recycle_bin.draw()
    hazardous_waste_bin.draw()
    organic_food_bin.draw()
    general_waste.draw()
    screen.draw.text("1",center = (100,600),fontsize=30,color="black")
    screen.draw.text("2",center = (350,600),fontsize=30,color="black")
    screen.draw.text("3",center = (600,600),fontsize=30,color="black")
    screen.draw.text("4",center = (850,625),fontsize=30,color="black")
    if game_over == True:
        screen.draw.text("Game Over,You Lose!",center = (WIDTH//2,HEIGHT//2),fontsize=56,color="red") 
    elif game_complete == True:
        screen.draw.text("Congratulations,you win!",center = (WIDTH//2,HEIGHT//2))
    else:
        for waste in items:
            waste.draw()
    

def update():
    global game_over

    #stop update if game is finished
    if game_over == True or game_complete == True:
        return
    
    #Moving each item 
    for waste in items:
        waste.y +=  start_speed
        if waste.y >HEIGHT-100:
            game_over = True

def on_mouse_down(pos):
    global current_level,game_over,game_complete,start_speed
    if game_complete == True or game_over == True:
        return
    if len(items) == 0:
        return
    
    #Checking the first item
    first_item = items[0]
    
    for key,bin_Actor in bins.items():
        #Checking for the correct bin
        if bin_Actor.collidepoint(pos):
            #if correct bin clicked
            if key == first_item.correct_bin:
                items.pop(0)
                if len(items) == 0:
                    current_level = current_level + 1
                    #start_speed = start_speed + 1
                    if current_level >= final_level:
                        game_complete == True
                    else:
                        create_trash_items()
            else:
                #This block is used when you click the wrong bin
                game_over == True

                    

               

            
            




 


pgzrun.go()

