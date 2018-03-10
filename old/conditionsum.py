import time

x=int(input("Please enter the first number :"))
y=int(input("Please enter the second number :"))
print("Calculating sum :")
time.sleep(1)
sum=x+y
print("Sum :",sum)
time.sleep(1)
if (sum>15) and (sum<20):
    print("As the sum of the 2 inputs is between 15 and 20 ...")
    time.sleep(1)
    print("Sum :",20)
else:
    time.sleep(1)
    print("As the sum of the 2 inputs is not between 15 and 20 ...")
    time.sleep(1)
    print("Sum :",sum)
