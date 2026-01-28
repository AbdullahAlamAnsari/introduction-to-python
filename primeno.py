primeno = int(input("ENTER THE NUMBER: "))

if primeno <= 1:
    print("NUMBER IS NOT PRIME")
else:
    is_prime = True

    for i in range(2, primeno):
        if primeno % i == 0:
            is_prime = False
            break

    if is_prime:
        print("THE NUMBER IS A PRIME NUMBER")
    else:
        print("NUMBER IS NOT PRIME")
