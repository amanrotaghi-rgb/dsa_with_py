arr = [2, 7, 11, 15]
target = 9

seen = set()

for x in arr:
    needed = target - x
    if needed in seen:
        print(True)
        break
    seen.add(x)
else:
    print(False)
