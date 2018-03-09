# Write a Python program to insert a given string at the beginning of all items in a lis

def insertString(str1,list1):
    list2 = []
    for i in range(len(list1)):
        list2.append(str1 + str(list1[i]))

    return list2

str1 = str(input("Please enter the string you want insert at the beginning :"))
list1 = [1,2,3,4]
output = insertString(str1,list1)
print(output)