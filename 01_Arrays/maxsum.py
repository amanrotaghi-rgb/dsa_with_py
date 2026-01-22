array = [2,3,5,7,1,3,4,2,-2,-4,4,5,100]
current_sum = array[0]
max_sum = array[0]
for i in range(1, len(array)):
    current_sum = max(array[i], current_sum + array[i])
    max_sum = max(current_sum, max_sum)
    print(max_sum)