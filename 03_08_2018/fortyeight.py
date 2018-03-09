# Write a Python program to print a nested lists (each list on a new line) using the print() function.

def nestedList(listprovided):
    for i in range(len(listprovided)):
        print([listprovided[i]])

listprovided = ['Amit','Anand','Pai']
nestedList(listprovided)

