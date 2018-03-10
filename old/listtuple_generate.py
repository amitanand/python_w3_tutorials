import time

list_item=[]

i=0
x=int(input("Enter the number of elements you want to enter :"))
while i<x:
    item=input("Please enter the item you want to enter :")
    list_item.append(item)
    i+=1

print("Creating lists ...")
print("List created:",list_item)
time.sleep(1)

print("Creating tuple now ...")
tuple_item=tuple(list_item)
time.sleep(1)
print("Tuple created :",tuple_item)
