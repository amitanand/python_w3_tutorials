import time
import math

def Hypotenuse(base,height):
    hypo=math.sqrt(base**2+(height)**2)
    print("Calculating hypotenuse ...")
    time.sleep(1)
    print("Hypotenuse :",hypo)

Hypotenuse(3,4)