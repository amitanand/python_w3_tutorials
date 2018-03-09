# Write a Python program to split a list every Nth element

def splitList(listprovided,n):
    list2 = [i*n for i in range(len(listprovided))]
    i = 0
    while i < int(len(listprovided)/2):
        print(listprovided[list2[i]:list2[i+1]])
        i += 1

listprovided = ['a','b','c','d','e','f','g','h','i','j']
splitList(listprovided,2)
