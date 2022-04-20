import matplotlib.pyplot as plt
import numpy as np


def big_short(lst: list, t: int) -> int:
    ''' Return the length of a shortest slice of lst whose sum is at least t
            (return len(lst) + 1 if sum(lst) < t).  Preconditions: t >= 0;
            lst is non-empty; every element of lst is non-negative. '''
    n = len(lst)
    total = 0
    m = n + 1  # min length found so far
    for i in range(n):  # Loop 1
        j = i
        s = 0  # sum of lst[i:j]
        while s < t and j < n:  # Loop 2
            s = s + lst[j]
            j = j + 1
            total += 1
        if s >= t and j - i < m:
            m = j - i
    return total


if __name__ == "__main__":
    xs = list(range(200))
    lst = []
    for x in xs:
        lst.append(1)
    ys = [big_short(lst, x) for x in xs]
    ys2 = [200 * np.log2(x+1) for x in xs]

    plt.plot(xs, ys, label='true')
    plt.plot(xs, ys2, label='expected')
    plt.legend()
    plt.show()
