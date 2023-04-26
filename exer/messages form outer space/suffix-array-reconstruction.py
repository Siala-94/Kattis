t = int(input())
ans = []
for _ in range(t):
    l, s = map(int, input().split())

    word = ['_'] * l
    possible = True

    for _ in range(s):
        p, suffix = input().split()
        p = int(p)

        for k, c in enumerate(suffix):
            if c == '*':
                p = l - len(suffix) + 1
                continue

            if word[p+k-1] != '_':
                if word[p+k-1] != c:
                    possible = False
                continue

            word[p+k-1] = c

    if '_' not in word and possible:
        ans.append(''.join(word))
    else:
        ans.append('IMPOSSIBLE')
for a in ans:
    print(a)
