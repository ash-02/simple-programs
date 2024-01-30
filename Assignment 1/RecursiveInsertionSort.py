def InsertionSort(A, N):
    for j in range(1,N):
        key = A[j]
        i = j - 1
        while A[i] > key and i >= 0:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    print("_____________________________")
    print(A)

def RecursionLoop(A, n):
    if n > 1:
        l = n - 1
        RecursionLoop(A=A, n=l)
        InsertionSort(A=A, N=l+1)

if __name__ == "__main__":
    print("Recursive Insertion Sort Starting....")
    A = [7, 2, 4, 1, 5, 3]
    N = len(A)
    RecursionLoop(A, N) 