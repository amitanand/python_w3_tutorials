# Write a Python program to get the smallest number from a list

# def smallest(lisofnum):
#     return min(lisofnum)
# listofnum = [1,2,3,4,5,6,7,8,9]
# output = smallest(listofnum)
# print(output)

print("-----------------------without inbuilt function -------------------------")

def smallestNum(listofNums):
    for i in range(len(listofNums)-1):
        if listofNums[i]>listofNums[i+1]:
            listofNums[i] = listofNums[i+1]
        else:
            pass

def checkList(listoNums):
    for i in range(len(listofNums)-1):
        if listofNums[i]<listofNums[i+1]:
            pass
        else:
            smallestNum(listofNums)

    return listofNums[0]

listofNums = [7,4,2,-1,5,0]
smallestNum(listofNums)
output = checkList(listofNums)
print(output)