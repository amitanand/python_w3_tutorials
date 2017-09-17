import time

x=int(input("Please enter the first number :"))
y=int(input("Please enter the second number :"))
z=int(input("Please enter the third number :"))
if (x==y) or (y==z) or (x==z):
    print("Calculating sum...")
    time.sleep(1)
    print("As two inputs are same, sum is:",0)
else:
    sum=x+y+z
    print("Calculating sum ...")
    time.sleep(1)
    print("Sum :",sum)