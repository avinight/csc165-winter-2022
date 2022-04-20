import matplotlib.pyplot as plt
from math import log2, floor


def dec2_bin(n):

    total = 0
    while n > 0:
        j = 0
        while 2 ** j <= n:
            j = j + 1
            total += 1
        n = n - 2 ** (j - 1)

    return total


if __name__ == "__main__":
    xs = list(range(200))
    ys = [dec2_bin(x) for x in xs]
    ys2 = [(floor(log2(x+1)) + 1)*2 for x in xs]

    plt.plot(xs, ys, label='true')
    plt.plot(xs, ys2, label='expected')
    plt.legend()
    plt.show()
