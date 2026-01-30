x = 5

def fun():
    global x
    x = x + 1
    y = x + 2
    print(y)

fun()
print(x)
