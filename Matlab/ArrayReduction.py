# Given an array arr of n integers, in a single operation, one can choose two indices, and j, 
# and delete arr[i] from the array if 2 * arr[i] ≤ arr[j].
# A particular element can be chosen at most once.
# Find the minimum possible size of the array after performing the operation any number of times, possibly zero.

def getMinSize(arr):

    arrList = list(arr)
    arrList.sort()
    consideredElements = set()
    i = -1
    while (i < len(arrList) // 2 ):
        i += 1
        j = len(arrList) // 2
        while(j < len(arrList)):
            if 2 * arrList[i] <= arrList[j] and arrList[j] not in consideredElements:
                consideredElements.add(arrList[j])
                arrList.remove(arrList[i])
                arrList.remove(arrList[j])
                i -= 1
                break
            j += 1

    return len(arr) - len(arrList)

if __name__ == '__main__':
    arr = [1,2,3,4,16,32,64]
    print(getMinSize(arr))  # 3
    arr = [1,3,2,1]
    print(getMinSize(arr))  # 4
