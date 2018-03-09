# Write a Python program to select the odd items of a list

def oddFromList(listprovided):
    j = 0
    oddItems = []
    while j < len(listprovided):
        if listprovided[j]%2 != 0:
            oddItems.append(listprovided[j])
        j += 1
    return oddItems


listprovided = [3,4,5,6,4,2,1,3,4,6,7,8]
output = oddFromList(listprovided)
print(output)
