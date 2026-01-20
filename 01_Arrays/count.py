array = [2,3,1,3,2,1,2,3,4]
freq = {}

for x in array :
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)        