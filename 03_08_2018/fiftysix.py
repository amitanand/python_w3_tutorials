# Write a Python program to convert a string to a list.

def strConversion(stringProvided):
    strToList =[]
    for i in range(len(stringProvided)):
        strToList.append(list(stringProvided[i]))

    return strToList

stringProvided = 'Amit Anand'
output = strConversion(stringProvided)
print(output)


        