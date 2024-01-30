import heapUtilities

def maxHeapify(A, i):

    largest = i

    l = heapUtilities.left(i)
    r = heapUtilities.right(i)

    if l < len(A) and A[l] > A[i]:
        largest = l
    
    else:
        largest = i

    if r < len(A) and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        heapUtilities.swap(A, i, largest)
        maxHeapify(A, largest)

def buildMaxHeap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(A,i)
    print(heapUtilities.is_max_heap(A))
    

# A = [4, 10, 3, 5, 1, 8, 7, 2, 9, 6]
# buildMaxHeap(A)
# print(heapUtilities.is_max_heap(A))