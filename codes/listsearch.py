
l = [2,3,5,6,6,4,2]

count = 0

for i in l:
    count = 0
    for j in l:
        if(i == j):
            count += 1
    
    print(i , " OCCURED ", count , " TIMES")
