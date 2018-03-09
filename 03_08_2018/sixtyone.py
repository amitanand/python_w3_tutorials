# Write a Python program to create a list of empty dictionaries

def createEmptyDict(n):
    listEmptyDict = []
    for i in range(n):
        new_dict = dict()
        listEmptyDict.append(new_dict)
    return listEmptyDict

n = int(input("Please enter the number of empty dict you want to create :"))
output = createEmptyDict(n)
print(output)