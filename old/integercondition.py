import time

x=int(input("Please enter the first integer :"))
y=int(input("Please enter the second integer :"))
print("Calculating ...")
time.sleep(1)
sum=x+y
diff=x-y
if (x ==y) or (sum ==5) or (diff ==5):
    print("TRUE")
else:
    time.sleep(1)
    print("Sum :",sum)
    print("Difference :",diff)