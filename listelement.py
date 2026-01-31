l = [10, 5, 20, 8, 15]

largest = l[0]
second_largest = -1  

for i in l:
    if i > largest:
        second_largest = largest
        largest = i
    elif i != largest and i > second_largest:
        second_largest = i

print("Second largest:", second_largest)
