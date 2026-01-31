l = [2,5,7,4,8,7]
l1 = [5,8,3,7,9]

l3 = l1+l
unique = []
for i in l3:
    if i not in unique:
        unique.append(i)

print("FIRST LIST ELEMENTS: ",l)
print("SECOND LIST ELEMENTS: ",l1)
print("COMBINED LIST ELEMENTS: ",l3)
print("ONLY UNIQUE ELEMENTS LIST: ",unique)



l4 = [1,2,3,2,1]
palindromelist = []


for i in range(len(l4)-1,-1,-1):
    palindromelist.append(l4[i])


if(palindromelist == l4):
    print("LIST IS PALINDROME")
else:
    print("LIST IS NOT PALINDROME")


l6 = [[1,2],[3,4],[5]]
l7 = [i for rows in l6 for i in rows]
print(l7)
number = int(input("Enter the number: "))
sumlist = [1,2,3,4,5]
lsum = [(x,y) for x in sumlist for y in sumlist if x+y==number ]
print(lsum)
