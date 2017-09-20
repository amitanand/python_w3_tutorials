#  Write a Python program to filter the positive numbers from a list ?

import time

list_1=[]
i=0

n=int(input("Please enter the number of elements you want to enter :"))
while i<n:
    list_ele=int(input("Please enter the elements :"))
    list_1.append(list_ele)
    i+=1

print("Preparing list ... ")
time.sleep(1)
print(list_1)


def Positive():
    count_positive = 0
    for x in list_1:
        if x==0:
            pass
        elif x>0:
            time.sleep(1)
            print("Positive elements in the lists are :", x)
            count_positive+=1
        else:
            pass

    time.sleep(1)
    print("Total positive elements :",count_positive)


Positive()