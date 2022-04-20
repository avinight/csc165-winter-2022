import matplotlib.pyplot as plt


def my_func(n):
    total = 0
    i = 0
    while i < n:  # Loop 1
        for j in range(n * n):  # Loop 2
            total += 1
        i = i + 2

    return total


if __name__ == "__main__":
    xs = list(range(200))
    ys = [my_func(x) for x in xs]
    ys2 = [x**3 / 2 for x in xs]

    plt.plot(xs, ys, label='true')
    plt.plot(xs, ys2, label='expected')
    plt.legend()
    plt.show()
