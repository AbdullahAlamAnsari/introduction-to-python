number = input("ENTER THE NO: ")
largest = 0
for i in number:
    for j in number:
        if(int(j)>int(i)):
        
            largest = int(j)
        elif(int(j)<int(i)):
          
            largest = int(i)
        elif(int(j)==int(i)):  
            pass
       

print("LARGEST NO IS: ",largest)