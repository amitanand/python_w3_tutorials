# Write a Python program to find the list of words that are longer than n from a given list of words

def lonerthanN(n,listprovided):
    for i in range(len(listprovided)):
        if len(listprovided[i])>n:
            print(listprovided[i])

n = int(input(" Please enter the value of n :"))
listprovided = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','1','2','5','45554']
lonerthanN(n,listprovided)
