array = [1,2,3,2,3,5,6,3,4,2,4]
seen = set()
result = []
for x in array:
    if x not in seen:
        result.append(x)
        seen.add(x)
print(result)
             