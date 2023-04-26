def factorial(start, end):
    if start > end:
        return 1
    if start == end:
        return start
    mid = (start + end) // 2
    return factorial(start, mid) * factorial(mid + 1, end)


n = int(input())

result = factorial(1, n)

while result % 10 == 0:
    result //= 10

ans = str(result)[-3:]
print(ans)
