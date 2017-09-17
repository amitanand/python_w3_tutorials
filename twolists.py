import time

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print("Checking colours which are there in set 1 but not in set 2 ...")
time.sleep(1)
final_set=set(color_list_1-color_list_2)
print("Final set :",final_set)
