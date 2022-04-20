import matplotlib.pyplot as plt
from math import log2, floor


def algo_s(n):

    total = 0
    i = 0
    j = 1
    while i < n:
        i = i + j
        if n % 2 == 0:
            j = j + 1
        total += 1
    return total


if __name__ == "__main__":
    xs = list(range(200))
    ys = [algo_s(2*x) for x in xs]
    ys3 = [algo_s(2*x + 1) for x in xs]

    ys2 = [(floor(log2(x+1)) + 1)*2 for x in xs]

    plt.plot(xs, ys, label='true')
    plt.plot(xs, ys3, label='expected')
    plt.legend()
    plt.show()
