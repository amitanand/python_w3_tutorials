#  Write a Python program to swap two variables ?

import time
x=int(input("Please enter the value of first int :"))
y=int(input("Please enter the value of second int :"))
print("The value of first int is",x,"and the value of second int is",y)
time.sleep(2)
print("Swapping the variables ...")
time.sleep(1)
x,y=y,x
print("The value of first int is",x,"and the value of second int is",y)

