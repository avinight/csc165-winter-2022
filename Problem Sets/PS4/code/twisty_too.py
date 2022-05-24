def twisty_too(n: int) -> None:
    """Precondition: n > 0."""
    i = n
    while i > 0:          # Loop 1
        s = -1
        j = 0
        while j < i:      # Loop 2
            s = s + 2
            j = j + s
        i = i - 1
        while i % 4 > 0:  # Loop 3
            i = i - 1
