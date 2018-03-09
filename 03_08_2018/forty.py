# Write a Python program to split a list based on first character of word

def changeInt(list1):
    firstChar = set()
    for i in range(len(list1)):
        firstChar.add(list1[i][0])

    return firstChar

output = changeInt(['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call'])
print(output)



