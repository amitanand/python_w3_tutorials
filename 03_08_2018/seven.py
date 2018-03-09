# Write a Python program to remove duplicates from a list.

def removeduplicate(listprovided):
    newlist = []
    for i in range(len(listprovided)):
        if listprovided[i] in newlist:
            pass
        else:
            newlist.append(listprovided[i])
    return newlist

listprovided = [1,2,3,4,2,5,3,7,8,9,1,0,5,6,7,8,9]
output = removeduplicate(listprovided)
print(output)