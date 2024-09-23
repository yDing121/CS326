import math


def M_naive(n: int) -> int:
    if n <= 1:
        return 0
    else:
        return M_naive(math.floor(n/2)) + M_naive(math.ceil(n/2)) + n - 1


def S_naive(n: int) -> int:
    if n < 100:
        return M_naive(n)
    else:
        return min(M_naive(n), 8*math.ceil(n/5) + S_naive(math.ceil(n/5)) + S_naive(math.floor(7*n/10)))


def M(n: int, m_map: dict) -> int:
    # print(f"n:\t{n}")
    if n <= 1:
        return 0

    if n in m_map.keys():
        return m_map[n]

    m_map[n] = M(math.floor(n/2), m_map) + M(math.ceil(n/2), m_map) + n - 1
    return m_map[n]


def S(n: int, s_map: dict, m_map: dict) -> int:
    if n < 100:
        return M(n, m_map)

    if n in s_map.keys():
        return s_map[n]

    s_map[n] = min(M(n, m_map),
                   8*math.ceil(n/5) + S(math.ceil(n/5), s_map, m_map) + S(math.floor(7*n/10), s_map, m_map))
    return s_map[n]


def bs(lo: int, hi: int, s_map: dict, m_map: dict) -> int:
    local_best = hi
    while lo < hi:
        mid = int(lo + (hi-lo)//2)

        if S(mid, s_map, m_map) < (2/3) * M(mid, m_map):
            # Big enough, try to decrease n
            local_best = mid
            hi = mid
        else:
            # Too small, increase n
            lo = mid+1

    return local_best


def clear(s_map: dict, m_map: dict) -> None:
    s_map.clear()
    m_map.clear()


def dumbsearch(n: int, s_map: dict, m_map: dict) -> int:
    clear(s_map, m_map)
    while S(n, s_map, m_map) > (2/3) * M(n, m_map):
        n += 1
    return n


if __name__ == '__main__':
    n0 = 324
    # print(S_naive(n0))
    # print("--------")
    # print(M_naive(n0))
    #
    # print(">>><<<")

    m_map = {}
    s_map = {}
    # print(S(n0, s_map, m_map))
    # print("--------")
    # print(M(n0, m_map))
    ans1 = bs(n0, int(5e6), s_map, m_map)
    ans2 = bs(0, int(1e7), s_map, m_map)
    dumbans = dumbsearch(n0, s_map, m_map)
    print(f"Answer by iterating up from n0:\t{dumbans}")
    print(f"Answer by binary searching on [0, 1e7]:\t{ans1}")
    print(f"Answer by binary searching on [n0, 5e6]:\t{ans2}")

    for ans in [ans1, ans2, dumbans]:
        print("----")
        print(f"S(n) < (2/3) * M(n):\t{S(ans, s_map, m_map) < (2 / 3) * M(ans, m_map)}")
        print(f"S(n-1) >= (2/3) * M(n-1):\t{S(ans - 1, s_map, s_map) >= (2 / 3) * M(ans - 1, m_map)}")
        print(f"Answer < 5 *10^6:\t{ans < 5e6}")
