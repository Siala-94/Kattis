import sys


def amountofodd(s):
    unmp = {}
    odd = 0
    for i in s:
        if unmp.get(i) == None:
            unmp[i] = 1
        else:
            unmp[i] += 1
    for i in unmp:
        if unmp[i] % 2 != 0:
            odd += 1
    return odd


def palindrome(s):
    s = list(s)[:-1]
    i = 0
    j = len(s)-1
    swaps = 0
    if (amountofodd(s) > 1):
        return -1

    while i < j:
        # if same iterate
        if s[i] == s[j]:
            i += 1
            j -= 1

        else:
            k = j

            while s[k] != s[i] and k > i:
                k -= 1

            if k == i:
                s[i], s[i+1] = s[k+1], s[k]
                swaps += 1
            else:
                while k < j:
                    s[k], s[k+1] = s[k+1], s[k]  # swap characters
                    k += 1
                    swaps += 1
    return swaps


for _ in range(int(sys.stdin.readline())):
    count = palindrome(sys.stdin.readline())
    print(count if count >= 0 else "impossible")
