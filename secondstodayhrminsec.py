import time

def Second_to(sec):
    sec_min=sec/60
    sec_hour=sec_min/60
    sec_day=sec_hour/24
    print("Converting second to min , hour & day ...")
    time.sleep(1)
    print(sec,"second is equal to :",sec_min,"min")
    time.sleep(1)
    print(sec, "second is equal to :", sec_hour, "hours")
    time.sleep(1)
    print(sec, "second is equal to :", sec_day, "day")

Second_to(60)
