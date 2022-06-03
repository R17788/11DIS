# print("Word Conditions:")
# print("1) The word must be between 1 and 20 characters long")
# print("2) The word must be all lowercase")
# print("3) There must be no punctuation (e.g: '.' or ',' etc ")
# print("")

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
#
# tenant
# ! @ @!
# estate
#

list1 = list(word1)
list2 = list(word2)
print(list1)
print(list2)

i = 0
if list1[i] == list2[i]:
    print(1)
    i = + 1
