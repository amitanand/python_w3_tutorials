import time

given_string1="Motilal Nehru"
given_string2="Is Amit Anand"
print("Checking given_string1 ...")
time.sleep(1)
if given_string1[0:2]=='Is':
    print("As the string contain 'Is' in the beginning")
    print("Printing the given string ...")
    time.sleep(1)
    print(given_string1)
else:
    print("Updating string with 'Is' in the beginning ")
    time.sleep(1)
    print(given_string1[:2]+"Is")

time.sleep(2)
print("Now checking the condition with given_string2")
time.sleep(2)
if given_string2[0:2]=='Is':
    print("As the string contain 'Is' in the beginning")
    print("Printing the given string ...")
    time.sleep(1)
    print(given_string2)
else:
    print("Updating string with 'Is' in the beginning ")
    print(given_string2[:2]+"Is")