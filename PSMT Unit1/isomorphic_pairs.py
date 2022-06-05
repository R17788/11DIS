# print("Word Conditions:")
# print("1) The word must be between 1 and 20 characters long")
# print("2) The word must be all lowercase")
# print("3) There must be no punctuation (e.g: '.' or ',' etc ")
# print("")

# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")
#
# tenant
# ! @ @!
# estate
#

# list1 = list(word1)
# list2 = list(word2)
# print(list1)
# print(list2)


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

str1 = "tenant"
str2 = "estate"
my_dict = []

if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] in my_dict:
            if my_dict[str1] == str2[i]:
                print("Not Isormophs")
            else:
                print("Isomorphs")
        else:
            if str1[i] == my_dict[i]:
                my_dict[i] = i+1
            else:
                my_dict[i] = str1[i]
else:
    print(f"{str1} and {str2} are not isomorphic pairs")


# Find if strings 'X' and 'Y' are Isomorphic or not
def isIsomorphic(X, Y):
    # if 'X' and 'Y' have different lengths, they cannot be isomorphic
    if len(X) != len(Y):
        return False

    # use a dictionary to store a mapping from characters of string 'X' to string 'Y'
    d = {}

    # use set to store a pool of already mapped characters
    s = set()

    for i in range(len(X)):
        x = X[i]
        y = Y[i]

        # if 'x' is seen before
        if x in d:
            # return false if the first occurrence of `x` is mapped to a
            # different character
            if d[x] != y:
                return False

        # if 'x' is seen for the first time (i.e., it isn't mapped yet)
        else:
            # return false if 'y' is already mapped to some other char in 'X'
            if y in s:
                return False

            # map 'y' to 'x' and mark it as mapped
            d[x] = y
            s.add(y)

    return True


if __name__ == '__main__':

    X = 'ACAB'
    Y = 'XCXY'

    if isIsomorphic(X, Y):
        print(f'{X} and {Y} are Isomorphic')
    else:
        print(f'{X} and {Y} are not Isomorphic')
