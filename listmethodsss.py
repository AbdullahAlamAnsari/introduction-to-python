l1 = []

for i in range(5):
    i = int(input("ENTER THE NUMBER TO BE ADDED IN THE LIST: "))
    l1.append(i)

print(l1)


l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)



lnum = [2,7,4,7,3,9,1]
leven = []

for i in lnum:
    if(i%2==0):
        leven.append(i)


print(leven)


l3 = [x*2 for x in lnum]
print(l3)