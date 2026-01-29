length = int(input("Enter the height of the pyramid"))

length = length + 1
for i in range(0,length):
    for j in range(i):
        print(i,end = '')
    print()