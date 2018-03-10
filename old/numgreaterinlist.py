#      Write a Python program to test if a certain number is greater than all numbers of a list ?


import time
list_1=[25,65,95,31,54,12,54,68,94,32,75,24,82]
count_great=0
count_small=0
n=int(input("Enter a number you want to check whether it is greater or not :"))
print("Calculating with the list ... ")
time.sleep(1)
for i in list_1:
    if i>n:
        count_small+=1
    else:
        count_great+=1

if count_small>0:
    print(n,"is smaller than",count_small,"elements")
    time.sleep(1)
else:
    pass

if count_great>0:
    print(n,"is greater than",count_great,"elements")

