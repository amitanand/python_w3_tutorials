import time

x=17
n=int(input("Please enter the number you want to subtract with 17 :"))
if n>x:
    absol_diff = -(n-x)
    result=2*(absol_diff)
    print("As",n,"is greater than",x,",calculating double to absolute diff ...")
    time.sleep(1)
    print("Result is :",result)
else:
    print("As", n, "is smaller than", x, ",calculating the diff ...")
    result=n-x
    time.sleep(1)
    print(result)