import matplotlib.pyplot as plt
from math import ceil


def long_prod(lst: list, t: int) -> int:
    """Return the maximum length of any slice of lst whose product is at most t.
    Preconditions: t > 0; lst is non-empty; every element of lst is positive.
    """
    m = 0  # max length found so far
    for i in range(1, len(lst) + 1):       # Loop 1
        j = i - 1
        p = 1  # product of lst[j+1:i]
        while j >= 0 and p * lst[j] <= t:  # Loop 2
            p = p * lst[j]
            j = j - 1
        j = j + 1
        if i - j > m:
            m = i - j
    return m


if __name__ == "__main__":
    xs = list(range(200))
    lst = []
    for _ in lst:
        lst.append(200**(1/3))
    ys = [long_prod(lst, ceil(x ** ((1/3) ** (x ** (1/3))))) for x in xs]
    ys2 = [x**(4 / 3) for x in xs]

    plt.plot(xs, ys, label='true')
    plt.plot(xs, ys2, label='expected')
    plt.legend()
    plt.show()
