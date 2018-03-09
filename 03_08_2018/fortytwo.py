# Write a Python program to find missing and additional values in two lists

def missAddValues(list1,list2):
    missingValue = []
    additionalValue = []
    for i in range(len(list2)):
        if list1[i] in list2:
            pass
        else:
            missingValue.append(list1[i])
        if list2[i] in list1:
            pass
        else:
            if i == len(list2):
                break
            else:

                additionalValue.append(list2[i])

    return (missingValue,additionalValue)

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
missing,additional = missAddValues(list1,list2)
print(missing,additional)