from math import floor
from random import shuffle


class MultiSet:
    def __init__(self):
        self.elements = []

    def select(self, k):
        a2 = self.elements.copy()
        a2.sort()
        return a2[k-1]

    def insert(self, x):
        self.elements.append(x)

    def DeleteLargerHalf(self):
        n = len(self.elements)
        if n == 0:
            return

        k = floor(n / 2)

        median = self.select(k)

        count_greater = 0 # Elements > median
        count_equal = 0 # Elements == median
        for x in self.elements:
            if x > median:
                count_greater += 1
            elif x == median:
                count_equal += 1

        del_median = k - count_greater # In the case where we have duplicate medians, we may need to delete some but not all of them

        arr = []
        equal_m_kept = count_equal - del_median
        for x in self.elements:
            if x < median:
                arr.append(x)
            elif x == median and equal_m_kept > 0:
                arr.append(x)
                equal_m_kept -= 1

        self.elements = arr

    def output_elements(self):
        for x in self.elements:
            print(x, end=" ")
        print()

if __name__ == '__main__':
    ms = MultiSet()
    a = []
    for i in range(9):
        a.append(i)

    shuffle(a)

    for i in a:
        ms.insert(i)

    ms.output_elements()
    ms.DeleteLargerHalf()
    ms.output_elements()