x=int(input("Please enter the number you want to check :"))
if x<0:
    print("Please enter the positive number :")
elif(x==2):
    print("Smallest prime number  .!")
else:
    for i in range (2,x):
        if (x%i==0):
            print("Number is not prime")
            break
    else:
            print("Number is prime")


