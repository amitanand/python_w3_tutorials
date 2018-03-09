# Write a Python program to get unique values from a list

def uniqueValues(listprovided):
    unique = []
    for i in range(len(listprovided)):
        if listprovided[i] not in unique:
            unique.append(listprovided[i])

    return unique

listprovided = [10, 20, 30, 40, 20, 50, 60, 40]
output = uniqueValues(listprovided)
print(output)
        