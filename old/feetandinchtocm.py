import time

def Convert_Height(feet,inch):
    feet_cm=30.48*feet
    inch_cm=2.54*inch
    print("Converting units ...")
    time.sleep(1)
    print(feet,"feet is equal to :",feet_cm,"cm")
    print(inch,"inch is equal to :",inch_cm,"cm")

Convert_Height(20,20)