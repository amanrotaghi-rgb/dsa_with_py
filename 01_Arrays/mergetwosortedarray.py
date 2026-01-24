arr1 = [2,5,8]
arr2 = [3,7,8]
i = 0
j = 0
result = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
       result.append(arr1[i])
       i += 1
    else:
        result.append(arr2[j])
        j += 1
print(result)