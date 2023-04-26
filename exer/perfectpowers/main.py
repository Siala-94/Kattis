
import sys
import random

# find all prime numbers up to v
# 4294967295
# 2146483647
# 17 -> 1
# 8 -> 3
# 1073741824 -> 30


# 2147483646 -> 1

# 2147383646
#
#
#

def getrand():
    v = random.randint(3, 2147483647)

    return v


done = False
while not done:

    v = int(sys.stdin.readline())
    # v = getrand()

    if v == 0:

        done = True
        pass

    else:
        x = abs(v)
        found = False
        max_limit = int(x**0.5)
        if (x == 2 or x == 3):
            print(1)

        b = 2
        while b < max_limit+1:
            p = 0
            x = abs(v)
            while x % b == 0:
                x //= b
                p += 1

            if x == 1 and ((v < 0 and p % 2 == 1) or v > 0):
                print(int(p))
                found = True
                break
            # prime number
            b += 1
        if found != True:
            print(1)
