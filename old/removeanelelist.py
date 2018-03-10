# Write a Python program to remove the first item from a specified list ?

import time

list_1=[]
i=0
n=int(input("Please enter the number of elements you want to enter in the list :"))
while i<n:
    list_ele=input("Please enter the  element :")
    list_1.append(list_ele)
    i+=1

print("Preparing lists ... ")
time.sleep(1)
print(list_1)

x=int(input("Please enter the index of the value you want to remove :"))
list_1.pop(x)
print("Removing the element from",x,"position ...")
time.sleep(1)
print("Current list :",list_1)

