arr = [3,2,0]
n = len(arr)
expected_sum = n*(n+1)//2
actual_sum = sum(arr)
missing_value = expected_sum - actual_sum
print(missing_value)