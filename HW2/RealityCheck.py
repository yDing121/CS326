import math
import numpy as np

# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
#
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Lance Ding



def M(n: int, m_map: np.ndarray) -> int:
    if n <= 1:
        return 0

    if m_map[n] > 0:
        return m_map[n]

    m_map[n] = M(math.floor(n/2), m_map) + M(math.ceil(n/2), m_map) + n - 1
    return m_map[n]


def S(n: int, s_map: np.ndarray, m_map: np.ndarray) -> int:
    if n < 100:
        return M(n, m_map)

    if s_map[n] > 0:
        return s_map[n]

    s_map[n] = min(M(n, m_map),
                   8*math.ceil(n/5) + S(math.ceil(n/5), s_map, m_map) + S(math.floor(7*n/10), s_map, m_map))
    return s_map[n]




def dumbsearch(n: int, s_map: np.ndarray, m_map: np.ndarray) -> int:
    while 3 * S(n, s_map, m_map) > 2 * M(n, m_map):
        n += 1
    return n


if __name__ == '__main__':
    n0 = 324

    m_map = np.zeros(int(1e7), dtype=int)
    s_map = np.zeros(int(1e7), dtype=int)

    # Verify n0
    n0_ver = 0
    while S(n0_ver, s_map, m_map) >= M(n0_ver, m_map):
        n0_ver += 1
    print(f"Empirical n0:\t{n0_ver}\nS:\t{S(n0_ver, s_map, m_map)}\nM:\t{M(n0_ver, m_map)}")
    print(f"Empirical n0 == given n0 == 324?\t{n0 == n0_ver}")
    print("=="*10)

    ans = dumbsearch(n0_ver, s_map, m_map)
    print(f"Answer by iterating up from n0:\t{ans}\nS:\t{S(ans, s_map, m_map)}\nM:\t{M(ans, m_map)}")
    print("--"*10)
    print(f"S(n) < (2/3) * M(n):\t{S(ans, s_map, m_map) < (2 / 3) * M(ans, m_map)}")
    print(f"S(n-1) >= (2/3) * M(n-1):\t{S(ans - 1, s_map, s_map) >= (2 / 3) * M(ans - 1, m_map)}")
    print(f"Answer < 5 *10^6:\t{ans < 5e6}")
