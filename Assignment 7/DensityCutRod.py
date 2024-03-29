def ExtendedBottomUpCutRodDensityPerInch(p, n):
    r = [0] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            print("p[i]:", p[i - 1])
            print("i:", i)
            if q < p[j - 1]/j:
                print("p[i]/i:", p[j - 1]/j)
                q = p[j - 1]/j
        r[j] = q
    print(p)
    print(r[1:])
    return r

if __name__ == '__main__':
    ExtendedBottomUpCutRodDensityPerInch([1, 6, 15, 18], 4)