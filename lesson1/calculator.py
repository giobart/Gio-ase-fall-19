def sum(m, n):
    addend = 1

    if(n < 0):
        addend = -1
        n *= -1

    while(n > 0):
        m += addend
        n = n-1

    return m


def divide(m, n):
    result = 0
    sign1 = 1
    sign2 = 1

    if(m < 0):
        sign1 = -1
        m = abs(m)

    if(n < 0):
        sign2 = -1
        n = abs(n)

    sign1 = sign1 * sign2

    while(m > 0):
        m -= n
        if(m >= 0):
            result += 1

    return result * sign1


def sub(m, n):
    return sum(m, -n)


def multiply(m, n):
    result = 0
    sign1 = 1
    sign2 = 1

    if(m < 0):
        sign1 = -1
        m = abs(m)

    if(n < 0):
        sign2 = -1
        n = abs(n)

    sign1 = sign1 * sign2

    while (n > 0):
        n -= 1
        result = sum(result, m)

    return result * sign1


print("10/5= ", divide(10, 5))
print("5+5", sum(5, 5))
print("10/3= ", divide(10, 3))
print("5+1", sum(5, 1))
print("3/1= ", divide(3, 1))
print("0+0", sum(0, 0))
print("10/5= ", divide(10, 5))
print("3+3", sum(3, 3))
print("-3+3", sum(-3, 3))
print("-3-3", sum(-3, -3))
print("-10/5= ", divide(-10, 5))
print("10/-5= ", divide(10, -5))
print("-3-3=", sum(-3, 3))
print("-3-(-3)=", sum(-3, -3))
print("3-3=", sum(3, -3))
print("10-3=", sum(10, -3))
print("3* -3=", multiply(3, -3))
print("-3 * -3=", multiply(-3, -3))
