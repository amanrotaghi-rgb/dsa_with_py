array = [2,3,4,5,6,7]
n = len(array)
k = 2 #number of rotations
k = k%n

result = array[k:] + array[:k]
print(result)