array = [1,5,72,42,100]
issorted = True
for i in range (len(array)-1):
    if array[i] >array[i+1]:
        issorted = False
        break
    print(issorted)