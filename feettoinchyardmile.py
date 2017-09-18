import time

def Distance(feet):
    feet_inch=feet*12
    feet_yard=feet*0.33
    feet_mile=feet*0.000189394
    print("calculating ...")
    time.sleep(1)
    print(feet,"feet is equal to",feet_inch,"inch")
    time.sleep(1)
    print(feet, "feet is equal to", feet_yard, "yard")
    time.sleep(1)
    print(feet, "feet is equal to", feet_mile, "mile")

Distance(12)