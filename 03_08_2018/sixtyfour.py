# Write a Python program to iterate over two lists simultaneously.

def iterTwoLists(list1,list2):
    for (a,b) in zip(list1,list2):
        print(a,b)

list1 = [1,2,3,4,5]
list2 = [10,11,12,13,14]
iterTwoLists(list1,list2)