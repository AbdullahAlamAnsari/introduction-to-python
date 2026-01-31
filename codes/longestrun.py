l = [1, 2, 3, 4]
result = []

for i in range(len(l)):
    product = 1
    for j in range(len(l)):
        if i != j:
            product = product * l[j]
    result.append(product)

print(result)
