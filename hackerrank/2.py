# # n = 3
# # a = [1,2,3]
# # k = 4

# # maxlen = 0
# # maxcount = [0]

# # for i in range(0, n):
# #     sum = 0
# #     count = 0
# #     for j in range(i, n):
# #         print(a[j:n])

# #         # for h in range(i,j):
# #         #     print(a[h], end =" ");
# #         #print("--------")
# #         count += 1
# #         sum = sum + a[j]
# #         if sum == k:
# #             maxcount.append(count)

# # print(max(maxcount))



# # # def getLongestSubarray(a: [int], k: int) -> int:
# # #     n = len(a) # size of the array.

# # #     length = 0
# # #     for i in range(n): # starting index
# # #         s = 0
# # #         for j in range(i, n):
# # #             s += a[j]

# # #             if s <= k:
# # #                 length = max(length, j - i + 1)
# # #     return length

# # # if __name__ == '__main__':
# # #     a = [1, 2, 3]
# # #     k = 4
# # #     len = getLongestSubarray(a, k)
# # #     print("The length of the longest subarray is:", len)





# from typing import List

# def getLongestSubarray(a: [int], k: int) -> int:
#     n = len(a) # size of the array.

#     length = 0
#     for i in range(n): # starting index
#         for j in range(i, n): # ending index
#             # add all the elements of
#             # subarray = a[i...j]:
#             s = 0
#             for K in range(i, j+1):
#                 s += a[K]

#             if s <= k:
#                 length = max(length, j - i + 1)
#     return length

# if __name__ == "__main__":
#     a = [1, 2, 3]
#     k = 4
#     length = getLongestSubarray(a, k)
#     print(f"The length of the longest subarray is: {length}")




from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        s = 0
        for j in range(i, n):
            s += a[j]

            if s <= k:
                length = max(length, j - i + 1)
    return length

if __name__ == '__main__':
    a = [-1, 1, 1]
    k = 1
    len = getLongestSubarray(a, k)
    print("The length of the longest subarray is:", len)
