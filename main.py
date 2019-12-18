import random
import place
import time

paths = {1 : [5, 2, 8], 2 : [1, 3, 10], 3 : [2, 4, 12], 4 : [3, 5, 14], 5 : [4, 6, 1], 6 : [5, 15, 7], 7 : [6, 8, 17], 8 : [1, 7, 11], 9 : [10, 12, 19], 10 : [2, 9, 11], 11 : [8, 10, 20], 12 : [3, 9, 13], 13 : [12, 14, 18], 14 : [4, 13, 15], 15 : [6, 14, 16], 16 : [15, 17, 18], 17 : [7, 16, 20], 18 : [13, 16, 19], 19 : [9, 18, 20], 20 : [11, 17, 19]}
start = random.randint(1, 20)
amtArrows = 5

running = True

while(running == True):
    place.disp("Welcome to Hunt the Wumpus!")
    inst = False
    while(inst == False):
        place.disp("Instructions? Y/N")
        wantInst = input("")
        if(wantInst == "y" or wantInst == "Y"):
            place.disp("Your goal is to find and kill the Wumpus.")
            place.disp("There are 3 different types of hazards: ")
            place.disp("Caves, which cause a draft nearby and kill you if you fall")
            place.disp("Bats, which cause a flapping noise and carry you somewhere random")
            place.disp("And the Wumpus. Smelly, unbathed, dirty, it will give off a terrible smell")
            place.disp("The Wumpus won't fall down the bottomless pit nor will bats be able to move him")
            place.disp("Also, if you try to shoot an arrow and miss, the wumpus will move to a different location")
            place.disp("You have 5 Arrows.")
            inst = True
        elif(wantInst == "n" or wantInst == "N"):
            place.disp("Ok, lets get straight to the game!")
            inst = True
        else:
            place.disp("Invalid Response")
    
    #back in main running loop
    Wump = place.genWumpus(start)
    dead = False
    while(dead == False):
        place.disp("What would you like to do?")
        action = input("")
