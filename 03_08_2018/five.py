# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

def firstlast(listprovided):
    count = 0
    for i in range(len(listprovided)):
        if len(listprovided[i]) < 2:
            pass
        else:
            if listprovided[i][0] == listprovided[i][-1]:
                count += 1
            else:
                pass
    return count

listprovided = ['abc', 'xyz', 'aba', '1221']
output = firstlast(listprovided)
print(output)
