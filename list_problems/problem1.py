l = []

for j in range(5):
    num = int(input("Enter the number: "))
    l.append(num)


for i in range(5):
    print(l[i])

sum = 0
for k in l:
    sum = sum + k


print("SUM OF ALL THE ELEMENTS: ",sum)
smallest = l[0]
largest = l[0]
for m in l:
    if m>largest:
        largest = m
    if m<smallest:
        smallest = m

print("SMALLEST NUMBER IS: ",smallest)
print("LARGEST NUMBER IS: ",largest)


for i in l:
    pass

print("TOTAL NUMBER OF ELEMENTS: ",i+1)


even = 0

for i in l:
    if i%2==0:
        even += 1

print("EVEN NUMBER IS: ",even)



number = int(input("Enter the number: "))
index = int(input("Enter the number: "))

for i in range(len(l)):
    if i == index:
        l[i] = number

print(l)
f = [2,3,4,2,2,3]
unique = []

for i in f:
    if i not in unique:
        unique.append(i)

print(unique)
            

l5 = [0,3,3,0,5,0,2]

count_zero = l5.count(0)

l5 = [i for i in l5 if i != 0]   # remove zeros
l5.extend([0] * count_zero)     # add zeros at end

print(l5)
