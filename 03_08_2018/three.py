# Write a Python program to get the largest number from a list

# def largestNum(lisofnums):
#     return max(lisofnums)
# listofnums = [1,2,3,4,5,6,7,8,9]
# output = largestNum(listofnums)
# print(output)

print("-----------------------------without inbuilt function -----------------------------")

def largest(listofnum):
    for i in range(len(listofnum)-1):
        if listofnum[i]>listofnum[i+1]:
            listofnum[i+1] = listofnum[i]
        else:
            pass
    return listofnum[-1]

listofnum = [2,48,5,1,4,6,7,9,43,5]
output = largest(listofnum)
print(output)