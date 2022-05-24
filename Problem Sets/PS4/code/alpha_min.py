def alpha_min(s: str) -> int:
    """Return the smallest index k such that s[k:len(s)] is sorted.
    Precondition: s is non-empty. """
    i = len(s) - 1
    while i > 0 and s[i-1] <= s[i]:
        i = i - 1
    return i
