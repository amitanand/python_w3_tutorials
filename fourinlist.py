import time

list_item=[]
n=int(input("How many items you want to put in the list : "))
i=0
while i<n:
    item=int(input("Please enter the integer input :"))
    list_item.append(item)
    i+=1

print("creating list ...")
time.sleep(1)
print("List has been created and now we will check number of 4's in it ")
time.sleep(1)
print("Checking ...")
time.sleep(1)
result= list_item.count(4)
print("Total number of 4's is :",result)


