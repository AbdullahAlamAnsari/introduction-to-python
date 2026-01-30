square = lambda x : x**2


print(square(2))


check = (lambda x : "POSITIVE" if x>0 else "NEGATIVE" if x<0 else "ZERO")

print(check(10))



dict = [1,2,3,4,5,6]


even = filter(lambda x : x%2==0,dict)

print(list(even))

sum_mul = lambda a,b : (a+b,a*b)

print(sum_mul(4,5)) 