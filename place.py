import random
import time

Map = {1 : "", 2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : "", 8 : "", 9 : "", 10 : "", 11 : "", 12 : "", 13 : "", 14 : "", 15 : "", 16 : "", 17 : "", 18 : "", 19 : "", 20 : ""}


def disp(string, *argv):
    fin = string
    for i in argv:
        fin += i
    for c in fin:
        print(c, end='')
        time.sleep(0.05)
    print("")

def genWumpus(start):
    loc = start
    while(loc != start):
        loc = random.randint(1, 20)
    loc = int(loc)
    Map[loc] = "w"
    return loc

numPit = 5
numBat = 3

"""class Environment():
    #shape:
    #Pentagon where each point connects to a circle inside (5 points)
    #Circle: 10 points, every other one connects to the outside pentagon
    #the points that dont go to the outside pentagon go to the inner pentagon
    #Inner Penta: 5 points
    def __init__(self):
        generated_points = []
        outside_pentagon = []
        decagon = []
        inner_pentagon = []
        #Generate outside Pentagon
        for i in range(5):
            found = False
            while(found == False):
                possible = random.randint(1, 20)
                found = False if (possible in generated_points)

            if(found == True):
                outside_pentagon.append(possible)
                generated_points.append(possible)
        #Generate Decagon
"""
