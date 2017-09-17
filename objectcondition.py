import time

x=input("Please enter the first input :")
y=input("Please enter the second input :")
print(type(x))
print(type(y))
if (type(x) =='int') and (type(y) == 'int'):
    time.sleep(1)
    print("As both the inputs are type 'int', adding both of them :")
    time.sleep(1)
    print("Sum :",x+y)
else:
    time.sleep(1)
    print("As type of your input are not same ...")
    time.sleep(1)
    print("EXITING PROGRAM")
