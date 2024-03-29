import random


def memorized_rod_cutting_with_cost(p, n, r, c):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memorized_rod_cutting_with_cost(p, n - i, r, c) - c)
    r[n] = q
    return q

if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(p) - 1
    r = [-1] * (n + 1)
    c = 0
    # print(memorized_rod_cutting_with_cost(p, n, r, c))

    array = [5, 9, 2, 13, 8, 4, 11, 7, 1, 15, 3, 10, 6, 12, 14, 16]

    random.shuffle(array)

    print("Randomized array:", array)
