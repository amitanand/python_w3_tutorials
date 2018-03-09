# Write a Python program to select an item randomly from a list.

import random
def selectItem(listprovided):
    n = random.randint(0,len(listprovided))
    return listprovided[n]

listprovided = [1,2,3,4,5,6,7,8,9]
output = selectItem(listprovided)
print(output)