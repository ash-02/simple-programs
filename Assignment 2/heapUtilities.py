def is_max_heap(A):
    n = len(A)
    print(A)

    for i in range(n // 2 - 1, -1, -1):
        l = left(i)
        r = right(i)

        if (l < n and A[l] > A[i]) or (r < n and A[r] > A[i]):
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