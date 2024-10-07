import random

def makelist(k):
    return [i for i in range(0, 2**k)]

def removestuff(l, n):
    for i in random.sample(l, n):
        print(i, end=" ")
        l.remove(i)
    print()

def padleft(s, k):
    if len(s) < k:
        s = "0"*(k-len(s)) + s
    return s

def bintodec(s):
    s = s[::-1]
    f = 1
    ans = 0

    for i in range(len(s)):
        ans += f * int(s[i])
        f *= 2
    return ans

def get(i, j, l, k):
    return padleft(bin(l[i])[2:], k)[j]


def findmissing(candidates, pos, sol, k):
    if pos >= k:
        return bintodec(sol)

    onecnt = 0
    ones = []
    zeros = []
    for i in candidates:
        bstring = bin(i)[2:]
        bstring = padleft(bstring, k)
        # print(f"{i}:\t{bstring}", end="\t")
        if bstring[pos] == "1":
            onecnt += 1
            ones.append(i)
            # print(f"bit {pos} is 1")
        else:
            onecnt -= 1
            zeros.append(i)
            # print(f"bit {pos} is 0")

    if onecnt < 0:
        # print(f"More zeros than ones at position:\t{pos}")
        sol += "1"
        return findmissing(ones.copy(), pos+1, sol, k)
    else:
        # print(f"More ones than zeros at position:\t{pos}")
        sol += "0"
        return findmissing(zeros.copy(), pos+1, sol, k)


def fm(candidates, pos, cur, k, ARR):
    if pos >= k:
        return bintodec(cur)
    # print(candidates)
    ones = []
    zeros = []

    for i in candidates:
        # print(i)
        if get(i, pos, ARR, k) == "1":
            ones.append(i)
        else:
            zeros.append(i)

    if len(ones) < len(zeros):
        # print(f">>More zeros than ones at bit {pos}")
        return fm(ones, pos+1, cur+"1", k, ARR)
    else:
        # print(f">>More ones than zeros at bit {pos}")
        return fm(zeros, pos+1, cur+"0", k, ARR)



if __name__ == '__main__':
    k = 8
    l = makelist(k)
    random.shuffle(l)
    print(l)
    removestuff(l, 5)
    n = len(l)
    print(l)

    # print(findmissing(l, 0, "", k))
    print("---"*5)
    print(fm([i for i in range(n)], 0, "", k, l))