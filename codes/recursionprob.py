

def factorial_count(number):
    if(number == 0):
        return 1

    else:
        return (number) * (factorial_count(number-1))

def sum_till_1(number):
    if number == 0:
        return 0
    else:
        return number + sum_till_1(number - 1)


def reversenum(number,reversed):
    while(number!=0):
        reversed = int((reversed*10) + (number%10))
        number = int(int(number)/10)

    print("REVERSED NUMBER IS: ",reversed)

choice = 0

while(choice!=4):
    choice = int(input("---USER MENU---\n1.FACTORIAL\n2.REVERSE NUMBER\n3.SUM TILL ONE\n4.EXIT\n"))
    match choice:
        case 1:
            factorial = int(input("Enter the number: "))
            print("FACTORIAL OF ",factorial," IS ",factorial_count(factorial))
            break
        case 2:
            reversed = 0
            revnum = int(input("ENTER THE NUMBER TO BE REVERSED: "))
            reversenum(revnum,reversed)
            break
        case 3:
            factorial = int(input("Enter the number: "))
            print("THE SUM OF ",factorial," TILL 1 IS :",sum_till_1(factorial))
            break
        case 4:
            pass
        case _:
            print("INVALID INPUT")








