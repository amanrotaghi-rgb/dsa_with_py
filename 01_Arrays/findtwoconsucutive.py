arr = [100, 4, 200, 1, 3, 2]

num_set = set(arr)
longest = 0

for x in num_set:
    if x - 1 not in num_set:      # sequence start
        current = x
        count = 1

        while current + 1 in num_set:
            current += 1
            count += 1

        longest = max(longest, count)

print(longest)

