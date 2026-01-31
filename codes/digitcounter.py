number = (input("Enter the number: "))
divisor = 1
i = 1
for i in enumerate(number,start = 1):
    
    
    divisor = divisor*10

divisor = int(divisor/10)

print(divisor)
count = 0
remainingnum = 0
while number!= 0:
    number = int(int(number)/10)
    print("REMAIN: ",number)
    count += 1

    

print("THE FOLLOWING NUMBER HAS :",count," DIGITS")