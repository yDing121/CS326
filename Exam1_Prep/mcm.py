import numpy as np


def mcm(p, n):
    m = np.zeros((n+1, n+1))
    s = np.zeros((n,n+1))

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i,j] = float("inf")
            for k in range(i, j):
                q = m[i,k] + m[k+1, j] + p[i-1]*p[k]*p[j]

                if q < m[i, j]:
                    m[i,j] = q
                    s[i,j] = k

    return m,s

def printmcm(s:np.ndarray, i, j):
    if i==j:
        print(f" A{i} ", end = "")
    else:
        print("(", end="")
        k = int(s[i, j])
        printmcm(s, i, k)
        printmcm(s, k+1, j)
        print(")", end="")


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    n = len(p)-1
    m, s = mcm(p, n)

    print("--"*20 + "m")

    for row in m:
        print(row)

    print("--"*20 + "s")

    for row in s:
        print(row)

    print("--"*20)
    printmcm(s, 1, n)


