print("Word Conditions:")
print("1) The word must be between 1 and 20 characters long")
print("2) There must be no punctuation (e.g: '.' or ',' etc ")
print("")


# tenant
# ! @ @!
# estate
# ------------------------Final Attempt---------------------------------------------------------------------------------
def isomorphic(word1, word2):  # define new function
    my_dict = {}  # blank dictionary
    mapped = set()  # blank unordered list
    if len(word1) != len(word2):  # if length word 1 and word 2 are not the same
        print(f"Words {word1} and {word2} are different lengths")
        exit()
    else:
        for i in range(len(word1)):  # loop (length of word one)
            if word1[i] in my_dict and my_dict[word1] != word2[i]:  # if word one (letter num of loop) is in dictionary,
                return False                                        # and word one in dictionary is not equal to word 2 (letter num of looop), return false
            else:
                if word2[i] in mapped:  # if word 2 (letter num of loop) is in unordered list
                    return False  # return false
                else:
                    my_dict[word1[i]] = word2[i]  # letter of word one in dictionary equals letter of word 2
                    mapped.add(word2[i])  # add letter of word two to unordered list
            return True  # return true


word1 = input("Enter the first word: ")  # word one user input
word2 = input("Enter the second word: ")  # word two user input

if isomorphic(word1, word2):  # if function true
    print(f"Words {word1} and {word2} are isomorphic!")  # are isomorphic
else:  # if function not true
    print(f"Words {word1} and {word2} are not isomorphic")  # are not isomorphic
# ------------------------------Attempt 1-------------------------------------------------------------------------------
# enu1 = enumerate(str1)
# enu2 = enumerate(str2)
# dict1 = {}
# dict2 = {}
#
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         print(1)
#
# else:
#     print("Else")

# for i, value in enu_word1:
#     #    print(i, value)
#     dict1[i] = value
#
# for i, value in enu_word2:
#     #    print(i, value)
#     dict2[i] = value
#
# print(dict1)
# print(dict2)
#
# for i in range(len(word1)):
#     if dict1[i] == dict2[i]:
#         print(i)
# --------------------------------Attempt2------------------------------------------------------------------------------
# str1 = "tenant"
# str2 = "estate"
# my_dict = []
#
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str1[i] in my_dict:
#             if my_dict[str1] == str2[i]:
#                 print("Not Isormophs")
#             else:
#                 print("Isomorphs")
#         else:
#             if str1[i] == my_dict[i]:
#                 my_dict[i] = i + 1
#             else:
#                 my_dict[i] = str1[i]
# else:
#     print(f"{str1} and {str2} are not isomorphic pairs")
