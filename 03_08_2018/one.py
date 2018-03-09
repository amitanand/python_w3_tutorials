# Write a Python program to sum all the items in a list

def sum(listofnum):
    sum = 0
    for i in range(len(listofnum)):
        sum += listofnum[i]
    return sum

listofnum = [1,2,3,4,5,6,7,8,9]
output = sum(listofnum)
print(output)