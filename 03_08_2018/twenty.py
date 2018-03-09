# Write a Python program access the index of a list

def indexList(n,listprovided):
    for i in range(len(listprovided)):
        if listprovided[i] == n:
            print("The number is found at",i," position")

listprovided = [1,2,3,4,5,6,7]
indexList(5,listprovided)
