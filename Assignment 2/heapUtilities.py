def is_max_heap(arr):
    n = len(arr)
    print(arr)

    for i in range(n // 2 - 1, -1, -1):
        left_child = left(i)
        right_child = right(i)

        if (left_child < n and arr[left_child] > arr[i]) or (right_child < n and arr[right_child] > arr[i]):
            return False
        
    return True

def left(i):
    return (2*i) + 1

def right(i):
    return (2*i) + 2

def swap(A, i, largest):
    temp = A[i]
    A[i] = A[largest]
    A[largest] = temp