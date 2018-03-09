# Write a Python program to insert an element before each element of a list

def insertEle(listprovided):
    for i in range(0,len(listprovided)*2,2):
        listprovided.insert(i,0)

    return listprovided

listprovided = [5,6,7,8,9]
output = insertEle(listprovided)
print(output)