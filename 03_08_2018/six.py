#  Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def sorted(tuplelist):
    sortedlist= []
    num = 0
    i = 0
    while i <len(tuplelist):
        print(i)
        for j in range(1,len(tuplelist)+1):
            if tuplelist[i][j] != num:
               pass
            else:
                sortedlist.append(tuplelist[i])
                num += 1

    return sortedlist


tuplelist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
output = sorted(tuplelist)
print(output)