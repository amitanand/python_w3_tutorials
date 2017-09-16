import time

x=input("Enter a character you want to validate for vowel :")
if (type(x) == int) or (len(x)>1):
    print("Please check your input !! ")
else:
    if (x=='a') or (x=='e') or(x=='i') or(x=='o') or(x=='u'):
        print("Checking ...")
        time.sleep(1)
        print("It's a vowel")
    else:
        print("Cheking ...")
        time.sleep(1)
        print("It's not a vowel")
