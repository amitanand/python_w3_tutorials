 # Write a Python program to check if a number is positive, negative or zero ?

import time

n=float(input("Please enter a number :"))
print("Checking ...")
time.sleep(1)

if n ==0:
    print("Number is neither -ve nor +ve ")
elif n>0:
    print("It's a +ve integer")
else:
    print("It's a -ve integer")