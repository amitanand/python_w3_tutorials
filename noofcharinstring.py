#  Write a Python program to count the number occurrence of a specific character in a string ?

import time
str_1 = str(input("Please enter the string :"))
a=input("Please enter the character you want to count the ouccurrence of  :")
print("Calculating it's occurrence ... ")
time.sleep(1)
print("Occurrence :",str_1.count(a),"times")
