number = "112523344"

count = 1
number_container = 'A'
temp = 0
for i in number:
    number_container1 = int(number) % 10
    print(number_container1)
    number = int(int(number)/10)
    print(number)
    number_container2 = int(number) % 10
    print(number_container2)
    number = int(int(number)/10)
    
    if(str(number_container1) == str(number_container2)):
        continue
    elif(number_container1 != number_container2):
        print("NUMBER NOT REPEATED IS: ",number_container2)
        exit()
    

