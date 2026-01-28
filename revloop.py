i = 1
while(i<=20):
    print(i)
    i = i+1

text = "geeksforgeeks"
j = 0
for i in text:
    j += 1
    pass


print("STRING LENGTH: ",j)

for i in range(1,20):
    if(i%3 == 0):
        continue
    if(i == 17):
        break

    print("NUMBER IS: ", i)