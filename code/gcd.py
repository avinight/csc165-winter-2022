def gcd(m: int, n: int) -> int:

    small = n
    if m < n:
        small = m
    for i in range(1, small+1):
        if((m % i == 0) and (n % i == 0)):
            gcd = i

    return gcd
