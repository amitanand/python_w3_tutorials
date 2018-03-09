# Write a Python program to split a list into different variables.

def splitList(listprovided):
    string = "variable"
    for i in range(len(listprovided)):
        print(string ," ",i," :",listprovided[i])

listprovided = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
splitList(listprovided)