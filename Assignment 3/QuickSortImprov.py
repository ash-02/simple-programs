def partition(arr, p, r):
    pivot = arr[r]
    a = p - 1
    b = p - 1
    for j in range(p, r):
        if arr[j] < pivot:
            a += 1
            b += 1
            # arr[a], arr[j] = arr[j], arr[a]
            if a != b:
                arr[b], arr[j] = arr[j], arr[b]
        elif arr[j] == pivot:
            b += 1
            arr[b], arr[j] = arr[j], arr[b]

    arr[a + 1], arr[r] = arr[r], arr[a + 1]
    return a + 1, b

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