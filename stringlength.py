import time

string_1="A"
string_2="Adi"
len_string1=len(string_1)
len_string2=len(string_2)
print("Operation on string 1 ...")
time.sleep(2)
if len_string1<2:
    print("As the length of string is less than 2,  printing the string ...")
    time.sleep(1)
    print(string_1)
    time.sleep(1)
else:
    print(string_1[:2])

print("Operation on string 2 ...")
time.sleep(2)
if len_string2<2:
    print("As the length of string is less than 2,  printing the string ...")
    time.sleep(1)
    print(string_2)
else:
    print("As the length of string is more than 2,  printing the first 2 characters of string ...")
    time.sleep(1)
    print(string_2[:2])