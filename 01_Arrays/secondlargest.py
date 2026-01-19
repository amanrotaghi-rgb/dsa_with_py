array = [4,6,7,3,9]
largest = array[0]
second_l = -1
for i in range(1,len(array)):
    if array[i]>largest:
        second_l = largest
        largest = array[i]
    elif array[i] < largest and array[i]>second_l:
        second_l = array[i]


print("second largest is :",second_l)
