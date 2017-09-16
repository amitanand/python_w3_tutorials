import time

string_1="MNSS Rai"
def stringCopies(n):
    if n<0:
        time.sleep(1)
        print("Please enter a positive integer :")
    else:
        print("Printing",n,"copies of string ...")
        time.sleep(1)
        print(string_1*n)

stringCopies(3)
stringCopies(-2)