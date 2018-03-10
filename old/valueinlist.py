import time

list_1=[1, 5, 8, 3]
x=int(input("Please enter the number you want to check in the list :"))
time.sleep(1)
print("Checking ... ")
time.sleep(1)
if (x in list_1):
    print(x,"is there in the list")
else:
    print(x,"is not there in the list")

