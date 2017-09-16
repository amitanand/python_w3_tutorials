import time

def abs(n):
    if n<0:
        print("Computing absolute ...")
        time.sleep(1)
        print("The absolute value of",n,"is :",-1*n)
        time.sleep(1)
    else:
        print("Computing absolute ...")
        time.sleep(1)
        print("The absolute value of", n, "is :", -1 * n)
        time.sleep(1)

abs(2)
abs(-6)
