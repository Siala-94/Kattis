import sys


def shouldadd(i, S):
    list_of_digits = [int(n) for n in str(i)]
    ans = 0
    if len(list_of_digits) == 1:
        ans = list_of_digits[0]
    else:
        for dig in list_of_digits:
            ans += dig
    ret = True if ans == S else False
    return ret


A, B, S = sys.stdin.readline().split()

ans = []
for i in range(int(A), int(B)+1):
    if shouldadd(i, int(S)):
        ans.append(i)
print(len(ans))
print(ans[0])
