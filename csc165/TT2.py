from math import ceil


def blah(n: int) -> None:
    i = 3 * n - 1
    x = 0
    bools = []
    while i > 0:  # Loop 1
        j = 1
        while j < i:  # Loop 2
            j = j + 7
            x += 1
        # print(f"{i=}, {x=}, {ceil((i-1)/7) == x}")
        bools.append(ceil((i-1)/7) == x)
        i = i - j
    return bools


bools = []
for n in range(5000):
    bools.extend(blah(n))

print(all(bools))
