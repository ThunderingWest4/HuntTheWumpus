import random
import time

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
    return loc

numPit = 5
numBat = 3
