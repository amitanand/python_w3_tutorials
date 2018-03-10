import time

n1=int(input("Please enter the first integer :"))
n2=int(input("Please enter the second integer :"))
n3=int(input("Please enter the third integer :"))
list_num=[]
print("Appending inputs into lists ...")
time.sleep(1)
print("Sorting the inputs ...")
time.sleep(1)
list_num.append(n1)
list_num.append(n2)
list_num.append(n3)
print(list_num)
print(sorted(list_num))