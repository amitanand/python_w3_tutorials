# Write a Python program to generate groups of five consecutive numbers in a list

def groupOfFive():
    multofFive = [i*5 for i in range(1,6)]
    listgiven = [j for j in range(0,25)]
    for k in range(len(multofFive)):
        print(listgiven[multofFive[k]-5:multofFive[k]])

groupOfFive()