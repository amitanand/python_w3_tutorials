#  Write a Python program to get numbers divisible by fifteen from a list using an anonymous function ?

import time

list_num=[]
i=0
n=int(input("Enter the no of elements you want to keep in the list :"))
while i<n:
    list_ele=int(input("Please enter the num for the list : "))
    list_num.append(list_ele)
    i+=1
time.sleep(1)
print("Preparing lists ...")
time.sleep(1)
print(list_num)

x=int(input("Please enter the number you want to check the divisibilty with :"))
def number_check(x):
    for a in list_num:
        if a%x ==0:
            print("Numbers divisible by",x,"in the lists are :",a)
            

number_check(x)
