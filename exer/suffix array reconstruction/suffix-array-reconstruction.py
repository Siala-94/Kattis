def reconstruct_string(l, s, suffixes):
    # Initialize set of possible characters for each position in the string
    possible_chars = [set() for _ in range(l)]

    # Iterate over suffixes and update possible_chars set
    for pos, suffix in suffixes:
        for i, c in enumerate(suffix):
            if c == '*':
                possible_chars[pos + i].update(
                    set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            else:
                possible_chars[pos + i].add(c)

    # Check if there is a unique character in each set
    for char_set in possible_chars:
        if len(char_set) != 1:
            return "IMPOSSIBLE"

    # Reconstruct string
    res = ""
    for char_set in possible_chars:
        res += char_set.pop()

    return res


# Read number of test cases
t = int(input())

for _ in range(t):
    l, s = map(int, input().split())
    suffixes = []
    for _ in range(s):
        pos, suffix = input().split()
        suffixes.append((int(pos)-1, suffix))  # Adjust pos to 0-based index
    # Reconstruct string and print result
    print(reconstruct_string(l, s, suffixes))
