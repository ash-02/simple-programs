import heapUtilities

def maxHeapify(A, i):

    largest = i
    subtreeSorted = False
    n = len(A)

    while(subtreeSorted is False):

        l = heapUtilities.left(i)
        r = heapUtilities.right(i)

        if l < n and A[l] > A[i]:
            largest = l
        
        else:
            largest = i

        if r < n and A[r] > A[largest]:
            largest = r
        
        if largest != i:
            heapUtilities.swap(A, i, largest)
            i = largest
        else:
            subtreeSorted = True

def buildMaxHeap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(A,i)
    print(heapUtilities.is_max_heap(A))

# A = [4, 10, 3, 5, 1, 8, 7, 2, 9, 6]
# buildMaxHeap(A)
# print("Original Array:")
# print(A)
# print("Modified Array:")
# print(heapUtilities.is_max_heap(A))