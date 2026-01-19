array = [2,3,5,9,5,6,4,2,51,]
start = 0
end = len(array)-1
while start <end:
    array[start],array[end] = array[end],array[start]
    start +=1
    end  -=1
    print(array)