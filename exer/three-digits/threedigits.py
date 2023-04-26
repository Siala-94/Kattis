import sys
number = int(sys.stdin.readline())
result = 1

for i in range(2, number+1):
    result *= i

    while result % 10 == 0 and result != 0:
        result //= 10

    result %= 10**12

print(str(result)[-3:])
