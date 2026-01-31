def palindrome_check(number):
    palindrome = 0
    origional = number

    while(number!=0):
        print("PALINDROME: ",palindrome)
        print("NUMBER: ",number)
        palindrome = (palindrome*10) + (int(int(number)%10))
        
        number = int(int(number)/10)


    if(palindrome==origional):
        print("PALINDROME")
    else:
        print("NOT A PALINDROME")
        


print(palindrome_check(123))
