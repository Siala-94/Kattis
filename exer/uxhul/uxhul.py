n = int(input())

for i in range(n):
    m = int(input())
    preferences = [list(map(int, input().split())) for _ in range(m)]

    # initialize the stones to all black (no)
    stones = ["N", "N", "N"]

    # iterate over each priest in order of age
    for p in preferences:
        # find the stone that gives the priest the highest preference
        best_stone = None
        best_preference = float("inf")
        for j in range(3):
            # calculate the preference for flipping this stone
            flipped_stones = stones[:]
            flipped_stones[j] = "Y" if stones[j] == "N" else "N"
            preference = p[flipped_stones.index(
                "Y") * 4 + flipped_stones.index("N")]

            # update the best stone if this one has higher preference
            if preference < best_preference:
                best_stone = j
                best_preference = preference

        # flip the chosen stone
        stones[best_stone] = "Y" if stones[best_stone] == "N" else "N"

    # print the final outcomes
    print("".join(stones))
