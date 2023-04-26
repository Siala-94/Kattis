import math
import sys


def factorize(n):
    factors = {}
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
        else:
            i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def div_factorial(n, factors):
    for f, exp in factors.items():
        i = f
        factor_exp = 0
        while i <= n:
            factor_exp += n // i
            i *= f
        if factor_exp < exp:
            return False
    return True


ans = []
while True:
    try:
        n, m = map(int, sys.stdin.readline.split())

        if m == 0:
            print(m + " does not divide " + n + "!")
        else:
            factors_m = factorize(m)
            factors_m.pop(1, None)

            if div_factorial(n, factors_m):
                print((str(m) + " divides " + str(n) + "!"))
            else:
                print(m + " does not divide " + n + "!")
    except:
        EOFError
