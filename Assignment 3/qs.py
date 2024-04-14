# PARTITION(A, p, r)
# 1.	x = A[r]
# 2.	q = p - 1
# 3.	t = p

# 4.	for j = p to r:
# 5.	 	if A[j] < x:
# 6.	 		q = q + 1
# 7.	 		t = t + 1
# 8.	 		swap( A[j], A[q] )
# 9.	 		swap( A[j], A[t] )

# 10.	 	else if A[j] == x:
# 11.	 		t = t + 1
# 12.	 		swap( A[j], A[t] )

# 13.	 swap(A[j], A[t])
# 14.	Return q+1, t

def partition(arr, p, r):
    pivot = arr[r]
    q = p - 1
    t = p - 1
    for j in range(p, r):
        if arr[j] < pivot:
            q += 1
            t += 1
            arr[j], arr[q] = arr[q], arr[j]
            # if q != t:
            arr[j], arr[t] = arr[t], arr[j]
        elif arr[j] == pivot:
            t += 1
            arr[j], arr[t] = arr[t], arr[j]

    arr[r], arr[q + 1] = arr[q + 1], arr[r]
    return q + 1, t

def quick_sort(arr, p, r):
    if p < r:
        q, t = partition(arr, p, r)
        print("q =", q, "t =", t)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, t + 1, r)

# Example usage:
arr = [3, 6, 3, 10, 3, 2, 3]
print("Original array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
# PARTITION(A, p, r)