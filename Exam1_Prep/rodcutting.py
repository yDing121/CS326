def cut_rod_topdown(p, n, cache):
    if n == 0:
        return 0

    if n in cache.keys():
        return cache[n]

    q = float("-inf")

    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod_topdown(p, n-i, cache))

    cache[n] = q
    return q


def cut_rod(p, n, c=0):
    # c is cost per cut
    r = [0] * (n+1)
    s = [0] * (n+1)

    for j in range(1, n+1):
        q = float("-inf")
        for i in range(1, j+1):
            if q < p[i-1] - c + r[j-i]:
                q = p[i-1] - c + r[j-i]
                s[j] = i

        r[j] = q
    print(r[n])
    return (r, s)

def print_cut_rod(p, n):
    (r, s) = cut_rod(p, n)
    while n > 0:
        print(s[n])
        n -= s[n]





if __name__ == '__main__':
    price = [1,5,6,9,10,17,17,20]
    l = 8

    print_cut_rod(price, l)
    # cache = {}
    #
    # ans = cut_rod(price, l, cache)
    # print(ans)