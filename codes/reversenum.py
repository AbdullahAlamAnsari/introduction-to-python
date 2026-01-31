number = int(input("Enter the number: "))


temp = 0
for i in str(number):
    temp = ((number%10) + temp)*10
    
    print("TEMP: ",temp)
    number = int(number/10)
    print("NUMBER: ",number)

temp = temp/10
print(temp)