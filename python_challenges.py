# def capital_indexes(str1):
#     list1 = []
#
#     for i in range(len(str1)):
#         if str1[i].isupper():
#             list1.append(i)
#
#     print(list1)
#
#
# capital_indexes("HI")

def mid(str1):
    if len(str1) % 2 == 1:
        for i in range(len(str1)-1):
            first = str1[0]
            last = str1[len(str1)-1]
            str2 = str1.strip(first)
            str2 = str2.strip(last)
            if len(str2) == 1:
                print(str2)
                exit()
            else:
                continue
    elif len(str1) % 2 == 0:
        print("")


mid("apple")
