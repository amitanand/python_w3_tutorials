#  Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

def squarelist(n):
    outputList = []
    for i in range(1,n):
        outputList.append(i**2)

    print(outputList[5:])


squarelist(21)