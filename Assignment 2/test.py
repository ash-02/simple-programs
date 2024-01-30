import heapUtilities

def max_heapify(array, i):

    while(True):
        left = heapUtilities.left(i)
        right = heapUtilities.right(i)
        length = len(array) - 1  # for termination condition check
        largest = i

        if left <= length and array[i] < array[left]:
            largest = left
        if right <= length and array[largest] < array[right]:
            largest = right
        if largest != i:
            # array[i], array[largest] = array[largest], array[i]
            heapUtilities.swap(array, i, largest)
            i = largest
        else:
            break

def buildMaxHeap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A,i)
    print(heapUtilities.is_max_heap(A))