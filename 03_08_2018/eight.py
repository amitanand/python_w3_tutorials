# Write a Python program to check a list is empty or not.

def check (listprovided):
    if len(listprovided) == 0:
        return ('Empty List')
    else:
        return ("Not Empty")

listprovided = [1,2]
print(check(listprovided))
listprovided1 = []
print(check(listprovided1))