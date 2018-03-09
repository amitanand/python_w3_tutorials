# Write a Python program to create a list by concatenating a given list which range goes from 1 to n

def concaeLists(n,listprovided):
    newList = []
    for i in range(1,n+1):
            newList.append(listprovided[0]+str(i))
            newList.append(listprovided[1]+str(i))
    return newList


listprovided = ['p','q']
output = concaeLists(5,listprovided)
print(output)
