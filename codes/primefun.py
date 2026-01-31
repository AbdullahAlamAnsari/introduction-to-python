def prime(number,temp):
    print("TEMP: ",temp)
    print("NUMBER: ",number)
    if temp == 1:
        print("Number is prime")
        return

    else:
        if(number%temp==0 and temp>1):
            print("Number is not prime")
            return
        elif(number%temp!=0):
            return prime(number,temp-1)





n = int(input("Enter the number: "))
temp = n-1
print(temp)
prime(n,temp)