# Write a Python program to get the difference between the two lists

def difference(listprovided1,listprovided2):
    output = list(set(listprovided1) - set(listprovided2))
    return output

listprovided1 = [1,2,3,4,5]
listprovided2 = [4,5,6,7,8]
result = difference(listprovided1,listprovided2)
print(result)