def FibonacciSeriesMemorized(n):
    r = []
    for i in range(0, n + 1):
        r.append(-1)
    return FibonacciSeriesMemorized_Aux(n, r)

def FibonacciSeriesMemorized_Aux(n, r):
    if r[n] > -1:
        return r[n]
    if n == 0:
        q = 0
    elif n == 1:
        q = 1
    else:
        q = FibonacciSeriesMemorized_Aux(n - 1, r) + FibonacciSeriesMemorized_Aux(n - 2, r)
    r[n] = q
    return q

if __name__ == "__main__":
    print(FibonacciSeriesMemorized(20))