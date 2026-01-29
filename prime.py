prime = int(input("Enter the number: "))
check = prime-1
checkprime = True

if(prime == 1 or prime == 0):
    print("NUMBER IS NOT PRIME")
    exit()

while(check!=1):
    if(prime%check == 0):
        checkprime = False
    check -= 1


if(checkprime):
    print("THE NUBER IS PRIME")
elif(checkprime == False):
    print("NOT A PRIME NO")