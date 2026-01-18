# this code finds the minimum and maximum values in an array
arr =[4, 2, 1, 4, 5, 4, 3, 2, 5, 6]

min_val = arr[0]
max_val = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
    if arr[i] > max_val:
        max_val = arr[i]

print("Min:", min_val)
print("Max:", max_val)
