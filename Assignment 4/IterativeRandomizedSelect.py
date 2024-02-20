import random

def randomized_partition(arr, p, r):
    pivot_index = random.randint(p, r)
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def randomized_select(arr, p, r, i):
    while p < r:
        q = randomized_partition(arr, p, r)
        k = q - p + 1
        if i == k:
            return arr[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i = i - k
    return arr[p]

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 2
result = randomized_select(arr, 0, len(arr) - 1, i)
print(f"The {i}th smallest element in the array is: {result}")