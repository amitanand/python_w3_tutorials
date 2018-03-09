# Write a Python program to find a tuple, the smallest second index value from a list of tuples

def smallestIdx(tupleList):
    diffList = []
    for i in range(len(tupleList)):
        print(tuplList[i])
        diffList.append(tupleList[i][0]-tupleList[i][1])
        sorted(diffList)

    return diffList[-1]

tuplList = x = [(4, 1), (1, 2), (6, 0)]
output = smallestIdx(tuplList)
print(output)