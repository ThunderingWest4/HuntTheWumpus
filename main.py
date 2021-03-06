import random
import place
import time

paths = {1 : [5, 2, 8], 2 : [1, 3, 10], 3 : [2, 4, 12], 4 : [3, 5, 14], 5 : [4, 6, 1], 6 : [5, 15, 7], 7 : [6, 8, 17], 8 : [1, 7, 11], 9 : [10, 12, 19], 10 : [2, 9, 11], 11 : [8, 10, 20], 12 : [3, 9, 13], 13 : [12, 14, 18], 14 : [4, 13, 15], 15 : [6, 14, 16], 16 : [15, 17, 18], 17 : [7, 16, 20], 18 : [13, 16, 19], 19 : [9, 18, 20], 20 : [11, 17, 19]}
start = random.randint(1, 20)
amtArrows = 5

thing = place.env()
thing.env(start)

running = True
isDead = False
def dead(cause):
    place.disp("You died due to ", cause)
    isDead = True
place.disp("Welcome to Hunt the Wumpus!")
place.disp("Built in Python by ThunderingWest4")
place.disp("-----------------------------------")
while(running == True):
    
    inst = False
    current = start
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
            #place.disp("You have 5 Arrows.")
            inst = True
        elif(wantInst == "n" or wantInst == "N"):
            place.disp("Ok, lets get straight to the game!")
            inst = True
        else:
            place.disp("Invalid Response, try again")
    
    #back in main running loop
    Wump = thing.genWumpus(start)
    #dead = False
    while(isDead == False):
        #print(thing.Start)
        #print(thing.Map)
        place.disp(str("You are in cave " + str(current)))
        currConnec = paths[current]
        place.disp(str("You can go to caves: " + str(currConnec[0]) + ", " + str(currConnec[1]) + ", or " + str(currConnec[2])))
        c1 = currConnec[0]
        c2 = currConnec[1]
        c3 = currConnec[2]
        #near wumpus?
        if(c1 == Wump or c2 == Wump or c3 == Wump or thing.Map[c1] == 'w' or thing.Map[c2] == 'w' or thing.Map[c3] == 'w'):
            place.disp("You can smell a terrible stench coming from a nearby cave")
        #near bats?
        if(thing.Map[c1] == 'b' or thing.Map[c2] == 'b' or thing.Map[c3] == 'b'):
            place.disp("You hear the fluttering of many wings nearby")
        #near pits?
        if(thing.Map[c1] == 'p' or thing.Map[c2] == 'p' or thing.Map[c3] == 'p'):
            place.disp("You feel a draft of cool air")

        place.disp("What would you like to do?")
        place.disp("You can either shoot an arrow (s) or move to one of the connecting caves (m)")
        valid = False
        action = ""
        while(not valid):
            action = input("")
            if(action == "s" or action == "S"):
                shot = False
                while(shot == False):
                    place.disp("Which cave would you like to shoot into: ", str(c1), ", ", str(c2), ", or ", str(c3), "?")
                    cave = input("")
                    if((cave == str(c1) or cave == str(c2) or cave == str(c3))):
                        cave = int(cave)
                        if(cave == Wump):
                            place.disp("Congratulations! You successfully shot the Wumpus!")
                            isDead = True
                        elif(thing.Map[cave] == "p"):
                            place.disp("You hear your arrow clatter down what seems to be a deep pit")
                            Wump = thing.genWumpus(current)
                        elif(thing.Map[cave] == "b"):
                            place.disp("You hear a loud screech")
                            Wump = thing.genWumpus(current)
                        else:
                            place.disp("You failed to hit anything important.")
                            Wump = thing.genWumpus(current)
                        shot = True
                    else:
                        place.disp("Invalid Cave")


                valid = True
            elif(action == "m" or action == "M"):
                done = False
                while(done == False):
                    place.disp("Which cave would you like to move into: ", str(c1), ", ", str(c2), ", or ", str(c3), "?")
                    cave = input("")
                    if((cave == str(c1) or cave == str(c2) or cave == str(c3))):
                            cave = int(cave)
                            if(thing.Map[cave] == "p"):
                                done = True
                                dead("falling into a cave")
                                isDead = True
                            elif(cave == Wump):
                                done = True
                                dead("being eaten by the wumpus you just walked into")
                                isDead = True
                            elif(thing.Map[cave] == "b"):
                                done = True
                                place.disp("Congratulations!")
                                #thing.Map[cave] = ""
                                place.disp("You just ran into a flock of bats")                                
                                found = False
                                while(found == False):
                                    test = random.randint(1, 20)
                                    if(thing.Map[test] == "" and test != Wump):
                                        thing.Map[current] = ""
                                        current = test
                                        found = True
                                place.disp("You have been picked up by the bats as they attempted to escape you")
                                place.disp("and moved to cave ", current)
                            else: 
                                done = True
                                place.disp("You have moved into cave ", cave)
                                current = cave
                                    
                    else:
                        print("Invalid Cave")
                    valid = True
            else:
                place.disp("Inalid Command. Please try again")
    place.disp("Play again? Y/N")
    again = input("")
    if(again == "n" or again == "N"):
        running = False
        place.disp("Thanks for Playing!")
    elif(again == "Y" or again == "y"):
        place.disp("Let's do this.")
    else:
        place.disp("I didn't read a no so I'm assuming you want to play again!")
        isDead = False

