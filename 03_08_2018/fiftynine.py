# Write a Python program to check if the n-th element exists in a given list.

def existence(n,list1):
    if n>len(list1)-1:
        print(n,"th element doesn't exist in the list")
    else:
        print(n,"th element exists :",list1[n])

list1 = [1,2,3,4,5,6,7,8,9,0]
n = int(input("Please enter the index you want to check :"))
existence(n,list1)