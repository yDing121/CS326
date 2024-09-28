def lcs_length(s1, s2):
    m = len(s1)
    n = len(s2)

    c = [[0 for _ in range(n+1)] for __ in range(m+1)]
    # for row in c:
    #     print(row)

    for i in range(1, m+1):
        for j in range(1, n+1):
            # print(f"s1: {s1[i - 1]}", end = "\t")
            # print(f"s2: {s2[j - 1]}")
            if s1[i-1] == s2[j-1]:
                # print("hi")
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]

    return c


def print_lcs(c, s1, s2, i, j):
    if i==0 or j==0:
        return
    if s1[i-1] == s2[j-1]:
        print_lcs(c, s1, s2, i-1, j-1)
        print(s1[i-1], end="")
    elif c[i-1][j] >= c[i][j-1]:
        print_lcs(c, s1, s2, i-1, j)
    else:
        print_lcs(c, s1, s2, i, j-1)



if __name__ == '__main__':
    s1 = "abcbdab"
    s2 = "bdcaba"
    c = lcs_length(s1, s2)

    for row in c:
        print(row)


    print_lcs(c, s1, s2, len(s1), len(s2))
