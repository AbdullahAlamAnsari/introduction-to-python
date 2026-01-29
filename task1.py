number = int(input("Enter the number: "))
if(number%2 ==0):
    print("The number is even")
else:
    print("The number is odd")


if(number>0):
    print("The number is positive")
elif(number<0):
    print("The number is negative")
else:
    print("The number is zero")

number1 = int(input("You can enter the second number to calculate: "))

op = (input("Enter operator (+, -, *, /):"))

match op:
    case "+":
        print(number+number1)
    case "-":
        print(number-number1)
    case "*":
        print(number*number1)
    case "/":
        print(float(number)/float(number1))



print("We are going to print the factorial of the number 1")
factorial = 1
temp = 1
while temp<=number:
    factorial = factorial * temp 
    temp += 1

print(factorial)


