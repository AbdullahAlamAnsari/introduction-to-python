limit = int(input("Enter limit: "))

a, b = 0, 1
score = 0

while a <= limit:
    print(a, end=" ")
    score += a
    a, b = b, a + b

print("\nSum:", score)
