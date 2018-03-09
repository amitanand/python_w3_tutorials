#  Write a Python program to count the number of elements in a list within a specified range.

def countElement(n,m,listprovided):
    count = 0
    for i in range(len(listprovided)):
        if listprovided[i]>=n and listprovided[i]<=m:
            count += 1
        else:
            pass

    return count

listprovided = [10,20,30,40,40,40,70,80,99]
output = countElement(40,100,listprovided)
print(output)
