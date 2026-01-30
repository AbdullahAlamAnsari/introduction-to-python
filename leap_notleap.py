year = int(input("Enter the year: "))



if((year%4==0    and year%100!=0) or year%400==0):
    print("THE YEAR IS LEAP YEAR")

else:
    print("THE YEAR IS NOT A LEAP YEAR")