

def isPrime(m):
    if m == 1:
        return False

    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True


def getNextNumber(m):
    return sum(int(digit)**2 for digit in str(m))


def isHappy(m):
    seen_numbers = set()
    while m != 1:
        if m in seen_numbers:
            return False
        seen_numbers.add(m)
        m = getNextNumber(m)
        if m == 1:
            return True


for p in range(int(input())):
    k, m = map(int, input().split())

    print(k, m, "YES" if isPrime(m) and isHappy(m) else "NO")
