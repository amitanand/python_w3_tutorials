# Write a Python program to multiplies all the items in a list.

def multiply(listofnum):
    mult = 1
    for i in range(len(listofnum)):
        mult *= listofnum[i]
    return mult

listofnum = [3,2]
output = multiply(listofnum)
print(output)