def solve(A, p1, r1, B, p2, r2, i):
    if p1 > r1:
        return B[p2 + i - 1]
    if p2 > r2:
        return A[p1 + i - 1]
    if i == 1:
        return min(A[p1-1], B[p2-1])

    # Length of A that we are considering
    m = r1 - p1 + 1

    # Length of B that we are considering
    n = r2 - p2 + 1

    midA = p1 + min(m, int(i//2)) - 1
    midB = p2 + min(n, int(i//2)) - 1

    if A[midA-1] < B[midB-1]:
        return solve(A, midA+1, r1, B, p2, r2, i - (midA - p1 + 1))
    else:
        return solve(A, p1, r1, B, midB+1, r2, i - (midB - p2 + 1))


if __name__ == '__main__':
    A = [1,3,6,8,9,20]
    B = [2,4,5,13]
    idx = 2

    ans = solve(A, 1, len(A), B, 1, len(B), idx)
    print(ans)
    print(f"Correct:\t{sorted(A + B)[idx-1] == ans}")