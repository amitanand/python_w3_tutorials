import math
# items = [['rice',2.4,8],['flour',1.9,5],['corn',4.7,6]]
# for x in items:
#     print("Product : %s Price :%.2f Quality :%i" %(x[0],x[1],x[2]))
#
# print("-----------------------------List Comprehension ----------------------------------")
#
# list1 = [1,2,3,4,5,6]
# print([i*2 for i in list1])
#
# words = 'here is a sentence'.split()
# print([[word, len(word)] for word in words])

def longestWord(sentence):
    idx = []
    wordlist = []
    for m in sentence.split():
        idx.append(len(m))
        wordlist.append(m)
    d = max(idx)
    print("Longest word :",wordlist[idx.index(d)])



label = 'The longest word in this sentence'
longestWord(label)