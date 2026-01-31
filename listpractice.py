l = [1,2,3,4,5]


for i in l:
    print(i)

print("LENGTH OF LIST IS: ",len(l))

sum = 0
for j in l:
    sum = sum + j
largest = 0
for k in l:
    for m in l:
        if(m>k):
            largest = m
        else:
            largest = k

smallest = 0

smallest = l[0]

for i in l:
    if i < smallest:
        smallest = i

counteven = 0
countodd = 0
for i in l:
    if(i%2==0):
        counteven += 1
    else:
        countodd += 1



print("SUM OF ALL THE NUMBERS IS: ",sum)
print("LARGEST NUMBER IS: ",largest)
print("SMALLEST NUMBER IS: ",smallest)
print("NUMBER OF ODD TERMS IN THE LIST: ",countodd)
print("NUMBER OF EVEN TERMS IN THE LIST: ",counteven)

l1 = [2,5,3,6,8]
l1.sort()
l2 = l1.copy()
print("SORTED FORM OF LIST 1: ",l1 ," IS ",l2)

my_list = [10, 20, 30, 40, 50]
revlist = []
for i in range(len(my_list) - 1, -1, -1):
    revlist.append(my_list[i])
    print(revlist)




searchlist = [1,2,3,4,5,6,7,8,9]
numbersearch = int(input("ENTER THE NUMBER: "))

for index,i in enumerate(searchlist,start = 0):
    if(i == numbersearch):
        print("REPEATED NUMBER FOUND: ",i ," INDEX ",index)
        break

repeatedlist = [1,2,2,5,8,4,4,3]

repeatedlist = [1,2,2,5,8,4,4,3]
unique = []

for i in repeatedlist:
    if i not in unique:
        unique.append(i)

print(unique)
