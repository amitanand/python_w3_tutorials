import math
import time

def distance(x1,y1,x2,y2):
    print("Calculating distance ...")
    time.sleep(1)
    space = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("Distance :",space)

distance(4,0,6,6)