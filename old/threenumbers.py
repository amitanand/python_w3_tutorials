import time

x1=int(input("Please enter the first number :"))
x2=int(input("Please enter the second number :"))
x3=int(input("Please enter the third number :"))

if x1==x2==x3:
    print("As the values are equal calculating thrice of their sum :")
    time.sleep(1)
    print("Result : ",3*(x1+x2+x3))
else:
    print("Calculating sum only ...")
    time.sleep(1)
    print("Sum :",x1+x2+x3)
