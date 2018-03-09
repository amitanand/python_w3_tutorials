# Write a Python program to find the second largest number in a list
def smallestNum(listprovided):
    outputlist = sorted(listprovided)
    return outputlist[-2]

listprovided = [-1,0,7,5,6,9,4,2,1,3]
output = smallestNum(listprovided)
print(output)