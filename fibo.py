fibono = int(input("Enter the number: "))
score = 1
temp = 0
count = 0


if(fibono == 1):
    print(0)
    exit()
if(fibono == 0):
    print(1)
    exit()

  
while count < fibono:
    temp,score = score,temp+score

    print(temp)
    count += 1


print(temp)


