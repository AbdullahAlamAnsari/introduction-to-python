number = input("Enter the number please: ")

num = 0
cube_sum = 0
for i in number:
    num = int(int(number)%10)
    number = int(int(number)/10)
    cube_sum = cube_sum + (num*num*num)



print(cube_sum)