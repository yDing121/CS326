
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
        print(f"Answer < 5 *1